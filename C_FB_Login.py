# C_FB_Login.py - Handles Facebook login using multiple methods (manual, cookies, email/password)
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Load cookies if available
def load_cookies(driver):
    try:
        with open("data/A_Cookies.json", "r") as file:
            cookies = json.load(file)
            for cookie in cookies:
                driver.add_cookie(cookie)
        print("✅ Cookies loaded successfully!")
        return True
    except Exception as e:
        print("⚠️ No cookies found. Manual login required.")
        return False

# Save cookies after login
def save_cookies(driver):
    with open("data/A_Cookies.json", "w") as file:
        json.dump(driver.get_cookies(), file)
    print("✅ Cookies saved successfully!")

# Facebook login function
def fb_login(method="cookies", email="", password=""):
    driver = webdriver.Firefox()
    driver.get("https://www.facebook.com")

    if method == "cookies":
        if load_cookies(driver):
            driver.refresh()
        else:
            print("⚠️ Login manually and press Enter...")
            input()
            save_cookies(driver)

    elif method == "email":
        email_input = driver.find_element(By.ID, "email")
        password_input = driver.find_element(By.ID, "pass")
        email_input.send_keys(email)
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)
        time.sleep(5)
        save_cookies(driver)

    print("✅ Facebook login successful!")
    return driver

if __name__ == "__main__":
    fb_login(method="cookies")
