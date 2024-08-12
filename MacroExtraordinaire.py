"""
Run these before running with python 3

pip install pydirectinput
pip3 install pyautogui
pip install pyscreeze
pip install pymsbox
pip install opencv-python
pip install pillow
"""

import pydirectinput
import sys
import time
import pyautogui
import pyscreeze
from pymsgbox import *
import hashlib

pyautogui.FAILSAFE = True

def user():
    loop = True
    while loop == True:
        user = pyautogui.prompt(text="Enter your account name:", title="Login").lower()
        if user == "alex" or user == "lincoln":
            loop = False
        else:
            pyautogui.alert(text='Not a registered user', title='Alert', button='OK')
            continue

def password():
    loop = True
    while loop == True:
        password = pyautogui.password(text='Enter password to continue:', title='Password', default='', mask='*').lower()
        dataBase_password = password
        hashed = hashlib.md5(dataBase_password.encode())
        hexed = (hashed.hexdigest())
        if hexed == "7de12fd49e239636d0d88fc819959def":
            loop = False
        else:
            pyautogui.alert(text='Incorrect password', title='Alert', button='OK')
            continue
    
def start_game():
    loop = True
    while loop == True:
        game = pyautogui.prompt(text="Current options: Elden ring", title="Enter game you are playing today: ").lower()
        if game == "elden ring":
            loop = False
        else:
            pyautogui.alert(text='Not valid game', title='Alert', button='OK')
            continue
    size = pyautogui.size()
    x = size[0]
    y = size[1]
    if game == "elden ring":
        windows_key = pyautogui.locateCenterOnScreen("windows_key.png", confidence=.85)
        pyautogui.click(windows_key)
        pyautogui.typewrite("Steam")
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.click(x/13.68, y/30)
        time.sleep(1)
        pyautogui.tripleClick(x/25.6, y/8)
        pyautogui.typewrite(game)
        pyautogui.doubleClick(x/42.66, y/6)
        pyautogui.moveTo(x/2, y/2)
        time.sleep(45)
        pydirectinput.click()
        time.sleep(10)
        pydirectinput.press('e', presses=5, interval=3)
    return game 

def game_macro(game):
    if game == "elden ring":
        time.sleep(10)
        pydirectinput.press('m')
        time.sleep(2)
        try:
            show_ground = pyautogui.locateCenterOnScreen("show_ground.png", confidence=.6)
        except:
            pydirectinput.press('y')
            pydirectinput.keyDown('a')
            pydirectinput.keyUp('a')
        pydirectinput.keyDown("s")
        pydirectinput.keyDown("d")
        time.sleep(120)
        pydirectinput.keyUp("s")
        pydirectinput.keyUp("d")
        time.sleep(6)
        pydirectinput.keyDown("w")
        time.sleep(11.85)
        pydirectinput.keyUp("w")
        pydirectinput.keyDown("a")
        time.sleep(19.85)
        pydirectinput.keyUp("a")
        pydirectinput.press("e", presses=2, interval=2)
        i = 0
        while True:
            time.sleep(3.5)
            pydirectinput.keyDown("a")
            time.sleep(1.25)
            pydirectinput.keyUp("a")
            pydirectinput.moveRel(-2135, 435, relative=True)
            pydirectinput.mouseDown(button="right")
            time.sleep(1)
            if i < 699:
                pydirectinput.mouseDown(button="left")
                time.sleep(.5)
                pydirectinput.mouseUp(button="left")
            elif i > 698 and i < 1399:
                pydirectinput.mouseDown(button="right")
                pydirectinput.keyDown("o")
                time.sleep(1)
                pydirectinput.keyUp("o")
                pydirectinput.mouseUp(button="right")
            elif i > 1398:
                sys.exit(pyautogui.alert(title='Alert', text='Program Completed', button='OK'))
            time.sleep(1)
            pydirectinput.mouseUp(button="right")
            time.sleep(7)
            pydirectinput.press('m')
            time.sleep(2)
            pydirectinput.press('d')
            pydirectinput.press('e', presses=2, interval=1)
            i += 1
    else:
        pass

user()
password()
game = start_game()
game_macro(game)
