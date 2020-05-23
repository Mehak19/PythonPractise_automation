import pandas as pd

# Aliasing that means pandas as pd

excel_data=pd.read_excel('sample.xlsx')
data=excel_data.set_index('Book')
print(data)
print('------------------------------------------')
print(excel_data.head(2))
print('------------------------------------------')
print(excel_data.tail(2))
print('------------------------------------------')
print(data.loc['java':'Js','Book number':'language'])
print('------------------------------------------')
print(data.loc['c#':,'Author':'Location'])
print('------------------------------------------')
print(data.loc['c#',:])