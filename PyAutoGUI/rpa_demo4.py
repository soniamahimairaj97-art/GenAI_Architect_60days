import pyautogui
import time
time.sleep(5)
location =pyautogui.locateOnScreen("windowmini.png",confidence = 0.8)
time.sleep(5)
print(location)
time.sleep(5)
pyautogui.click(pyautogui.center(location))
time.sleep(5)
print(pyautogui.size())
ss=pyautogui.screenshot()
ss.save("DemoSS.png")