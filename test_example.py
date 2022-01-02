#no hay cython
from sklearn import datasets
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# boston = datasets.load_boston()
data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url,sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]

df_filter = raw_df.fillna(0)
# print(df_filter.head())
# x = df_filter[2]
# y = df_filter[6]

# plt.scatter(x,y)
# plt.show()
x = data[:,np.newaxis,5]
y = target

print(x)
print(y)

#algorithm
l_reg = linear_model.LinearRegression()

# #train
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.4)

model = l_reg.fit(x_train,y_train)
predictions = model.predict(x_test)

# #Mostrar grafica

plt.scatter(x_test,y_test)
plt.plot(x_test,predictions,color='green',linewidth=2)
plt.title('Regresion lineal entre el data y target')
plt.xlabel('data')
plt.ylabel('target')
plt.show()

# #Mostrar datos importantes
# print("predictions", predictions)
# print("R^2 value",l_reg.score(x,y))
# print("coedd",l_reg.coef_)
# print("intercept",l_reg.intercept_)


