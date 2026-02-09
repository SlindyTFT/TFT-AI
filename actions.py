import pyautogui
import pydirectinput as pdi
from positions import SHOP_POSITIONS, PLAYER_BOARD_POSITIONS, CREATE_ITEM_POSITIONS, UNIT_BOARD_POSITION, BENCH_POSITIONS
from computervision import get_shop, get_gold
from player import Player
from unit import Unit
from typing import Optional, List


def roll_down(p : Player, econ: int ):
    while p.show_gold() > 0:
        p._load_shop(get_shop())
        p._set_gold(get_gold())
        pyautogui.moveTo(10,10)
        pyautogui.click()
        pyautogui.mouseUp()
        for i in range(len(p.show_shop())):
            if p.show_shop()[i] is not None:
                if (p.show_shop()[i].get_name() in p.target_units.keys()) and (p.count_of_champ(p.show_shop()[i]) < p.target_units[p.show_shop()[i].get_name()]):
                    pyautogui.moveTo(SHOP_POSITIONS[i][0], SHOP_POSITIONS[i][1])
                    pyautogui.sleep(.05)
                    p.purchase_champ(i)
                    pyautogui.mouseUp()
                    pyautogui.click()
                    pyautogui.mouseUp()
        if p.show_gold() > econ:
            if p.roll_shop() is None:
                pdi.keyDown('d')
                pdi.keyUp('d')
                p._load_shop(get_shop())
                p._set_gold(get_gold())
            else:
                break
        else:
            break

def roll_shop(p : Player, num_rolls: int):
    for i in range(num_rolls):
        p._load_shop(get_shop())
        p._set_gold(get_gold())
        pyautogui.moveTo(10,10)
        pyautogui.click()
        pyautogui.mouseUp()
        for j in range(len(p.show_shop())):
            if p.show_shop()[j] is not None:
                if (p.show_shop()[j].get_name() in p.target_units.keys()) and (p.count_of_champ(p.show_shop()[j]) < p.target_units[p.show_shop()[j].get_name()]):
                    pyautogui.moveTo(SHOP_POSITIONS[j][0], SHOP_POSITIONS[j][1])
                    pyautogui.sleep(.05)
                    p.purchase_champ(j)
                    pyautogui.mouseUp()
                    pyautogui.click()
                    pyautogui.mouseUp()
        if p.show_gold() > 1:
            if p.roll_shop() is None:
                pdi.keyDown('d')
                pdi.keyUp('d')
                p._load_shop(get_shop())
                p._set_gold(get_gold())
            else:
                break
        else:
            break
    for i in range(len(p.show_shop())):
        if p.show_shop()[i] is not None:
            if p.show_shop()[i].get_name() in p.target_units.keys():
                pyautogui.moveTo(SHOP_POSITIONS[i][0], SHOP_POSITIONS[i][1])
                pyautogui.sleep(.5)
                p.purchase_champ(i)
                pyautogui.mouseUp()
                pyautogui.click()
                pyautogui.mouseUp()

def purchase_champ(p : Player, shop_position : int):
    pyautogui.moveTo(SHOP_POSITIONS[shop_position][0], SHOP_POSITIONS[shop_position][1])
    pyautogui.sleep(.05)
    p.purchase_champ(shop_position)
    pyautogui.mouseUp()
    pyautogui.click()
    pyautogui.mouseUp()

def sell_unit(p : Player, board_positions : list[(int,int)]):
    for x, y in board_positions:
        pyautogui.moveTo(UNIT_BOARD_POSITION[x][y])
        pyautogui.sleep(.05)
        pdi.keyDown('e')
        pdi.keyUp('e')
        pyautogui.sleep(.05)


def find_nearest_neighbor(point : (int,int), locations : list[(int,int)]):
    nearest_ind = 0
    nearest_dist = (point[0] - locations[0][0])**2 + (point[1] - locations[0][1])**2
    for i in range(1, len(locations)):
        dist = (point[0] - locations[i][0])**2 + (point[1] - locations[i][1])**2
        if dist < nearest_dist:
            nearest_ind = i
            nearest_dist = dist
    return  nearest_ind

