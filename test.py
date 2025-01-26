import pandas as pd
import numpy
from pandas import DataFrame
import os
import xlwt
import xlrd
from xlutils.copy import copy


write_into = pd.read_excel("FINAL.xlsx", sheet_name='State-Year')

write_list = write_into['State'].to_list()
state_index = write_list.index('Colorado')
column_index = write_into.columns.get_loc('General Notes')


df = DataFrame({'State': ['Colorado'], 'General Notes': ['hello lmao']})
writer = pd.ExcelWriter('FINAL.xlsx')
df.to_excel(excel_writer=writer, sheet_name='State-Year', index=False, startrow=state_index, startcol=column_index)
