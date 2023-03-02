from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options


def cookie_count():
    count = driver.find_element(By.ID, "cookies")
    count = count.text.split(" ")[0].replace(",","")
    return int(count)

def highest_upgrade():
    enabled_options = driver.find_elements(By.CLASS_NAME, "unlocked")
    print([option.find_element(By.CLASS_NAME, "productName").text for option in enabled_options])
    choice = enabled_options[-1]
    choice.click()
    choice_name = choice.find_element(By.CLASS_NAME, "productName")
    print(f"Selected: {choice_name.text}")
    time_mark = time.perf_counter()
    return time_mark

options = Options()
options.add_experimental_option('detach', True)

url='https://orteil.dashnet.org/cookieclicker/'

web_driver = ChromeDriverManager().install()
service = Service(web_driver)
driver = webdriver.Chrome(service=service, options=options)

driver.get(url)
time.sleep(5)
english_button = driver.find_element(By.ID, "langSelect-EN")
english_button.click()
time.sleep(5)
cookie = driver.find_element(By.CSS_SELECTOR, "button#bigCookie")
time_mark = time.perf_counter()
while True:
    cookie.click()
    if time.perf_counter()-time_mark >= 5:
        time_mark = highest_upgrade()

