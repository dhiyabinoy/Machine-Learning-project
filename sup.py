import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
x=np.array([[1,2],[2,3],[3,3],[8,8],[9,10],[10,9],[15,16],[16,15],[17,17]])
Kmeans=KMeans(n_clusters=5,random_state=42)
clusters=Kmeans.fit_predict(x)
plt.scatter (x[:,0],x[:,1],c=clusters)
centers=Kmeans.cluster_centers_
plt.scatter(centers[:,0],centers[:,1],marker='x',s=200)
plt.xlabel("feature1")
plt.ylabel("feature2")
plt.title("UNSUPERVISED")
plt.show()

