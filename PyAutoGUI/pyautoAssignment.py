# pyautogui_browser_search.py

import pyautogui
import time
import webbrowser

# Step 1: Open the browser (Chrome in this example)
webbrowser.open("https://www.google.com")
time.sleep(3)  # wait for browser to open
print("step 1")

# Step 2: Type the search query
pyautogui.typewrite("Africa vs Australia score")
pyautogui.press("enter")
time.sleep(3)  # wait for search results
print("step 2")

# Step 3: Move the mouse to the first link and click
# NOTE: You must adjust coordinates based on your screen resolution
# Example coordinates (x=400, y=300) – change these!
pyautogui.moveTo(400, 300, duration=1)
pyautogui.click()
print("step 3")

print("Search completed and first link clicked.")