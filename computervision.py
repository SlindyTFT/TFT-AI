import pyautogui
import pydirectinput as pdi
from PIL import Image, ImageFilter, ImageOps
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
from units import UNIT_DICT, UNIT_POOL
from positions import SHOP_POSITIONS, PLAYER_BOARD_POSITIONS, STAGE_POSITIONS, GOLD_POSITIONS, ITEM_POSITIONS_MOUSE, \
    ITEM_POSITIONS, BENCH_POSITIONS, HIGHLIGHT_UNIT_POSITION, AUGMENT_POSITIONS
from items import BASE_ITEMS
import numpy as np
import re
import time

def normalize_name(text):
    text = text.strip()
    text = re.sub(r"[^A-Za-z]", "", text)  # remove spaces, hyphens, apostrophes
    return text.lower()

UNIT_LOOKUP = {
    normalize_name(unit.name): unit
    for unit in UNIT_POOL
}

def get_shop():
    current_shop = [None] * 5
    for i in range(5):
        im = pyautogui.screenshot(f"Screenshots/Unit Screenshots/screenshot{i}.png", region = (SHOP_POSITIONS[i]))
        img = Image.open(f"Screenshots/Unit Screenshots/screenshot{i}.png")
        # Convert to grayscale
        img = ImageOps.grayscale(img)

        # Increase contrast slightly
        img = ImageOps.autocontrast(img)

        # Optional: sharpen edges (helps with small fonts)
        img = img.filter(ImageFilter.SHARPEN)

        # 3) normalize + tame jaggies
        # img = img.filter(ImageFilter.GaussianBlur(0.6))

        # Optional: resize to improve clarity (Tesseract likes bigger text)
        # img = img.resize((img.width * 3, img.height * 3))

        config = (
            "--oem 3 "
            "--psm 7 "  # single line (shop name)
            "-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
            "-c user_words_suffix=tft_units "
        )
        text = pytesseract.image_to_string(img, config = config)
        cleaned_text = text.replace("\n", "")
        norm = normalize_name(cleaned_text)
        unit = UNIT_LOOKUP.get(norm)


        current_shop[i] = unit
        if current_shop[i] is None:
            if norm == 'maoi':
                current_shop[i] = UNIT_LOOKUP.get('illaoi')
                continue
            cleaned_text = text.replace("\n", "")
            length = len(cleaned_text)
            if length > 0:
                for j in range(length):
                    if UNIT_LOOKUP.get(normalize_name(cleaned_text[:length - j])) is not None:
                        current_shop[i] = UNIT_LOOKUP.get(normalize_name(cleaned_text[:length - j]))
                        break
    return current_shop

def get_highlighted_unit():
    # im = pyautogui.screenshot(f"Screenshots/Unit Screenshots/current_unit.png", region=(HIGHLIGHT_UNIT_POSITION[0]))
    # img = Image.open(f"Screenshots/Unit Screenshots/current_unit.png")

    im = pyautogui.screenshot(region=(HIGHLIGHT_UNIT_POSITION[0]))
    img = im

    # Convert to grayscale
    img = ImageOps.grayscale(img)

    # Increase contrast slightly
    img = ImageOps.autocontrast(img)

    # Optional: sharpen edges (helps with small fonts)
    img = img.filter(ImageFilter.SHARPEN)

    # 3) normalize + tame jaggies
    # img = img.filter(ImageFilter.GaussianBlur(0.6))

    # Optional: resize to improve clarity (Tesseract likes bigger text)
    # img = img.resize((img.width * 3, img.height * 3))

    config = (
        "--oem 3 "
        "--psm 7 "  # single line (shop name)
        "-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
        "-c user_words_suffix=tft_units "
    )
    text = pytesseract.image_to_string(img, config=config)
    cleaned_text = text.replace("\n", "")
    norm = normalize_name(cleaned_text)
    unit = UNIT_LOOKUP.get(norm)
    if unit is None:
        if norm == 'maoi' or norm == 'lilaoi':
            return UNIT_LOOKUP.get('illaoi')
        cleaned_text = text.replace("\n", "")
        length = len(cleaned_text)
        if length > 0:
            for j in range(length):
                if UNIT_LOOKUP.get(normalize_name(cleaned_text[:length - j])) is not None:
                    return UNIT_LOOKUP.get(normalize_name(cleaned_text[:length - j])).__copy__()
    if unit is None:
        return None
    else:
        return unit.__copy__()

