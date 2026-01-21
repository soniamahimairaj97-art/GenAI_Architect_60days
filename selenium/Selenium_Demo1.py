from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com")
print("web page opened")

# 1. FIXED: Removed quotes from By.ID
element = driver.find_element(By.ID, "content")
print("Element by id")

# 2. FIXED: Removed quotes from By.XPATH and fixed casing
element = driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[1]/a')
print("Elment by Xpath")

# 3. FIXED: Wait requires a TUPLE (double parentheses) and the correct By object
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "content")))
print("Locator by Id")

# 4. FIXED: method is 'send_keys' (underscore) and 'click' works on buttons/links
element.click() 
print("Click action")
# Note: You cannot send_keys to the "content" div. 
# You would need an input field like:
# driver.find_element(By.NAME, "q").send_keys("Social Eagle")

driver.save_screenshot("selenium_demo.png")
print("screenshot saved")
driver.quit() # Always close the browser at the end



































# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# driver=webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com")
# # driver.back()
# # driver.forward()
# # driver.refresh()

# #Finding Element
# element=driver.find_element('By.ID',"content")
# element=driver.find_element('By.Xpath','//*[@id="content"]/ul/li[1]/a')

# #Wait 
# wait=WebDriverWait(driver,10)
# element=wait.until(EC.presence_of_all_elements_located('By.Id',"content"))

# #interaction
# element.click()
# element.sendkeys('Social Eagle')
# element.clear()

# #screenshot

# driver.save_screenshot("selenium_demo.png")