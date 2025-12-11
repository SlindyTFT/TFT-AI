import pyautogui
from PIL import Image, ImageFilter, ImageOps
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
from units import UNIT_DICT
from positions import SHOP_POSITIONS

def get_shop():
    current_shop = [None] * 5
    for i in range(5):
        im = pyautogui.screenshot(f"Screenshots/screenshot{i}.png", region = (SHOP_POSITIONS[i]))
        img = Image.open(f"Screenshots/screenshot{i}.png")
        # Convert to grayscale
        img = ImageOps.grayscale(img)

        # Increase contrast slightly
        img = ImageOps.autocontrast(img)

        # Optional: sharpen edges (helps with small fonts)
        img = img.filter(ImageFilter.SHARPEN)

        # Optional: resize to improve clarity (Tesseract likes bigger text)
        img = img.resize((img.width * 2, img.height * 2))

        text = pytesseract.image_to_string(img)
        cleaned_text = text.replace("\n", "")
        current_shop[i] = UNIT_DICT.get(cleaned_text)
    return current_shop

