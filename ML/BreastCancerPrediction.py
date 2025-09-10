#import modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import isnull
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.naive_bayes import GaussianNB


#create dataframe
df=pd.read_csv('C:/Users/mits31/Desktop/DataSet/Breast_Cancer.csv')
print(df.head())
print(df.isnull())

x=df.drop(['id','diagnosis','Unnamed: 32'],axis=1)
y=df['diagnosis']

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

cm=confusion_matrix(y_test,pred)
plt.figure(figsize=(8,5))
sns.heatmap(cm,annot=True)
plt.title('Confusion Matrix Heatmap')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.show()