import pyautogui
import keyboard
import time

pyautogui.press('win')  # Open Start menu
time.sleep(3)
pyautogui.write('firefox', interval=0.2) 
time.sleep(2)
pyautogui.press('enter') 

# Wait for the application to open
time.sleep(5)

pyautogui.write('https://portaldatransparencia.gov.br/servidores', interval=0.2)  
pyautogui.press('enter') 

time.sleep(5)

for i in range(14):
    pyautogui.press('tab', interval=0.1)

pyautogui.write('ALCIONE TALASKA', interval=0.2)             
time.sleep(1)
pyautogui.press('enter')  

time.sleep(10)

# for i in range(77):
for i in range(20):    
    pyautogui.press('tab', interval=0.2)

pyautogui.press('enter')

time.sleep(3)

# for i in range(82):
for i in range(24):    
    pyautogui.press('tab', interval=0.2 )

pyautogui.press('enter')

pyautogui.press('tab', interval=1 )
pyautogui.press('enter')

