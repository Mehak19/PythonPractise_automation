import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver= webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait(20)
data=pd.read_excel('login.xlsx',sheet_name='login_page')
print("fdsgnddgfnfd")
while True:
      i,x=0
      i=+1
      x=+1
      driver.find_element_by_id("txtUsername").send_keys(data.loc[i,'username']+Keys.TAB+data.loc[x,'password':]+Keys.ENTER)
