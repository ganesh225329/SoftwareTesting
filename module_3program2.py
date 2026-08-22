import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

path = "file:///" + os.path.abspath("index.html").replace("\\","/")

driver.get(path)

print("="*60)
print("WINDOW HANDLING TEST")
print("="*60)

# Store original window
original_window = driver.current_window_handle

print("Original Page Title :", driver.title)

# Click button
driver.find_element(By.ID, "openButton").click()

time.sleep(2)

# Switch to new window
for window in driver.window_handles:

    if window != original_window:

        driver.switch_to.window(window)

        break

print("\nNew Window Title :", driver.title)

# Verify title
if "Dashboard" in driver.title:

    print("✅ Dashboard Page Verified")

else:

    print("❌ Dashboard Verification Failed")

# Close new window
driver.close()

print("\nNew Window Closed")

# Switch back
driver.switch_to.window(original_window)

print("\nBack to Original Window")

print("Original Window Title :", driver.title)

print("="*60)

input("Press Enter to Exit...")

driver.quit()