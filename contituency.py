from driver.driver import Driver
from login.login_contituency import Login
from profiling.profiling import Profiling

driver = Driver().driver
driver.get("http://13.251.162.105/login")
Login().login(driver)

Profiling().profiling(driver)


print(input("End Work:"))
