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
actions.move_to_element(driver.find_element_by_xpath('''//span[.="Home & Furniture"]''')).click().perform()

# select clock
driver.find_element_by_xpath('''//a[.="Clocks"]''').click()
# verify clock page
time.sleep(3)
clock_page = driver.title
assert 'Clocks' in clock_page, print("unable to validate Clock page")

# slider to 2000 limit

all_options = driver.find_element_by_xpath('''(//select[@class="fPjUPw"])[1]''')
select = Select(all_options)
select.select_by_visible_text("2000")
time.sleep(4)

prices = driver.find_elements_by_xpath(
    '''//div[@id="container"]/div/div[3]/div[2]/div/div[2]/div/div/div/div/a[3]/div[1]/div[1]''')
print(len(prices))
time.sleep(2)
# print([price.get_attribute("textContent") for price in prices])
for price in prices:
    clock_name = price.find_element_by_xpath(
        "parent::div/parent::a/preceding-sibling::div/preceding-sibling::a[1]").get_attribute("text")
    print(clock_name)
    time.sleep(5)
    price_string = price.get_attribute("textContent")
    new_price = price_string[1::].replace(",", "")
    print(new_price)
    assert int(new_price) > 2000, print("not matched")
    print("price validated")
    print("===================================================")

# close the browser
driver.close()
