#import modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import read_csv
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


#get dataset
df=pd.read_csv('C:/Users/mits31/Desktop/DataSet/iris.csv')
print(df.head())

r,c=df.shape
print('Number of Rows : ',r,'\nNumber of columns :',c)

#split train and test data
x=df.drop(['Id','Species'],axis=1)
y=df['Species']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.30,random_state=42)

#model creation
model = DecisionTreeClassifier(criterion='entropy',min_samples_split=50)
model.fit(x_train,y_train)

#prediction
pred = model.predict(x_test)

#visualization
plt.figure(figsize=(15,15))
plt.title('Decision Tree')
tree.plot_tree(model,filled=True,fontsize=10)
plt.show()

#Accuracy
print('Accuracy : ',accuracy_score(y_test,pred))

# Display Decision Tree using graphics
fname=['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']
tnmae=y.unique().tolist()

model2=DecisionTreeClassifier(criterion='entropy',random_state=42,max_depth=3)
model2.fit(x_train,y_train)
