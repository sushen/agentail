import time

from driver.driver import Driver
from login.login import Login
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = Driver().driver
driver.get("https://www.facebook.com/")
Login().login(driver)

search_query = "binance"

driver.get(f"https://www.facebook.com/search/groups/?q={search_query}")

all_btn_x_path = "(//span[contains(text(),'Visit')])"

visit_buttons = driver.find_elements(By.XPATH, all_btn_x_path)


# print(visit_buttons)
# print(len(visit_buttons))

for visit in range(len(visit_buttons)):
    driver.implicitly_wait(10)
    time.sleep(2)
    print(visit + 1)
    # element = driver.find_elements(By.XPATH, f"// span[contains(text(), 'Visit')])[{int(visit+1)}]")
    element = driver.find_element(By.XPATH, f"(//span[contains(text(),'Visit')])[{visit + 1}]")

    ActionChains(driver) \
        .key_down(Keys.CONTROL) \
        .click(element) \
        .key_up(Keys.CONTROL) \
        .perform()

    driver.implicitly_wait(10)
    time.sleep(4)

    # print(input("Pause:"))
    print(driver.window_handles)

    window_before = driver.window_handles[0]
    window_after = driver.window_handles[1]

    driver.switch_to.window(window_after)

    filename = 'GroupName.txt'

    groupUrlForList = driver.current_url + "\n"
    line_index = 3
    lines = None
    with open(filename, 'r') as file_handler:
        lines = file_handler.readlines()
    lines.insert(line_index, groupUrlForList)
    with open(filename, 'w') as file_handler:
        file_handler.writelines(lines)

    time.sleep(2)
    driver.close()
    driver.switch_to.window(window_before)


print(input("End Work:"))
