from selenium import webdriver
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

USER = "standard_user"
PASSWORD = "standard_user"

def main():
    service = Service(ChromeDriverManager().install())
    option = webdriver.ChromeOptions()
    #option.add_argument("--headless")
    option.add_argument("--window-size=1920,1800")
    driver = Chrome(service=service,options=option)
    driver.get("https://www.saucedemo.com/")
    time.sleep(5)
    driver.quit()
    


if __name__ == "__main__":
    main()
