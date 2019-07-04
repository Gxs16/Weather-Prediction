import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np 

m = Basemap(llcrnrlon = -180, llcrnrlat = -90, urcrnrlon = 180, urcrnrlat = 90, ellps = 'WGS84')
m.drawcoastlines()

x = np.loadtxt('stats_file.csv',delimiter = ',',skiprows = 1,usecols=(4,5))
plt.xlim(-180,180)
plt.ylim(-90,90)
plt.scatter(x[:,1],x[:,0],marker='.',s=0.5,c='red')
plt.title('Stations')
plt.show()