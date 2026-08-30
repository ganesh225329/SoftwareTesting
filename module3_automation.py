import os

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

path = "file:///" + os.path.abspath("employee.html").replace("\\","/")

driver.get(path)

rows = driver.find_elements(By.XPATH,'//*[@id="employeeTable"]/tbody/tr')

found = False

print("="*60)
print("Searching Employee : John Deo")
print("="*60)

for row in rows[1:]:

    cols = row.find_elements(By.TAG_NAME,"td")

    name = cols[1].text

    if name == "John Deo":

        department = cols[2].text

        salary = cols[3].text

        print("Employee Found")
        print("Department :",department)
        print("Salary :",salary)

        found = True

        break

if not found:

    print("Employee Not Found")

print("="*60)

input("Press Enter to Exit...")

driver.quit()