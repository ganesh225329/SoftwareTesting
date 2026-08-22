import os

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.maximize_window()

path = "file:///" + os.path.abspath("index2.html").replace("\\","/")

driver.get(path)

wait = WebDriverWait(driver,10)

print("="*60)
print("LOADING SPINNER TEST")
print("="*60)

# Click Load Data button
driver.find_element(By.ID,"loadButton").click()

print("Load Data Button Clicked")

# Wait until spinner disappears
wait.until(
    EC.invisibility_of_element_located((By.ID,"spinner"))
)

print("Loading Spinner Disappeared")

# Verify table is visible
table = wait.until(
    EC.visibility_of_element_located((By.ID,"table"))
)

print("Table Displayed Successfully")

# Print Row 1
row = driver.find_element(
    By.XPATH,
    '//*[@id="table"]/tbody/tr[2]'
)

print()

print("First Row Data :")

print(row.text)

print("="*60)

input("Press Enter to Exit...")

driver.quit()