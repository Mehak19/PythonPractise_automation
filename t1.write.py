import pandas as pd

data=pd.DataFrame({'Book':['Python','java','c#','Rust','Js'],
              'Book number':[4,7,5,6,8],
               'Author':['Rossum','willeys','oreilly','williams','john'],
                'language':['hindi','English','german','french','chinese'],
                   'Location':['delhi','lucknow','bangalore','Chennai','kolkata']})
print(data)
writer=pd.ExcelWriter('sample.xlsx',engine='xlsxwriter')
data.to_excel(writer,sheet_name='sheet 1')
writer.save()