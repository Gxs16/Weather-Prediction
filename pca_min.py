import numpy as np 
from sklearn.decomposition import PCA

raw = np.loadtxt('Data_va\\MIN.csv',delimiter=',')
origin = raw[:2922,:]
loss = np.isnan(origin)

origin[loss] = 0

year_start = [0]

for year in range(2009,2014):
    if year %4 == 0:
        year_start += [year_start[-1]+366]
    else:
        year_start += [year_start[-1]+365]
        
year_start = np.array(year_start)
year_leap=[1460,2921]
day_average = np.zeros((366,3273))
for i in range(365):
    day_average[i] =np.sum(origin[year_start + i], axis = 0) / np.sum(1 - loss[year_start + i], axis = 0) 
    origin[year_start + i] -= day_average[i]  # 距平
    
day_average[365] = np.sum(origin[year_leap], axis = 0) / np.sum(1 - loss[year_leap], axis = 0) 

origin[year_leap] -= day_average[365] 

origin[loss] = 0  

origin_std = np.std(origin, axis = 0) / ((np.sum(1 - loss, axis = 0) / 3287) ** 0.5)  

origin /= origin_std

pca = PCA(n_components = 1000)
pca.fit(origin)
X=pca.fit_transform(origin)
X=X[:-6]
#test
origin_valid = raw[2922:3750,:]
loss_valid = np.isnan(origin_valid)
for i in range(828):
    origin_valid[i]-=day_average[i%365]
origin_valid[loss_valid] = 0
origin_valid /= origin_std
X_valid = pca.transform(origin_valid)
np.savetxt('X_MIN.csv',X,delimiter=',')
np.savetxt('X_valid_MIN.csv',X_valid,delimiter=',')