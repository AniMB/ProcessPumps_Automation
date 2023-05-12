from openpyxl import Workbook,load_workbook
wb = load_workbook(filename='mypractsheet.xlsx')
ws= wb.active

ws.title ='trial'

data={'val1': ['40'] , 'val2': ['5'], 'val3': ['60'] , 'val4': ['70']}
'''
print(data)
l=type(data)
print(l)
'''

for record in [[k]+v for k,v in data.items()]:
    ws.append(record)

wb.save('mypractsheet.xlsx')

