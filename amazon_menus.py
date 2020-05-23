import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

# Assingment:
# Scenario 3:
# •	launch browser
# •	navigate to amazon website
# •	go to the menu,print all the menus


# launch the browser
driver = webdriver.Chrome(ChromeDriverManager().install())

# navigate to url
driver.get("https://www.amazon.in/")

# handle synchronization issues with implicit wait
driver.implicitly_wait(20)

# maximize the window
driver.maximize_window()

# title of Homepage
actual_title = driver.title

# validate title of HomePage
assert actual_title == 'Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in', print(
    "-------->test case failed: unable to validate title of home page")
print("Title of Homepage ------>", actual_title, "--------->test case passed")

# Printing the menus on home Page
menus = driver.find_elements_by_xpath('//div[@id="nav-xshop-container"]/descendant::a')
print('\nMenu listed in amazon are:')
for menu in menus:
    print("{}".format(menu.text))

# close the browser
driver.close()
