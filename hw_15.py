import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

iris = sns.load_dataset("iris")
print(iris.head())


data = iris[["petal_width", "petal_length", "species"]].copy()


data_v = data[data["species"] == "versicolor"]
data_v = data_v.drop(columns="species")
x = data_v['petal_width']
y = data_v['petal_length']


plt.scatter(x, y)


p = PCA(n_components=2)

p.fit(data_v)

print(p.components_)
print(p.explained_variance_)
print(p.mean_)

plt.plot([p.mean_[0], p.mean_[0] + p.components_[0][0] * np.sqrt(p.explained_variance_[0])],
          [p.mean_[1], p.mean_[1] + p.components_[0][1] * np.sqrt(p.explained_variance_[0])])
plt.plot([p.mean_[0], p.mean_[0] + p.components_[1][0] * np.sqrt(p.explained_variance_[1])],
          [p.mean_[1], p.mean_[1] + p.components_[1][1] * np.sqrt(p.explained_variance_[1])])
plt.show()