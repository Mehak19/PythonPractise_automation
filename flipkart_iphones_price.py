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
# title of Homepage
actual_title = driver.title
# validate title of HomePage
assert actual_title == 'Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!', print(
    "-------->test case failed: unable to validate title of home page")
print("Title of Homepage ------>", actual_title, "--------->test case passed")
# handle html popup
driver.find_element(By.XPATH, '''//button[.="✕"]''').click()
# search iphone product
driver.find_element(By.XPATH, "//input[@name='q']").send_keys(("iphone") + Keys.ENTER)
# verify iphone page
time.sleep(3)
iphone_page = driver.title
assert 'Iphone' in iphone_page, print("unable to validate iphone page")
# capture the prices
prices = driver.find_elements_by_xpath('''//div[@class='_3liAhj']/a[3]/div/div[1]''')
print(len(prices))
for price in prices:
    print(price.get_attribute("textContent"))
driver.quit()
