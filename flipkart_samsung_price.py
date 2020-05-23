import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# launch the browser
driver = webdriver.Chrome(ChromeDriverManager().install())

# navigate to url
driver.get("https://www.flipkart.com/")

# handle synchronization issues with implicit wait
driver.implicitly_wait(40)

# maximize the window
driver.maximize_window()

# handle html popup
driver.find_element(By.XPATH, '''//button[.="✕"]''').click()

# Search samsung product
driver.find_element(By.XPATH, "//input[@name='q']").send_keys(("samsung") + Keys.ENTER)

# verify samsung page
time.sleep(3)
samsung_page = driver.title
assert 'Samsung' in samsung_page, print("unable to validate iphone page")

# capture the prices
prices = driver.find_elements_by_xpath('''//div[@class='_3O0U0u']/div/div/a/div[2]/div[2]/div/div/div[1]''')
print(len(prices))
for price in prices:
    print(price.get_attribute("textContent"))

driver.quit()
