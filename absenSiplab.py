import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Import the Keys module


with open('pass.txt', 'r') as file:
    password = file.read()


# Create a Chrome WebDriver instance
driver = webdriver.Chrome()

driver.get('https://fmipa.usk.ac.id/siplab/login')

time.sleep(1)  # Let the user actually see something!

role_box = driver.find_element(By.NAME, 'loginsebagai')
role_box.send_keys(Keys.ARROW_DOWN)

# menacri field username
search_box = driver.find_element(By.NAME, 'username')

# Clear any existing text in the input field
search_box.clear()

# Enter the search query
search_box.send_keys('2108107010044')

pass_box = driver.find_element(By.NAME, 'password')
pass_box.send_keys(password)


# Submit the form
search_box.submit()

driver.get('https://fmipa.usk.ac.id/siplab/mahasiswa/kehadiran_praktikum')

attendace_box = driver.find_element(By.ID, 'tombolHadir1')
attendace_box.click()

time.sleep(2)  # Let the user actually see something!

driver.quit()
