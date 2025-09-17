#import modules
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import k_means, KMeans
from sklearn.metrics import silhouette_score

#Load Cars dataset
df=pd.read_csv('C:/Users/mits31/Desktop/DataSet/jkcars.csv')
print(df.head())

r,c = df.shape
print ('Number of rows :',r,'\nNumber of columns :',c)
print('Datatypes :',df.dtypes)
print('Missing values :\n',df.isnull().sum())

# Create a new DataFrame consisting of three columns 'Volume', 'Weight', 'CO2'.
newdf= df[['Weight','Volume','CO2']]

# Print the first 5 rows of this new DataFrame.
print(newdf.head(5))

# Create an empty list to store silhouette scores obtained for each 'K'
inertia = []
sil_score = []

# Calculate inertia and silhouette score for different values of 'K'.
for i in range(2,11):
    k_means=KMeans(n_clusters=i,random_state=42)
    k_means.fit(newdf)
    inertia.append(k_means.inertia_)
    score = silhouette_score(newdf,k_means.labels_)
    sil_score.append(score)

# Plot silhouette scores vs number of clusters.
plt.figure(figsize=(15,15))
plt.plot(sil_score,marker='o')
plt.title('K Means Algorithm Diagram')
plt.grid(True)
plt.show()

# Clustering the dataset for K = 3
# Perform K-Means clustering with n_clusters = 3 and random_state = 10
clust=KMeans(n_clusters=3,random_state=10)

# Fit the model to the scaled_df
clust.fit(newdf)

# Make a series using predictions by K-Means
labels = pd.Series(clust.labels_, name='Clusters')

