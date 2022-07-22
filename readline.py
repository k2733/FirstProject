'''
获取某包含若干csv文件的文件夹下各csv文件数据行数
'''

import os

rowcount = {}
path = r"C:\Users\vcc-user\Desktop\全是csv"  # 存放所有csv文件的文件夹
filelist = os.listdir(path)  # 存储了所有的文件名
for file1 in filelist:
    filename= 'C:/Users/vcc-user/Desktop/全是csv/' + file1
    print (file1)
    total = len(open(filename).readlines())
    rowcount[file1] = total
print(rowcount)