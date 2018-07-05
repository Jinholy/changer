import openpyxl as ox
import options as op

wb = ox.load_workbook(op.xls_file)
ws = wb.active
ws2 = wb.get_sheet_by_name("Sheet2")

city_dic = {}


def init_dic:
    i = 2
    while True:
        if ws2['B' + str(i)].value == None:
            break
        else:
            city_dic.
            i = i+1


def get_data_by_key(key):
    # Event:J , Year:K, Mag:M
    key = str(key)
    return [ws['J' + key].value, ws['K' + key].value, ws['M' + key].value]


wb.close()

# 1 : num
# 2 : region
# 3 : city
# 4 : year
# 5 : magnitude
# 6 : file order
