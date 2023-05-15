import time

from driver.driver import Driver
from login.login import Login
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = Driver().driver
driver.get("https://www.facebook.com/")
Login().login(driver)

filename = 'GroupName.txt'
with open(filename) as file:
    lines = [line.rstrip() for line in file]

for line in lines:
    driver.get(line)
    time.sleep(10)
    print(line)

print(input("End Work:"))
