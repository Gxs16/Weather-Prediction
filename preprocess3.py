import numpy as np 
import scipy as sci
import pandas as pd
import os
from shutil import copyfile 
import datetime
date0 = datetime.datetime.strptime('20090101', "%Y%m%d")

def line2desc(data):

    stn = data[:6]
    wban = data[7:12]
    date = (datetime.datetime.strptime(data[14:22], "%Y%m%d") - date0).days
    
    temp = float(data[24:30])
    if temp == 9999.9:
        temp = np.nan
        
    dewp = float(data[35:41])
    if dewp == 9999.9:
        dewp = np.nan

    slp = float(data[46:52])
    if slp == 9999.9:
        slp = np.nan

    stp = float(data[57:63])
    if stp == 9999.9:
        stp = np.nan

    MAX = float(data[102:108])
    if MAX == 9999.9:
        MAX = np.nan

    MIN = float(data[110:116])
    if MIN == 9999.9:
        MIN = np.nan

    prcp = float(data[118:123])
    if prcp == 99.99:
        prcp = np.nan

    return [stn + '-' + wban, date, temp, dewp, slp, stp, MAX, MIN, prcp]

folder = 'Data_file'

files = os.listdir(folder)

#####
stats = pd.read_csv('stats_file.csv',low_memory=False)
n = 0

for usaf_wban in stats['USAF-WBAN'].get_values():

    total = np.zeros((3750,7)) + np.nan

    for y in range(2009,2020):

        data_temp = pd.read_csv(folder + '\\' + usaf_wban+'-'+str(y)+'.op.gz', low_memory=False).get_values()  # 读取每个站点每年的数据

        for row in data_temp:

            desc = line2desc(row[0])  # 将一行数据转化为需要的数据
            #print(desc)
            line = np.array(desc[2:])

            total[desc[1],:] = line  # 每7列一个站点，desc[1]是从2001年1月1日至数据记录时的天数，也就是在矩阵中的行数
    np.savetxt('Data_st\\'+usaf_wban+'.csv', total,delimiter=',')
        