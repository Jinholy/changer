import openpyxl as ox
import options as op





wb = ox.load_workbook(op.xls_file)
ws = wb.active
# ws = wb.get_sheet_by_name("Sheet1")

ws.cell(1, 1).value = 1



wb.close()

# 1 : num
# 2 : region
# 3 : city
# 4 : year
# 5 : magnitude
# 6 : file order
