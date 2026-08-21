import os

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.maximize_window()

wait = WebDriverWait(driver,10)

path = "file:///" + os.path.abspath("originalpage.html").replace("\\","/")

driver.get(path)

original_window = driver.current_window_handle

driver.find_element(By.ID,"viewButton").click()

for window in driver.window_handles:

    if window != original_window:

        driver.switch_to.window(window)

        break

try:

    wait.until(
        EC.invisibility_of_element_located((By.ID,"spinner"))
    )

    product = wait.until(
        EC.visibility_of_element_located((By.ID,"productName"))
    ).text

    price = driver.find_element(By.ID,"price").text

    rating = driver.find_element(By.ID,"rating").text

    print("Product Name :",product)

    print("Price :",price)

    print("Rating :",rating)

except Exception:

    print("Element Not Found")

    driver.save_screenshot("error.png")

    print("Screenshot Saved as error.png")

driver.close()

driver.switch_to.window(original_window)

print("Returned to Original Window")

input("Press Enter to Exit...")

driver.quit()