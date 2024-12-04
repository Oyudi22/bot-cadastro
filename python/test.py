import pyautogui
from time import sleep

#pyautogui.hotkey('shift', 'end')
pyautogui.click(2801,341,duration=2)
#pyautogui.hotkey()
pyautogui.doubleClick(2801,341,duration=1)
#pyautogui.hotkey('shift', 'End')
pyautogui.hotkey('shift', 'end')
sleep(2)

pyautogui.hotkey('ctrl', 'c')


pyautogui.click(73,278,duration=1)
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'v')

pyautogui.click(3192,719,duration=1)
pyautogui.click(2043,122,duration=1)


