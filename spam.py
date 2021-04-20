from win32api import GetSystemMetrics
import pyautogui
from time import sleep

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

pyautogui.click(width / 2, height / 2) #moves the cursor and clicks to any location on the screem

def write(n):
    for i in range(n):
        pyautogui.press('tab')
        pyautogui.write('XDbrozos')   # writes text into chat
        pyautogui.press('enter') # enter to send to chat
        sleep(2)

write(69420)

