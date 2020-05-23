import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

# Assingment:
# Scenario 1:
# •	launch browser
# •	navigate to urban ladder website
# •	go to the menu,listed as Living
# •	print  the headings or submenus inside living menu
# •	print all the subheadings under submenus of living module

# launch the browser
driver = webdriver.Chrome(ChromeDriverManager().install())

# navigate to url
driver.get("https://www.urbanladder.com/")

# handle synchronization issues with implicit wait
driver.implicitly_wait(50)

# maximize the window
driver.maximize_window()

# title of Homepage
actual_title = driver.title

# validate title of HomePageR
assert actual_title == 'Furniture Online: Buy Home Wooden Furniture Online In India At Best Price - Urban Ladder - Urban Ladder', print(
    "-------->test case failed: unable to validate title of home page")
print("Title of Homepage ------>", actual_title, "--------->test case passed")

# close the window popup
driver.find_element_by_xpath('''//a[contains(@class,'close-reveal-modal')]''').click()

time.sleep(2)
# mousehover on living unit
living_unit = driver.find_element_by_xpath('//li[contains(@class,"living")]/span')
actions = ActionChains(driver)
actions.move_to_element(living_unit).click().perform()

#  submenus of Living unit
submenus = driver.find_elements_by_xpath(
    '//li[contains(@class,"living")]/descendant::div[@class="taxontype"]/a')
print('\nmenu living unit :')
submenu_count = len(submenus)
#  count of submenus of Living unit
print("submenu count------>", submenu_count)

for i in range(1, submenu_count + 1):
    sub_headings = driver.find_elements_by_css_selector(
        '#topnav_wrapper > ul > li.topnav_item.livingunit > div > div > ul > li:nth-child(' + str(
            i) + ') > ul>li>a>span')
    count = len(sub_headings)
    print("submenu Heading------>", submenus[i - 1].text + "\ncount of sub Headings:", count)
    for sub_heading in sub_headings:
        print("{}".format(sub_heading.text))
# close the browser
driver.close()
