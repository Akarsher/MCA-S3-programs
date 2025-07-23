#importing all required libraries
import numpy as np;
import pandas as pd;
import seaborn as sns;
import matplotlib.pyplot as plt;
from sklearn import linear_model;
from sklearn.linear_model import LinearRegression;
from sklearn.model_selection import train_test_split;
from sklearn.metrics import mean_squared_error, r2_score;

df=pd.read_csv('C:/Users/mits31/Downloads/insurance_dataset (1) - insurance_dataset (1).csv')
print(df.head())

#checking for null values in data set
df.isnull().sum()

# regression plot of age and charges relation
plt.figure(figsize=(10,5))
plt.title('Insurance Charges and Age')
sns.regplot(x='age',y='charges',color='red',line_kws={'color':'blue'},data=df)
plt.grid()
plt.show()

#split data into 2 for training
#train data
x=df['age']
y=df['charges']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4,random_state=42)

#Reshaping the model
x_train = np.reshape(x_train,(-1,1))
x_test = np.reshape(x_test,(-1,1))
y_train = np.reshape(y_train,(-1,1))


#creating a model
model=LinearRegression()
model.fit(x_train,y_train)

# Displaying slope and intercept
print('Slope :',model.coef_)
print('Intercept :',model.intercept_)

#create prediction variable for predicting output
pred=model.predict(x_test)

#Evaluating the model's performance
res = r2_score(y_test,pred)
print('Accuracy :', res)





