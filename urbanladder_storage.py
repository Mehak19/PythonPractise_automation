import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

# Assingment:
# Scenario 2:
# •	launch browser
# •	navigate to urban ladder website
# •	go to the menu,print all the menus
# •	print  the headings or submenus inside storage menu

# launch the browser
driver = webdriver.Chrome(ChromeDriverManager().install())

# navigate to url
driver.get("https://www.urbanladder.com/")

# handle synchronization issues with implicit wait
driver.implicitly_wait(20)

# maximize the window
driver.maximize_window()

# title of Homepage
actual_title = driver.title

# validate title of HomePage
assert actual_title == 'Furniture Online: Buy Home Wooden Furniture Online In India At Best Price - Urban Ladder - Urban Ladder', print(
    "-------->test case failed: unable to validate title of home page")
print("Title of Homepage ------>", actual_title, "--------->test case passed")

# close the window popup
driver.find_element_by_xpath('//a[@class="close-reveal-modal hide-mobile"]').click()

# Printing the menus on home Page
menus = driver.find_elements_by_css_selector('#topnav_wrapper > ul > li')
print('\nMenu listed in urbanladder are:')
for menu in menus:
    print("{}".format(menu.text))

time.sleep(2)
# mousehover on Storage unit
storage = driver.find_element_by_xpath('//*[@id="topnav_wrapper"]/ul/li[5]/span')
actions = ActionChains(driver)
actions.move_to_element(storage).click().perform()

# Printing submenus of Storage unit
Submenus = driver.find_elements_by_css_selector(
    '#topnav_wrapper > ul > li.topnav_item.storageunit > div > div > ul > li>div>a')
print('\nSubmenus of Storage unit :')
for submenu in Submenus:
    print("{}".format(submenu.text))

# close the driver
driver.close()