def get_highlighted_cost():
    # im = pyautogui.screenshot(f"Screenshots/highlighted cost.png", region = (HIGHLIGHT_UNIT_POSITION[1]))
    # img = Image.open(f"Screenshots/highlighted cost.png")

    im = pyautogui.screenshot(region = (HIGHLIGHT_UNIT_POSITION[1]))
    img = im

    # Convert to grayscale
    img = ImageOps.grayscale(img)

    # Increase contrast slightly
    img = ImageOps.autocontrast(img)

    # Optional: sharpen edges (helps with small fonts)
    img = img.filter(ImageFilter.SHARPEN)

    # 3) normalize + tame jaggies
    img = img.filter(ImageFilter.GaussianBlur(0.6))

    # # Optional: resize to improve clarity (Tesseract likes bigger text)
    # img = img.resize((img.width * 2, img.height * 2), Image.NEAREST)

    thr = 140
    img = img.point(lambda p: 255 if p > thr else 0)

    img.save(f"Screenshots/highlighted cost.png")
    # img.show()

    text = pytesseract.image_to_string(img, config='--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789')
    cleaned_text = text.replace("\n", "")

    return cleaned_text

def get_stage():
    # im = pyautogui.screenshot(f"Screenshots/stage screenshot.png", region = (STAGE_POSITIONS[0]))
    # img = Image.open(f"Screenshots/stage screenshot.png")

    im = pyautogui.screenshot(region = (STAGE_POSITIONS[0]))
    img = im

    # Convert to grayscale
    img = ImageOps.grayscale(img)

    # Increase contrast slightly
    img = ImageOps.autocontrast(img)

    # Optional: sharpen edges (helps with small fonts)
    img = img.filter(ImageFilter.SHARPEN)

    # 3) normalize + tame jaggies
    img = img.filter(ImageFilter.GaussianBlur(0.6))

    # # Optional: resize to improve clarity (Tesseract likes bigger text)
    # img = img.resize((img.width * 2, img.height * 2), Image.NEAREST)

    thr = 140
    img = img.point(lambda p: 255 if p > thr else 0)

    img.save(f"Screenshots/stage screenshot preprocessed.png")
    # img.show()

    text = pytesseract.image_to_string(img, config='--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789')
    cleaned_text = text.replace("\n", "")

    if cleaned_text != "":
        return cleaned_text
    else:
        # im = pyautogui.screenshot(f"Screenshots/stage screenshot.png", region=(STAGE_POSITIONS[1]))
        # img = Image.open(f"Screenshots/stage screenshot.png")

        im = pyautogui.screenshot(region=(STAGE_POSITIONS[1]))
        img = im

        # Convert to grayscale
        img = ImageOps.grayscale(img)

        # Increase contrast slightly
        img = ImageOps.autocontrast(img)

        # Optional: sharpen edges (helps with small fonts)
        img = img.filter(ImageFilter.SHARPEN)

        # 3) normalize + tame jaggies
        img = img.filter(ImageFilter.GaussianBlur(0.6))

        # # Optional: resize to improve clarity (Tesseract likes bigger text)
        # img = img.resize((img.width * 2, img.height * 2), Image.NEAREST)

        thr = 120
        img = img.point(lambda p: 255 if p > thr else 0)

        img.save(f"Screenshots/stage screenshot preprocessed.png")
        # img.show()

        text = pytesseract.image_to_string(img, config='--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789')
        cleaned_text = text.replace("\n", "")

        return cleaned_text

def get_gold():
    cleaned_text = ''
    # for i in range(1):
    while cleaned_text == '':
        # im = pyautogui.screenshot(f"Screenshots/gold screenshot.png", region=(GOLD_POSITIONS[0]))
        # img = Image.open(f"Screenshots/gold screenshot.png")

        im = pyautogui.screenshot(region=(GOLD_POSITIONS[0]))
        img = im

        # Convert to grayscale
        img = ImageOps.grayscale(img)

        # Increase contrast slightly

        img = ImageOps.autocontrast(img)

        # Optional: sharpen edges (helps with small fonts)
        img = img.filter(ImageFilter.SHARPEN)

        # Optional: resize to improve clarity (Tesseract likes bigger text)
        # img = img.resize((img.width * 5, img.height * 5), Image.NEAREST)

        thr = 120
        img = img.point(lambda p: 255 if p > thr else 0)

        # Optional: subset to gold value
        text = pytesseract.image_to_string(img, config='--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789')
        img.save("Screenshots/gold preprocessed.png")
        cleaned_text = text.replace("\n", "")
    return int(cleaned_text)

