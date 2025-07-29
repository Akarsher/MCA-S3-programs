
#importing required libraries and packages
import numpy as np
import pandas as pd
import  seaborn as sns
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, root_mean_squared_error

# creating dataframe and storing the dataset
df=pd.read_csv('C:/Users/mits31/Desktop/DataSet/Housing_Price.csv')
print(df.head())

#checking for null values
df.isnull().sum()

# Replace all non-numeric values with numeric values.
df.replace(to_replace='yes',value=1,inplace=True)
df.replace(to_replace='no',value=1,inplace=True)
df.replace(to_replace='unfurnished',value=0,inplace=True)
df.replace(to_replace='semi-furnished',value=1,inplace=True)
df.replace(to_replace='furnished',value=2,inplace=True)
print(df.head()) #table after replacing the values

#split datas for testing and training
x=df.drop('price',axis=1) #dropping the price column and storing all other values to the x variable
y=df['price']   #target variable
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33,random_state=42)


#Reshaping the y_test values
y_test=np.reshape(y_test,(-1,1))

#creating the model and training the model
model = LinearRegression()
model.fit(x_train,y_train)

print('Intercept value :', model.intercept_)
print('Slope :',model.coef_)

slope=model.coef_
f=x.columns
print(pd.DataFrame({'Features :':f,'reg_coef.:':slope}))

'''
print('area : ',model.coef_[0])
print('Bedroom : ',model.coef_[1])
print('Bathroom : ',model.coef_[2])
print('Stories : ',model.coef_[3])
print('main road : ',model.coef_[4])
print('guest room : ',model.coef_[5])
print('basement : ',model.coef_[6])
print('hotwater : ',model.coef_[7])
print('air conditioning : ',model.coef_[8])
print('parking area : ',model.coef_[9])
print('prefarea : ',model.coef_[10])
print('furnishing status : ',model.coef_[11])
'''

#making the prediction using our model by giving the x_test value
pred = model.predict(x_test)

#checking the model accuracy
res= r2_score(y_test,pred)
print('Accuracy :' , res)

#evaluating the model
mse =mean_squared_error(y_test,pred)
print('Mean Squared Error :',mse)

mae = mean_absolute_error(y_test,pred)
print('Mean Absolute Error:', mse)

rmse =root_mean_squared_error(y_test,pred)
print('Rooted Mean Squared Error :',rmse)