def collect_orbs(locations : list[(int,int)]):
    if len(locations) > 0:
        pyautogui.moveTo(PLAYER_BOARD_POSITIONS[0][0], PLAYER_BOARD_POSITIONS[0][1])
        current_position = locations.pop(0)
        pyautogui.moveTo(current_position[0] + PLAYER_BOARD_POSITIONS[0][0], current_position[1] + PLAYER_BOARD_POSITIONS[0][1])
        pyautogui.rightClick()
        pyautogui.sleep(2)
        while len(locations) > 0:
            nearest_ind = find_nearest_neighbor(current_position, locations)
            nearest_point = locations.pop(nearest_ind)
            pyautogui.moveTo(nearest_point[0] + PLAYER_BOARD_POSITIONS[0][0],nearest_point[1] + PLAYER_BOARD_POSITIONS[0][1])
            pyautogui.rightClick()
            pyautogui.sleep(1)
            current_position = nearest_point
            # pyautogui.moveTo(location[0] + PLAYER_BOARD_POSITIONS[0][0] - 100,location[1] + PLAYER_BOARD_POSITIONS[0][1])
            # pyautogui.rightClick()
            # pyautogui.sleep(.2)
            # pyautogui.moveTo(location[0] + PLAYER_BOARD_POSITIONS[0][0],location[1] + PLAYER_BOARD_POSITIONS[0][1] - 100)
            # pyautogui.rightClick()
            # pyautogui.sleep(.2)
            # pyautogui.moveTo(location[0] + PLAYER_BOARD_POSITIONS[0][0] + 100,location[1] + PLAYER_BOARD_POSITIONS[0][1])
            # pyautogui.rightClick()
            # pyautogui.sleep(.2)
            # pyautogui.moveTo(location[0] + PLAYER_BOARD_POSITIONS[0][0],location[1] + PLAYER_BOARD_POSITIONS[0][1] + 100)
            # pyautogui.rightClick()
            # pyautogui.sleep(.2)
        pyautogui.mouseUp(button = 'right')

def make_item(starting_position : (int, int), item : str):
    pyautogui.moveTo(starting_position[0], starting_position[1])
    pyautogui.click(button = 'left')
    pyautogui.mouseUp(button = 'left')
    pyautogui.sleep(.2)
    pyautogui.click(button = 'right')
    pyautogui.mouseUp(button = 'right')
    pyautogui.moveTo(CREATE_ITEM_POSITIONS[item][1][0])
    pyautogui.sleep(.2)
    pyautogui.moveTo(CREATE_ITEM_POSITIONS[item][1][1])
    pyautogui.sleep(.2)
    pyautogui.moveTo(CREATE_ITEM_POSITIONS[item][1][2])
    # pyautogui.doubleClick(button='left')
    pyautogui.mouseUp()
    return CREATE_ITEM_POSITIONS[item][0]

def move_item_to_unit(item_position : (int, int), unit_position : (int, int)):
    pyautogui.moveTo(item_position[0], item_position[1])
    pyautogui.click(button = 'left')
    pyautogui.mouseDown(button = 'left')
    pyautogui.sleep(.05)
    pyautogui.moveTo(unit_position[0], unit_position[1] - 10)
    pyautogui.sleep(.05)
    pyautogui.mouseUp(button = 'left')
    pyautogui.mouseUp(button = 'left')

def move_unit_to_pos(unit_position, position):
    if type(unit_position) is int and type(position) is tuple:
        x1, y1 = BENCH_POSITIONS[unit_position]
        pyautogui.moveTo(x1, y1)
        pyautogui.sleep(.05)
        pyautogui.doubleClick(button = 'left')
        pyautogui.mouseDown(button = 'left')
        x2, y2 = UNIT_BOARD_POSITION[position[0]][position[1]]
        pyautogui.moveTo(x2, y2)
        pyautogui.sleep(.05)
        pyautogui.mouseUp(button = 'left')
        pyautogui.mouseUp(button = 'left')
    elif type(unit_position) is tuple and type(position) is tuple:
        x1, y1 = UNIT_BOARD_POSITION[unit_position[0]][unit_position[1]]
        pyautogui.moveTo(x1, y1)
        pyautogui.sleep(.05)
        pyautogui.doubleClick(button='left')
        pyautogui.mouseDown(button='left')
        x2, y2 = UNIT_BOARD_POSITION[position[0]][position[1]]
        pyautogui.moveTo(x2, y2)
        pyautogui.sleep(.05)
        pyautogui.mouseUp(button='left')
    elif type(unit_position) is int and type(position) is int:
        x1, y1 = BENCH_POSITIONS[unit_position]
        pyautogui.moveTo(x1, y1)
        pyautogui.sleep(.05)
        pyautogui.doubleClick(button='left')
        pyautogui.mouseDown(button='left')
        x2, y2 = BENCH_POSITIONS[position]
        pyautogui.moveTo(x2, y2)
        pyautogui.sleep(.05)
        pyautogui.mouseUp(button='left')
    else:
        x1, y1 = UNIT_BOARD_POSITION[unit_position[0]][unit_position[1]]
        pyautogui.moveTo(x1, y1)
        pyautogui.sleep(.05)
        pyautogui.doubleClick(button='left')
        pyautogui.mouseDown(button='left')
        x2, y2 = BENCH_POSITIONS[position]
        pyautogui.moveTo(x2, y2)
        pyautogui.sleep(.05)
        pyautogui.mouseUp(button='left')



