import pyautogui
import pydirectinput as pdi
from positions import SHOP_POSITIONS, PLAYER_BOARD_POSITIONS
from computervision import get_shop, get_gold
from player import Player
from unit import Unit
from typing import Optional, List


def roll_down(p : Player, current_shop : list[Optional[Unit]], target_units : list[str], econ : int):
    while p.show_gold() > 0:
        pyautogui.moveTo(10,10)
        pyautogui.click()
        pyautogui.mouseUp()
        for i in range(len(current_shop)):
            if current_shop[i] is not None:
                pyautogui.moveTo(SHOP_POSITIONS[i][0],SHOP_POSITIONS[i][1])
                pyautogui.sleep(.5)
                if current_shop[i].get_name() in target_units:
                    pyautogui.sleep(1)
                    p.purchase_champ(i)
                    pyautogui.mouseUp()
                    pyautogui.click()
                    pyautogui.mouseUp()
        if p.show_gold() > econ:
            if p.roll_shop() is None:
                pdi.keyDown('d')
                pdi.keyUp('d')
                p._load_shop(get_shop())
            else:
                break
        else:
            break
        p._load_shop(get_shop())
        p._set_gold(get_gold())

def collect_orbs(locations : list[(int,int)]):
    for location in locations:
        print((location[0] - 45) ** 2 + (location[1] - 230) ** 2)
        if ((location[0] - 45) ** 2 + (location[1] - 230) ** 2) ** 0.5 < 100:
            continue
        pyautogui.moveTo(location[0] + PLAYER_BOARD_POSITIONS[0][0],location[1] + PLAYER_BOARD_POSITIONS[0][1])
        pyautogui.rightClick()
        pyautogui.sleep(2)
        pyautogui.moveTo(location[0] + PLAYER_BOARD_POSITIONS[0][0] - 100,location[1] + PLAYER_BOARD_POSITIONS[0][1])
        pyautogui.rightClick()
        pyautogui.sleep(.2)
        pyautogui.moveTo(location[0] + PLAYER_BOARD_POSITIONS[0][0],location[1] + PLAYER_BOARD_POSITIONS[0][1] - 100)
        pyautogui.rightClick()
        pyautogui.sleep(.2)
        pyautogui.moveTo(location[0] + PLAYER_BOARD_POSITIONS[0][0] + 100,location[1] + PLAYER_BOARD_POSITIONS[0][1])
        pyautogui.rightClick()
        pyautogui.sleep(.2)
        pyautogui.moveTo(location[0] + PLAYER_BOARD_POSITIONS[0][0],location[1] + PLAYER_BOARD_POSITIONS[0][1] + 100)
        pyautogui.rightClick()
        pyautogui.sleep(.2)
    pyautogui.mouseUp(button = 'right')


