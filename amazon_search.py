

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager





driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.amazon.in/")
driver.implicitly_wait(20)
driver.maximize_window()


# Printing the menus on home Page
driver.find_element_by_xpath('//input[@id="twotabsearchtextbox"]').send_keys('iphonesXR')

driver.close()
