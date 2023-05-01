import os
from selenium.webdriver.common.by import By

from driver.driver import Driver

from dotenv import load_dotenv

# Load the environment variables
load_dotenv()


class Login:
    def login(self, driver):
        # print(input("Inside class and function :"))
        try:
            # I use environment variable  base on this tutorials https://www.youtube.com/watch?v=IolxqkL7cD8
            FACEBOOK_USERNAME = os.getenv("FACEBOOK_USERNAME", "")
            FACEBOOK_PASSWORD = os.getenv("FACEBOOK_PASSWORD", "")
            # FACEBOOK_USERNAME = os.environ.get('facebook_email')
            # FACEBOOK_PASSWORD = os.environ.get('facebook_pass')
            # print(FACEBOOK_PASSWORD)
            # print(input("...:"))
            driver.find_element(By.NAME, "email").send_keys(FACEBOOK_USERNAME)
            driver.find_element(By.NAME, "pass").send_keys(FACEBOOK_PASSWORD)
            driver.find_element(By.NAME, "login").click()

            print(input("Login work Successfully Press any Key: "))
        except:
            pass


if __name__ == "__main__":
    driver = Driver().driver
    driver.get("https://www.facebook.com/")
    Login().login(driver)
