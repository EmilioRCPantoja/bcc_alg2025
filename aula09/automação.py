import pyautogui
import keyboard

confirm = pyautogui.confirm(text='clica ok', title='vai clica', buttons=['OK', 'Cancel'])

if confirm == "OK":
    pyautogui.sleep(5)
    pyautogui.press("win", 1 , 5)
    pyautogui.write("firefox",0.4)
    pyautogui.press("enter")
    pyautogui.sleep(5)
    pyautogui.write("youtube.com/@viniccius13",0.5)
    pyautogui.press("enter")
    pyautogui.sleep(20)
    pyautogui.press("tab", 72, 0.5)
    pyautogui.press("enter")
else:
    pyautogui.sleep(5)
    pyautogui.press("win",1, 5)
    pyautogui.write("firefox",0.4)
    pyautogui.sleep(3)
    pyautogui.press("enter")
    pyautogui.sleep(5)
    pyautogui.write("https://www.youtube.com/watch?v=6Coux33LrJc", 0.4)
    pyautogui.press("enter")



