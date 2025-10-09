import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


df = pd.read_csv("C:/Users/mits31/Downloads/jkcars.csv")
print(df.head(5))
rows,cols=df.shape
print("rows: ",rows)
print("columns: ",cols)
print(df.dtypes)
print(df.isnull().sum())
df1=df.drop(['Model','Car'],axis=1)
print(df1.head(5))
sil_score=[]
kval=range(2,11)
for k in kval:
    kmeans=KMeans(n_clusters=k,random_state=10)
    labels=kmeans.fit_predict(df1)
    silsc=silhouette_score(df1,labels)
    sil_score.append(silsc)
silhouette_df=pd.DataFrame({'K':kval,'Silhouette Score':sil_score})
max_silsc=silhouette_df['Silhouette Score'].max()
best_k=silhouette_df.loc[silhouette_df['Silhouette Score'].idxmax(),'K']
print("max score silhouette is: ",max_silsc," Optimal k value :",best_k)
# Plot silhouette scores vs number of clusters.
plt.figure(figsize=(9, 5))
plt.plot(silhouette_df['K'], silhouette_df['Silhouette Score'], marker='o')
plt.title('Silhouette Score vs Number of Clusters')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Silhouette Score')
plt.grid(True)
plt.show()
#best k value=best_k
k_means = KMeans(n_clusters=best_k, random_state=10)


# Fit the model to the scaled_df
k_means.fit(df1)

# Make a series using predictions by K-Means
clusters = pd.Series(k_means.predict(df1))
df['clusters']=clusters
print((df.head()))
