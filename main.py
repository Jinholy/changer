import glob
import options as ops


class data:
    def __init__(self, num, region, city, year, magnitude, file_order):
        self.num = num
        self.region = region
        self.city = city
        self.year = year
        self.magnitude = magnitude
        self.file_order = file_order


data_list = list()

data_list.append(data(1, 2, 3, 4, 5, 6))

print(data_list.pop())

fpath = ops.fpath
f_list = glob.glob(fpath)

#result = '\n'.join(f_list)
#print(result)
