import pandas as pd
from pandas import isnull
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error, accuracy_score, classification_report, \
    f1_score

df=pd.read_csv('C:/Users/mits31/Desktop/DataSet/social-network-ads.csv')
print(df.head())

print(df.isnull().sum())

x=df.drop(['User ID','Purchased'],axis=1)
y=df['Purchased']

print(x.info())

x_dummy=pd.get_dummies(x)
print(x_dummy.head())

x_train,x_test,y_train,y_test=train_test_split(x_dummy,y, test_size=0.30,random_state=42)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(x_train,y_train)

pred=model.predict(x_test)

score=model.score(x_train,y_train)
print('Accuracy Score : ',score)

print('Shape of X_train set : ',x_train.shape)
print('Shape of Y_train set : ',y_train.shape)
print('Shape of X_test set : ',x_test.shape)
print('Shape of Y_test set : ',y_test.shape)

print(classification_report(y_test,pred))
print('y_train f1 score :',f1_score(y_train,pred))
