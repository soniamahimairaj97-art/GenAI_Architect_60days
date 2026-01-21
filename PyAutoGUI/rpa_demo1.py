import pyautogui
import time

# #To find the position of the mouse pointer 
# x,y = pyautogui.position()
# print(f"x: {x}, y : {y}")

#Mouse operations
pyautogui.click(1761,645)
print("click is done")
time.sleep(5)
pyautogui.rightClick(295,151)
print("Right click is done")
time.sleep(5)
pyautogui.doubleClick(86,116)
print("double click is done")
time.sleep(5)
pyautogui.drag(300, 300, duration=2.0)
print("drag is done")
time.sleep(5)
pyautogui.scroll(500)
print("scroll is done")
