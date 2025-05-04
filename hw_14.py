import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.svm import SVC


iris = sns.load_dataset("iris")
print(iris.head())


data = iris[["sepal_length", "petal_length", "species"]].copy()
mapping = {"setosa": 0, "versicolor": 1, "virginica": 2}
data["species"] = data["species"].map(mapping)
data_df = data[(data["species"] == 2) | (data["species"] == 1)]


print(data_df.head())
