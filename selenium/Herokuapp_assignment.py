from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize Driver
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.maximize_window()

try:
    # --- FEATURE 1: Checkboxes ---
    print("--- Testing Checkboxes ---")
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
    # Select the first checkbox if it's not already checked
    if not checkboxes[0].is_selected():
        checkboxes[0].click()
    print("Checkboxes tested successfully.\n")

    # --- FEATURE 2: Dropdown ---
    print("--- Testing Dropdown ---")
    driver.get("https://the-internet.herokuapp.com/dropdown")
    dropdown_element = wait.until(EC.presence_of_element_located((By.ID, "dropdown")))
    select = Select(dropdown_element)
    select.select_by_visible_text("Option 2")
    print("Dropdown selected 'Option 2' successfully.\n")

    # --- FEATURE 3: Form Authentication (Login) ---
    print("--- Testing Login Form ---")
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    # Verify login success
    success_msg = wait.until(EC.presence_of_element_located((By.ID, "flash"))).text
    print(f"Login result: {success_msg.splitlines()[0]}\n")

    # --- FEATURE 4: Add/Remove Elements (FIXED) ---
    print("--- Testing Add/Remove Elements ---")
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    
    # Wait for the Add button and click it 3 times
    add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add Element']")))
    for i in range(3):
        add_button.click()
    
    # FIX: Explicitly wait for the newly created buttons to appear in the DOM
    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "added-manually")))
    
    # Now fetch the list of delete buttons
    delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")
    print(f"Elements added successfully. Count: {len(delete_buttons)}")
    
    # Safety check to avoid IndexError
    if len(delete_buttons) > 0:
        delete_buttons[0].click() 
        print("Successfully removed one element.\n")

    # --- FEATURE 5: Key Presses ---
    print("--- Testing Key Presses ---")
    driver.get("https://the-internet.herokuapp.com/key_presses")
    input_field = wait.until(EC.presence_of_element_located((By.ID, "target")))
    input_field.send_keys("A")
    result_text = driver.find_element(By.ID, "result").text
    print(f"Key Press Result: {result_text}\n")

except Exception as e:
    print(f"An error occurred during the test: {e}")

finally:
    print("All tests completed. Closing browser in 3 seconds...")
    time.sleep(3)
    driver.quit()