import os
import time

from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys

from driver.driver import Driver

from dotenv import load_dotenv

# Load the environment variables
load_dotenv()


class Profiling:
    def profiling(self, driver):
        driver.get("http://13.251.162.105/profiling")
        driver.implicitly_wait(10)
        # time.sleep(2)
        # print(input("Entering the loop :"))
        j = 30
        for i in range(10):
            print(f"i : {i}")
            print(f"print j + i : {j}")
            driver.implicitly_wait(10)
            time.sleep(2)
            # driver.find_element(By.XPATH, f"(//div)[{(j)+(i)}]").click()
            profile = driver.find_element(By.XPATH, f"(//div)[{j}]")
            print(profile)
            try:
                ActionChains(driver) \
                    .key_down(Keys.CONTROL) \
                    .click(profile) \
                    .key_up(Keys.CONTROL) \
                    .perform()

                print(f"We are in {i} circle.")
                # print(input("....:"))

                driver.implicitly_wait(10)
                time.sleep(2)
                window_before = driver.window_handles[0]
                print(window_before)
                window_after = driver.window_handles[1]
                print(window_after)
                driver.switch_to.window(window_after)

                print(driver.current_url)
                el = driver.page_source
                print(el)

                time.sleep(4)
                driver.close()
                driver.switch_to.window(window_before)

            except:
                print(input("Why this profile is not accessible Investigate:"))

            i += 4
            j = j+i


if __name__ == "__main__":
    driver = Driver().driver
    Profiling().profiling(driver)
