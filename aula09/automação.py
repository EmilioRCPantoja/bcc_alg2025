import time
import pyautogui
import keyboard

"""pyautogui.press("win")
pyautogui.sleep(1)
pyautogui.write("firefox")
pyautogui.sleep(2)"""
confirm = pyautogui.confirm(text='aperta', title='vai', buttons=['OK', 'Cancel'])

print(confirm)
