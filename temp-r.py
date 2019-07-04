import numpy as np 
from sklearn.decomposition import PCA
from sklearn import linear_model
import matplotlib.pyplot as plt 
X=np.loadtxt('X_temp.csv',delimiter=',')
y = np.loadtxt('y.csv',delimiter=',')
loss_y = np.isnan(y[6:])
y = y [6:]
loss_y = loss_y
use_y = loss_y ==0
new_y = y[use_y]
new_X=X[use_y]
y_true = np.loadtxt('y_true.csv',delimiter=',')
y_day_average = np.loadtxt('y_day_average.csv',delimiter=',')
#linear_model
clf=linear_model.LinearRegression()
clf.fit(new_X,new_y)
y_fore_test = np.sum(new_X*clf.coef_,axis=1)+clf.intercept_
print('MAE',np.average(abs(y_fore_test-new_y)))

X_valid = np.loadtxt('X_valid_temp.csv',delimiter=',')

y_r = np.sum(X_valid * clf.coef_,axis = 1) + clf.intercept_
for i in range(828):
    y_r[i]+=y_day_average[i%365]


y_true[821] =y_day_average[821%365]
y_true[679] =y_day_average[679%365]
y_true[680] =y_day_average[680%365]
y_true[681] =y_day_average[681%365]
y_true[682] =y_day_average[682%365]
y_true[683] =y_day_average[683%365]
y_true[684] =y_day_average[684%365]
print('mae:',np.average(abs(y_r[:-6]-y_true)))
np.savetxt('Linear\\y_predict_temp.csv',y_r,delimiter=',')

np.savetxt('Use\\X_valid.csv',X_valid,delimiter=',')
np.savetxt('Linear\\y_fore_test.csv',y_fore_test,delimiter=',')
x=np.arange(0,822)
plt.figure()
plt.plot(x,y_true,x,y_r[:-6])
plt.legend('True','Prediction')
plt.show()