import pyautogui
import pydirectinput as pdi
from positions import SHOP_POSITIONS
from computervision import get_shop
from player import Player
from unit import Unit
from typing import Optional, List


def roll_down(p : Player, current_shop : list[Optional[Unit]], target_units : list[str]):
    while p.show_gold() > 0:
        pyautogui.moveTo(10,10)
        pyautogui.click()
        pyautogui.mouseUp()
        for i in range(len(current_shop)):
            if current_shop[i] is not None:
                pyautogui.moveTo(SHOP_POSITIONS[i][0],SHOP_POSITIONS[i][1])
                pyautogui.sleep(.5)
                if current_shop[i].get_name() in target_units:
                    print('here')
                    print(p.show_gold())
                    print(p.purchase_champ(i))
                    pyautogui.click()
                    pyautogui.mouseUp()
        if p.roll_shop() is None:
            pdi.keyDown('d')
            pdi.keyUp('d')
            p._load_shop(get_shop())
        p._load_shop(get_shop())