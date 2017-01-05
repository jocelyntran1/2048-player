import pyautogui
import time 
import webbrowser

def play2048(keys_combination):
    webbrowser.open('https://gabrielecirulli.github.io/2048/', new=2) 
    time.sleep(3)
    while True:
        for key in keys_combination:
            pyautogui.press(key)
            time.sleep(0.3)
play2048(['up', 'left', 'down', 'right'])
