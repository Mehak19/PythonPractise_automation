import pandas as pd

data=pd.DataFrame({'username':['admin','admin123','Admin'],
              'password':['','Admin','admin123']})

writer=pd.ExcelWriter('login.xlsx',engine='xlsxwriter')
data.to_excel(writer,sheet_name='login_page')
writer.save()
