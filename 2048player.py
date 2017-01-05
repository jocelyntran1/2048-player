import pyautogui
import time 
 
def play2048(keys_combination):
    pyautogui.hotkey('winleft', '4');
    time.sleep(3);
    pyautogui.hotkey('ctrl', 't')
    pyautogui.typewrite('https://gabrielecirulli.github.io/2048/', interval = 0.2);
    pyautogui.press('enter')
    time.sleep(3)
    while True:
        for key in keys_combination:
            pyautogui.press(key)
            time.sleep(0.3)
play2048(['up', 'left', 'down', 'right'])
