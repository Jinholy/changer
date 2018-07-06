import glob
import options as ops
import xls_handler as xh
import os



def change_file_name():
    #flielist : c_name ,f_list
    flist = xh.make_file_list()
    j = 1
    for fl in flist:
        i = 0
        new_path = ops.fpath + fl.c_name
        for f in fl.f_list:
            #old_path = ops.fpath + str(j+1) + ops.separator + f        #파일에 29번없이 30번으로 바로가서 한번 밀어줘야함
            old_path = ops.fpath + str(j+1) + ops.separator + f
            new_path + ops.separator + str(i) + ops.ext
            #print(old_path + "-->" + new_path + ops.separator + str(i) + ops.ext)
            i = i + 1
            #os.rename(old_path, new_path + ops.separator + str(i) + ops.ext)
            #print(old_path)

            try:
                os.rename(old_path, new_path + ops.separator + str(i) + ops.ext)
                #pass
            except FileNotFoundError as e:
                print(e)

        j = j + 1


change_file_name()
#os.startfile('C:\\Users\\hnsle\\Desktop\\university\\earthquake\\data\\AT\\NA_AT\\100_NCALIF.AG_D-CPMDWN.AT2')
'''
def get_origin_file_list():
    fpath = ops.fpath
    f_list = glob.glob(fpath)
    result = '\n'.join(f_list)

    return result
'''

