#import modules
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.naive_bayes import GaussianNB


#create dataframe
df=pd.read_csv('C:/Users/mits31/Desktop/DataSet/iris.csv')
print(df.head())

#split data
x=df.drop(['Species'],axis=1)
y=df['Species']

#Train the data
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30,random_state=42,stratify=y)

#model creation
model=GaussianNB()
model.fit(x_train,y_train)

#prediction
pred=model.predict(x_test)

#accuracy and model evaluation
print('\n Accuracy :',accuracy_score(y_test,pred))
print('\n Classification Report :\n',classification_report(y_test,pred))
print('\n Confusion Matrix : \n',confusion_matrix(y_test,pred))

#Impliment NaiveBayes algorithm using breast cancer dataset