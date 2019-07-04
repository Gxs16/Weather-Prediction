import numpy as np 
import scipy as sci
import pandas as pd
import os
from shutil import copyfile 

nofile = pd.read_csv('nofile.csv')
folder = 'Data_date'
files = os.listdir(folder)

nofile_dedup = nofile.drop_duplicates()
stats_data = pd.read_csv('stats.csv')
for row in nofile_dedup['ID']:
    stats_data = stats_data.drop(stats_data[stats_data['USAF-WBAN']==row].index.tolist())

stats_data.to_csv('stats_file.csv',index=False)

stats_file = stats_data
for year in range(2009,2020):
    for usaf_wban in stats_file['USAF-WBAN'].get_values():
        try:
            copyfile('Data_date\\'+usaf_wban+'-'+str(year)+'.op.gz','Data_file\\'+usaf_wban+'-'+str(year)+'.op.gz')
        except Exception:
            print(usaf_wban+'-'+str(year))