import numpy as np 
import scipy as sci
import pandas as pd
import os
from shutil import copyfile 
import datetime

folder = 'Data_st'

files = os.listdir(folder)
temp=np.zeros((3750,3273)) + np.nan
dewp=np.zeros((3750,3273)) + np.nan
slp=np.zeros((3750,3273)) + np.nan
stp=np.zeros((3750,3273)) + np.nan
MAX=np.zeros((3750,3273)) + np.nan
MIN=np.zeros((3750,3273)) + np.nan
prcp=np.zeros((3750,3273)) + np.nan
total=np.zeros((3750,3273*7)) + np.nan
n = 0
for file in files:
    data = np.loadtxt(folder+'\\'+file, delimiter=',')
    if np.sum(np.isnan(data[:,0])) <365 and np.sum(np.isnan(data[:,1])) <365 and np.sum(np.isnan(data[:,2])) <365 and np.sum(np.isnan(data[:,3])) <365 and np.sum(np.isnan(data[:,4])) <365 and np.sum(np.isnan(data[:,5])) <365 and np.sum(np.isnan(data[:,6])) <365:
        temp[:,n] = data[:,0]
        dewp[:,n] = data[:,1]
        slp[:,n] = data[:,2]
        stp[:,n] = data[:,3]
        MAX[:,n] = data[:,4]
        MIN[:,n] = data[:,5]
        prcp[:,n] = data[:,6]
        total[:,7*n:7*n+7] = data[:,:]
        n = n+1
np.savetxt('Data_va\\temp.csv', temp,delimiter=',')
np.savetxt('Data_va\\dewp.csv', dewp,delimiter=',')
np.savetxt('Data_va\\slp.csv', slp,delimiter=',')
np.savetxt('Data_va\\stp.csv', stp,delimiter=',')
np.savetxt('Data_va\\MAX.csv', MAX,delimiter=',')
np.savetxt('Data_va\\MIN.csv', MIN,delimiter=',')
np.savetxt('Data_va\\prcp.csv', prcp,delimiter=',')
np.savetxt('Data_va\\total.csv',total,delimiter=',')