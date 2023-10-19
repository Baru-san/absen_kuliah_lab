import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

with open('pass.txt', 'r') as file:
    password = file.read()

# Specify the path to ChromeDriver as a system property
# chromedriver_path = os.path.expanduser('~/baru_san/coding/belajar/selenium/chromedriver_linux64/chromedriver')
# os.environ["webdriver.chrome.driver"] = chromedriver_path

# Create a Chrome WebDriver instance
driver = webdriver.Chrome()

driver.get('https://simkuliah.usk.ac.id/')

time.sleep(2)  # Let the user actually see something!

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

driver.get('https://simkuliah.usk.ac.id/index.php/absensi')

attendace_box = driver.find_element(By.ID, 'konfirmasi-kehadiran')
attendace_box.click()

time.sleep(2)  # Let the user actually see something!

confirm_button= driver.find_element(By.CSS_SELECTOR, 'button.confirm')
confirm_button.click()


time.sleep(5)  # Let the user actually see something!

driver.quit()