def find_target_pixels_on_board():
    TARGET_COLOR_BLUE = (47, 245, 255)        # your sampled blue (R, G, B)
    TARGET_COLOR_GRAY = (230,230, 230)
    TARGET_COLOR_GOLD = (230, 230, 65)

    # im = pyautogui.screenshot(f"Screenshots/Board Screenshot.png", region=(PLAYER_BOARD_POSITIONS[0]))
    # img = Image.open(f"Screenshots/Board Screenshot.png")

    im = pyautogui.screenshot( region=(PLAYER_BOARD_POSITIONS[0]))
    img = im

    # Convert to numpy array (H, W, 3)
    img = np.array(img)[:, :, :3].astype(np.int16)

    # Compute per-pixel color distance to target
    target_blue = np.array(TARGET_COLOR_BLUE, dtype=np.int16)
    target_grey = np.array(TARGET_COLOR_GRAY, dtype=np.int16)
    target_gold = np.array(TARGET_COLOR_GOLD, dtype=np.int16)
    diff_blue = np.linalg.norm(img - target_blue, axis=2)
    diff_grey = np.linalg.norm(img - target_grey, axis=2)
    diff_gold = np.linalg.norm(img - target_gold, axis=2)

    # Mask of "close enough to target blue"
    mask_blue = diff_blue < 30
    mask_grey = diff_grey < 30
    mask_gold = diff_gold < 75

    ysb, xsb = np.where(mask_blue)
    ysg, xsg = np.where(mask_grey)
    yso, xso = np.where(mask_gold)
    if len(xsb) + len(xsg) + len(xso) == 0:
        return []  # no match

    # Convert local coords -> absolute screen coords
    positions = [(int(x), int(y)) for x, y in zip(np.concatenate([xsb, xsg, xso]),np.concatenate([ysb, ysg, yso]))]
    clean_positions = [positions[0]]
    for x, y in positions:
        too_close = False
        for cx, cy in clean_positions:
            if ( (x - cx)**2 + (y - cy)**2 )**0.5 < 100:
                too_close = True
                break
        if not too_close:
            clean_positions.append((x, y))
    # clean_positions = [
    #     (x, y)
    #     for x, y in clean_positions
    #     if not (20 <= x <= 450 and 65 <= y <= 170)
    # ]
    # clean_positions.append((70, 115))
    # clean_positions.append((420, 115))
    return clean_positions

def find_gold():
    TARGET_COLOR_GOLD = (230, 230, 65)

    # im = pyautogui.screenshot(f"Screenshots/Board Screenshot.png", region=(PLAYER_BOARD_POSITIONS[0]))
    # img = Image.open(f"Screenshots/Board Screenshot.png")

    im = pyautogui.screenshot(region=(PLAYER_BOARD_POSITIONS[0]))
    img = im

    # Convert to numpy array (H, W, 3)
    img = np.array(img)[:, :, :3].astype(np.int16)

    # Compute per-pixel color distance to target
    target_gold = np.array(TARGET_COLOR_GOLD, dtype=np.int16)
    diff_gold = np.linalg.norm(img - target_gold, axis=2)

    # Mask of "close enough to target blue"
    mask_gold = diff_gold < 75

    yso, xso = np.where(mask_gold)
    if len(xso) == 0:
        return []  # no match

    # Convert local coords -> absolute screen coords
    positions = [(int(x), int(y)) for x, y in zip(np.concatenate([xso]),np.concatenate([yso]))]
    clean_positions = [positions[0]]
    for x, y in positions:
        too_close = False
        for cx, cy in clean_positions:
            if ( (x - cx)**2 + (y - cy)**2 )**0.5 < 100:
                too_close = True
                break
        if not too_close:
            clean_positions.append((x, y))
    clean_positions = [
        (x, y)
        for x, y in clean_positions
        if not (30 <= x <= 450 and 65 <= y <= 165)
    ]
    return clean_positions

