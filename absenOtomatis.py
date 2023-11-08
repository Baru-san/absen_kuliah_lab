import time
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Import the Keys module
from selenium.common.exceptions import NoSuchElementException


class User:
    def __init__(self, url, role, lamanAbsen, submitButton,confirmButton):
        self.url = url
        self.role = role
        self.lamanAbsen = lamanAbsen
        self.submitButton = submitButton
        self.confirmButton = confirmButton

home_dir = os.path.expanduser("~")

# Path to the file within the home directory
file_path = os.path.join(home_dir, 'coding/belajar/selenium/pass.txt')

# Read the file
with open(file_path, 'r') as file:
    password = file.read()

def create_siplab():
    url = 'https://fmipa.usk.ac.id/siplab/login'
    role = 'loginsebagai'
    lamanAbsen = "https://fmipa.usk.ac.id/siplab/mahasiswa/kehadiran_praktikum"
    submitButton = 'tombolHadir1'
    confirmButton = None
    return User(url, role, lamanAbsen, submitButton, confirmButton)

def create_simkul():
    url = 'https://simkuliah.usk.ac.id/'
    role = None
    lamanAbsen = 'https://simkuliah.usk.ac.id/index.php/absensi'
    submitButton = 'konfirmasi-kehadiran'
    confirmButton = 'button.confirm'
    return User(url, role, lamanAbsen, submitButton, confirmButton)

def default():
    print("Invalid selection")
    sys.exit(0)

switch = {
    1: create_siplab,
    2: create_simkul
}

# Get user input
choice = int(input("silahkan pilih\n1. Siplab\n2. Simkul\n"))

# Execute the selected case or default
result = switch.get(choice, default)()

# Create a Chrome WebDriver instance
driver = webdriver.Chrome()

driver.get(result.url)

time.sleep(1)  # Let the user actually see something!


if(result.role):
    role_box = driver.find_element(By.NAME, result.role)
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

driver.get(result.lamanAbsen)


try:
    attendace_box = driver.find_element(By.ID, result.submitButton)
    attendace_box.click()
except NoSuchElementException as e:
    print("Element not found:", e)
    # Add your error handling or recovery mechanism here
except Exception as e:
    print("An unexpected error occurred:", e)
    # Add error handling for other exceptions

time.sleep(1)  # Let the user actually see something!

if(result.confirmButton):
    confirm_button= driver.find_element(By.CSS_SELECTOR, result.confirmButton)
    confirm_button.click()

time.sleep(2)  # Let the user actually see something!

driver.quit()
