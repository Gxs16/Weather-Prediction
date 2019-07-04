import numpy as np 
import scipy as sci
import pandas as pd
import os
from shutil import copyfile 
stationlist = pd.read_csv('isd-history.csv', low_memory=False)
usable_enddate = stationlist.loc[stationlist['END']>=20190326]
usable_date = usable_enddate.loc[usable_enddate['BEGIN']<=20090101]
usable_date.to_csv('usable_date.csv', index = False)

stats_data=[]
for row in usable_date.get_values():
    stats_data += [[row[0].zfill(6)+'-'+str(row[1]).zfill(5),row[2],row[3],row[4],row[5],row[6],row[7]]]
stats_data = pd.DataFrame(stats_data,columns=['USAF-WBAN', 'STATION NAME', 'CTRY', 'ST CALL', 'LAT', 'LON', 'ELEV(m)'])

stats_data.to_csv('stats.csv', index = False)
nofile = []
for year in range(2009,2020):
    for usaf_wban in stats_data['USAF-WBAN'].get_values():
        try:
            copyfile('Data\\'+usaf_wban+'-'+str(year)+'.op.gz','Data_date\\'+usaf_wban+'-'+str(year)+'.op.gz')
        except Exception:
            nofile += [[usaf_wban,str(year)]]
            print(usaf_wban+'-'+str(year))

nofile = pd.DataFrame(nofile,columns=['ID','year'])
nofile['ID'].to_csv('nofile.csv',index = False)