def get_item_bench():
    items = [None] * 10
    for i in range(10):
        pyautogui.moveTo(ITEM_POSITIONS_MOUSE[i])
        # im = pyautogui.screenshot(f"Screenshots/Item Screenshots/item screenshot{i}.png", region=(ITEM_POSITIONS[i]))
        # img = Image.open(f"Screenshots/Item Screenshots/item screenshot{i}.png")

        im = pyautogui.screenshot(region=(ITEM_POSITIONS[i]))
        img = im

        # Convert to grayscale
        img = ImageOps.grayscale(img)

        # Increase contrast slightly
        img = ImageOps.autocontrast(img)

        # Optional: resize to improve clarity (Tesseract likes bigger text)
        img = img.resize((img.width * 15, img.height * 15))

        # Optional: sharpen edges (helps with small fonts)
        img = img.filter(ImageFilter.SHARPEN)

        thr = 160
        img = img.point(lambda p: 255 if p > thr else 0)

        config = (
            "-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'. "
        )
        text = pytesseract.image_to_string(img, config = config)
        cleaned_text = text.replace("\n", "")
        length = len(cleaned_text)
        if length > 0:
            for j in range(length):
                if cleaned_text[:length - j] in BASE_ITEMS:
                    items[i] = (cleaned_text[:length - j])
                    break
        if cleaned_text == '':
            break
    return items

def get_unit_bench():
    units = [None] * 9
    for i in range(len(BENCH_POSITIONS)):
        pyautogui.moveTo(BENCH_POSITIONS[i][0], BENCH_POSITIONS[i][1])
        pyautogui.rightClick()
        pyautogui.mouseUp(button='right')
        pdi.press('s')
        unit = get_highlighted_unit()
        print(unit)
        unit_cost = get_highlighted_cost()
        print(unit_cost)
        if unit is not None:
            if unit_cost != '':
                if int(unit_cost) > unit.get_cost():
                    print('here')
                    unit.set_level(2)
            print(unit)
            units[i] = unit.__copy__()
        else:
            # im = pyautogui.screenshot(f"Screenshots/Item Screenshots/anvil.png", region=(BENCH_POSITIONS[i][0] + 75, BENCH_POSITIONS[i][1], 175, 40))
            # img = Image.open(f"Screenshots/Item Screenshots/anvil.png")

            im = pyautogui.screenshot(region=(BENCH_POSITIONS[i][0] + 75, BENCH_POSITIONS[i][1], 175, 40))
            img = im
            # Convert to grayscale
            img = ImageOps.grayscale(img)

            # Increase contrast slightly
            img = ImageOps.autocontrast(img)

            # Optional: resize to improve clarity (Tesseract likes bigger text)
            img = img.resize((img.width * 15, img.height * 15))

            # Optional: sharpen edges (helps with small fonts)
            img = img.filter(ImageFilter.SHARPEN)

            thr = 175
            img = img.point(lambda p: 255 if p > thr else 0)

            config = (
                "-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'. "
            )
            text = pytesseract.image_to_string(img, config=config)
            cleaned_text = text.replace("\n", "")
            print(cleaned_text)
            if cleaned_text == 'ComponentAnvil':
                units[i] = 'ComponentAnvil'
        pyautogui.mouseUp(button='right')
    return units

