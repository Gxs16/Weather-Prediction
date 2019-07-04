import numpy as np 

year_start = [0]

for year in range(2009,2014):
    if year %4 == 0:
        year_start += [year_start[-1]+366]
    else:
        year_start += [year_start[-1]+365]
y = np.loadtxt('Data_st\\545110-99999.csv',delimiter=',')[:2922,5]
loss_y = np.isnan(y)
y[loss_y]=0
year_start = np.array(year_start)
year_leap=[1460,2921]

y_day_average = np.zeros(366)
for i in range(365):

    y_day_average[i] = np.sum(y[year_start + i]) / np.sum(1 - loss_y[year_start + i])

    y[year_start + i] -= y_day_average[i]

y_day_average[365] = np.sum(y[year_leap]) / np.sum(1 - loss_y[year_leap])

y[year_leap] -= y_day_average[365]

y_true = np.loadtxt('Data_st\\545110-99999.csv',delimiter=',')[2928:3750,5]

np.savetxt('y_true_min.csv',y_true,delimiter=',')
np.savetxt('y_min.csv',y,delimiter=',')
np.savetxt('y_day_average_min.csv',y_day_average,delimiter=',')