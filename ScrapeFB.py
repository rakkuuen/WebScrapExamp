from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import itertools
import json

# Initialize the Chrome driver
driver = webdriver.Chrome()

try:
    # Open the Facebook login page
    driver.get("https://www.facebook.com/")

    # Get email and password from user and attepmt login until successful
    validAccount = False
    while not validAccount:
        email = input("Enter your email: ")
        password = input("Enter password: ")

        # Wait until the email input field is visible (explicit wait)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'email')))
        email_input = driver.find_element(By.NAME, 'email')
        print("Email input field found.")

        # Enter email
        email_input.send_keys(email)
        # Wait for the password input field
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'pass')))
        password_input = driver.find_element(By.NAME, 'pass')
        print("Password input field found.")

        # Enter password
        password_input.send_keys(password)
        # Wait for the login button to be clickable and click it
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        ).click()
        print("Login button found.")
        
        # if the account is valid and it logs in then set valid account to true and leave while
        current_url = driver.current_url
        if "login/?privacy_mutation_token" in current_url:
            print("Login failed, Try again")
            driver.back()
            time.sleep(5)
            email_input = driver.find_element(By.NAME, 'email')
            email_input.clear()
        else:
            validAccount = True
            print("Login successful!")

    # Wait for 10 seconds as a general pause
    time.sleep(10)
    print("Successfully logged in and profile page loaded.")

    # Here I want to go to the friends tab and save every friend name to a json folder
    name_list = []


    # Keep the browser open to observe
    input("Scraping done. Converted to json. Press enter to exit")


except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Pass, keeping the browser open for now
    pass