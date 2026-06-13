import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
x=np.array([[2,3,1],[3,4,2],[4,5,3],[8,9,7],[9,10,8],[10,11,9]])
pca=PCA(n_components=2)
x_pca=pca.fit_transform(x)
print(x_pca)
plt.scatter(x_pca[:,0],x_pca[:,1])
plt.xlabel("features1")
plt.ylabel("features2")
plt.title("PCA")
plt.show()
