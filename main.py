import glob
import options as ops
import xls_handler as xh


class data:
    def __init__(self, num, region, city, year, magnitude, file_order):
        self.num = num
        self.region = region
        self.city = city
        self.year = year
        self.magnitude = magnitude
        self.file_order = file_order


data_list = list()

# print(xh.get_data_by_key(1))  #1번은 attribute name이 나옴 2번부터 진짜 data임

i = 2
while True:
    tmp_list = xh.get_data_by_key(i)
    print(tmp_list[0])
    if tmp_list[0] == None:
        break
    else:
        data_list.append(data(i - 1, ops.region, tmp_list[0], tmp_list[1], tmp_list[2], (i - 1) % 3))
        i = i+1



for d in data_list:
    print(d.num, d.region, d.city, d.year, d.magnitude, d.file_order)


fpath = ops.fpath
f_list = glob.glob(fpath)

# result = '\n'.join(f_list)
# print(result)
