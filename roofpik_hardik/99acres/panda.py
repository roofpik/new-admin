import openpyxl
from pandas import DataFrame
l1 = [1,2,3,4]
l2 = [1,2,3,4]
df = DataFrame({'Stimulus Time': l1, 'Reaction Time': l2})
df.to_excel('test.xlsx', sheet_name='sheet1', index=False)
