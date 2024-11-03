from selenium import webdriver
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

USER = "standard_user"
PASSWORD = "secret_sauce"

def main():
    service = Service(ChromeDriverManager().install())
    option = webdriver.ChromeOptions()
    #option.add_argument("--headless")
    option.add_argument("--window-size=1920,1800")
    driver = Chrome(service=service,options=option)
    driver.get("https://www.saucedemo.com/")

    #LOGIN
    driver.find_element(By.ID, "user-name").send_keys(USER)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()
    
    #BUY
    driver.find_element(By.NAME, 'add-to-cart-sauce-labs-bike-light').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[1]/div[3]/a").click()

    #CHECKOUT
    driver.find_element(By.ID,'checkout').click()
    driver.find_element(By.ID, "first-name").send_keys('Name')
    driver.find_element(By.ID, "last-name").send_keys('Last Name')
    driver.find_element(By.ID, "postal-code").send_keys('0000')
    driver.find_element(By.ID, "continue").click()
    driver.find_element(By.ID, "finish").click()
    time.sleep(10)
    driver.quit()
    


if __name__ == "__main__":
    main()
