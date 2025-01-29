import openpyxl
import pandas as pd

wb = openpyxl.load_workbook('QC standard files.xlsx')
pandas_type = pd.read_excel('QC standard files.xlsx', sheet_name='State-Year')

ws = wb['State-Year']

column_index = pandas_type.columns.get_loc('missing custody_50to64') + 1
row_index = pandas_type[pandas_type["State"] == 'Alabama'].index[0] + 2
print(f'Row: {row_index}, Column: {column_index}')
test = ws.cell(row_index, column=column_index)
test.value = "htoabobo"
test.value = 'hotabobo again please pleapslepasdl'
wb.save('QC standard files.xlsx')
