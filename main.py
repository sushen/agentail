from driver.driver import Driver
from login.login import Login

driver = Driver().driver
driver.get("https://www.facebook.com/")
Login().login(driver)


print(input("End Work:"))
