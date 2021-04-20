import pyautogui
from time import sleep


pyautogui.click(1700,1005) #moves the cursor and clicks to any location on the screem

def write(n):
    for i in range(n):
        pyautogui.write('boo')   # writes text into chat
        pyautogui.press('enter') # enter to send to chat
        sleep(2)

write(69)

