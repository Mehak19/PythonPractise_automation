import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

# Assingment:

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
# mosehover
actions = ActionChains(driver)
actions.move_to_element(driver.find_element_by_xpath('''//span[.="Electronics"]''')).click().perform()

# select Samsung S10 Lite
driver.find_element_by_xpath('''//a[.="Samsung S10 Lite"]''').click()
# verify Samsung S10 Lite page
time.sleep(3)
samsungLite_page = driver.title
assert 'Samsung S10 lite - Buy Samsung S10 lite Online at Low Prices In India | Flipkart.com' == samsungLite_page, print(
    "unable to validate Clock page")
print("Verified page expected title :", samsungLite_page)
# close the browser
driver.close()
