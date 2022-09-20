from dbm import dumb
import pyautogui, time

time.sleep(5)
pyautogui.moveTo(1096, 1056)

pyautogui.leftClick(x = 1096, y = 1056)
time.sleep(10)

pyautogui.moveTo(1287, 448)
pyautogui.leftClick(x = 1287, y = 448)
time.sleep(10)

pyautogui.typewrite("https://schoolworkspro.com/sign-in")
time.sleep(3)
pyautogui.press("enter")
time.sleep(10)

pyautogui.moveTo(692, 453)
pyautogui.leftClick(x = 692, y = 453)
time.sleep(3)
pyautogui.typewrite("210121")
time.sleep(3)

pyautogui.moveTo(680, 577)
pyautogui.leftClick(x = 680, y = 577)
pyautogui.typewrite("abcdefghijkl")
time.sleep(10)

pyautogui.moveTo(693, 647)
pyautogui.leftClick(x = 693, y = 647)
time.sleep(10)