def get_unit_bench_n_slots(n : int):
    units = [None] * 9
    for i in range(n):
        pyautogui.moveTo(BENCH_POSITIONS[i][0], BENCH_POSITIONS[i][1])
        pyautogui.rightClick()
        pyautogui.mouseUp(button='right')
        pdi.press('s')
        unit = get_highlighted_unit()
        unit_cost = get_highlighted_cost()
        if unit is not None:
            if unit_cost != '':
                print(unit_cost)
                if int(unit_cost) > unit.get_cost():
                    unit.set_level(2)
            units[i] = unit.__copy__()
        else:
            # im = pyautogui.screenshot(f"Screenshots/Item Screenshots/anvil.png", region=(BENCH_POSITIONS[i][0] + 75, BENCH_POSITIONS[i][1], 175, 40))
            # img = Image.open(f"Screenshots/Item Screenshots/anvil.png")

            im = pyautogui.screenshot(region=(BENCH_POSITIONS[i][0] + 75, BENCH_POSITIONS[i][1], 175, 40))
            img = im
            # Convert to grayscale
            img = ImageOps.grayscale(img)

            # Increase contrast slightly
            img = ImageOps.autocontrast(img)

            # Optional: resize to improve clarity (Tesseract likes bigger text)
            img = img.resize((img.width * 15, img.height * 15))

            # Optional: sharpen edges (helps with small fonts)
            img = img.filter(ImageFilter.SHARPEN)

            thr = 175
            img = img.point(lambda p: 255 if p > thr else 0)

            config = (
                "-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'. "
            )
            text = pytesseract.image_to_string(img, config=config)
            cleaned_text = text.replace("\n", "")
            print(cleaned_text)
            if cleaned_text == 'ComponentAnvil':
                units[i] = 'ComponentAnvil'
        pyautogui.mouseUp(button='right')
    return units

def get_unit_bench_until_none():
    units = [None] * 9
    for i in range(len(BENCH_POSITIONS)):
        pyautogui.moveTo(BENCH_POSITIONS[i][0], BENCH_POSITIONS[i][1])
        print('here')
        pyautogui.rightClick()
        pyautogui.mouseUp(button='right')
        pdi.press('s')
        unit = get_highlighted_unit()
        unit_cost = get_highlighted_cost()
        if unit is not None:
            if unit_cost != '':
                print(unit_cost)
                if int(unit_cost) > unit.get_cost():
                    unit.set_level(2)
            units[i] = unit.__copy__()

        else:
            # im = pyautogui.screenshot(f"Screenshots/Item Screenshots/anvil.png", region=(BENCH_POSITIONS[i][0] + 75, BENCH_POSITIONS[i][1], 175, 40))
            # img = Image.open(f"Screenshots/Item Screenshots/anvil.png")

            im = pyautogui.screenshot(region=(BENCH_POSITIONS[i][0] + 75, BENCH_POSITIONS[i][1], 175, 40))
            img = im
            # Convert to grayscale
            img = ImageOps.grayscale(img)

            # Increase contrast slightly
            img = ImageOps.autocontrast(img)

            # Optional: resize to improve clarity (Tesseract likes bigger text)
            img = img.resize((img.width * 15, img.height * 15))

            # Optional: sharpen edges (helps with small fonts)
            img = img.filter(ImageFilter.SHARPEN)

            thr = 175
            img = img.point(lambda p: 255 if p > thr else 0)

            config = (
                "-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'. "
            )
            text = pytesseract.image_to_string(img, config=config)
            cleaned_text = text.replace("\n", "")
            print(cleaned_text)
            if cleaned_text == 'ComponentAnvil':
                units[i] = 'ComponentAnvil'
        if units[i] is None:
            print('here')
            break
        pyautogui.mouseUp(button='right')
    return units


def get_augment_names():
    aug_names = [None] * 3
    for i in range(3):
        pyautogui.moveTo(ITEM_POSITIONS_MOUSE[i])
        im = pyautogui.screenshot(f"Screenshots/Item Screenshots/augment screenshot{i}.png", region=(AUGMENT_POSITIONS[i]))
        img = Image.open(f"Screenshots/Item Screenshots/augment screenshot{i}.png")

        # Convert to grayscale
        img = ImageOps.grayscale(img)

        # Increase contrast slightly
        img = ImageOps.autocontrast(img)

        # Optional: resize to improve clarity (Tesseract likes bigger text)
        img = img.resize((img.width * 15, img.height * 15))

        # Optional: sharpen edges (helps with small fonts)
        img = img.filter(ImageFilter.SHARPEN)

        thr = 165
        img = img.point(lambda p: 255 if p > thr else 0)

        config = (
            "-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'. "
        )

        text = pytesseract.image_to_string(img, config = config)
        cleaned_text = text.replace("\n", "")
        length = len(cleaned_text)
        aug_names[i] = (cleaned_text)
        # if length > 0:
        #     for j in range(length):
        #         print(cleaned_text[:length - j])
        #         if cleaned_text[:length - j] in BASE_ITEMS:
        #             items[i] = (cleaned_text[:length - j])
        #             break
    return aug_names


