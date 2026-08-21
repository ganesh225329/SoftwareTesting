import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.maximize_window()

path = "file:///" + os.path.abspath("products.html").replace("\\","/")

driver.get(path)

wait = WebDriverWait(driver,10)

rows = driver.find_elements(By.XPATH,'//*[@id="productTable"]/tbody/tr')

found=False

for row in rows[1:]:

    cols=row.find_elements(By.TAG_NAME,"td")

    product=cols[0].text

    stock=cols[2].text

    if product=="Wireless Mouse":

        found=True

        print("Product Found :",product)

        if stock=="In Stock":

            print("Stock Status : In Stock")

        else:

            print("Stock Status : Out of Stock")

        cols[3].find_element(By.TAG_NAME,"button").click()

        break

if not found:

    print("Product Not Found")

    driver.quit()
    exit()

wait.until(
    EC.visibility_of_element_located((By.ID,"editForm"))
)

print("Edit Form Loaded")

price=driver.find_element(By.ID,"price")

price.clear()

price.send_keys("29.99")

driver.find_element(By.ID,"saveButton").click()

message=wait.until(
    EC.visibility_of_element_located((By.ID,"message"))
).text

if message=="Product Updated Successfully!":

    print("Price Updated Successfully")
    print("Success Message Verified")

else:

    print("Update Failed")

input("Press Enter to Exit...")

driver.quit()