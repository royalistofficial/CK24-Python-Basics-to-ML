import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor

iris = sns.load_dataset("iris")
print(iris.head())


data = iris[["sepal_length", "petal_length", "species"]].copy()
mapping = {"setosa": 0, "versicolor": 1, "virginica": 2}
data["species"] = data["species"].map(mapping)
# data = data[(data["species"] == 1) | (data["species"] == 2)]


print(data.head())


# data_versicolor = data[data["species"] == 1]
# data_virginica = data[data["species"] == 2]

# data_versicolor_A = data_versicolor.iloc[:25, :]
# data_versicolor_B = data_versicolor.iloc[25:, :]

# data_virginica_A = data_virginica.iloc[:25, :]
# data_virginica_B = data_virginica.iloc[25:, :]


# data_df_A = pd.concat([data_versicolor_A, data_virginica_A], ignore_index=True)
# data_df_B = pd.concat([data_versicolor_B, data_virginica_B], ignore_index=True)


# x1_p = np.linspace(min(data['sepal_length']), max(data['sepal_length']), 1000)
# x2_p = np.linspace(min(data['petal_length']), max(data['petal_length']), 1000)

# X1_p, X2_p = np.meshgrid(x1_p, x2_p)
# X_p = pd.DataFrame(
#     np.vstack([X1_p.ravel(), X2_p.ravel()]).T, columns=["sepal_length", "petal_length"]
# )
# fig, ax = plt.subplots(2, 4, sharex='col', sharey='row')

# max_depth = [1, 3, 5, 7]
# X = data_df_A[["sepal_length", "petal_length"]]
# Y = data_df_A["species"]

# for j, md in enumerate(max_depth):
#     model = DecisionTreeClassifier(max_depth=md)
#     model.fit(X, Y)
    

#     ax[0, j].scatter(data_virginica_A["sepal_length"], data_virginica_A["petal_length"])
#     ax[0, j].scatter(data_versicolor_A["sepal_length"], data_versicolor_A["petal_length"])

#     y_p = model.predict(X_p)

#     ax[0, j].contourf(x1_p, x2_p, y_p.reshape((x1_p.shape[0], x2_p.shape[0])), alpha=0.3, levels=2, cmap="rainbow", zorder=1)


# X = data_df_B[["sepal_length", "petal_length"]]
# Y = data_df_B["species"]

# for j, md in enumerate(max_depth):
#     model = DecisionTreeClassifier(max_depth=md)
#     model.fit(X, Y)
    

#     ax[1, j].scatter(data_virginica_B["sepal_length"], data_virginica_B["petal_length"])
#     ax[1, j].scatter(data_versicolor_B["sepal_length"], data_versicolor_B["petal_length"])

#     y_p = model.predict(X_p)

#     ax[1, j].contourf(x1_p, x2_p, y_p.reshape((x1_p.shape[0], x2_p.shape[0])), alpha=0.3, levels=2, cmap="rainbow", zorder=1)
    
# plt.show()




data_setosa = data[data["species"] == 0]
data_versicolor = data[data["species"] == 1]
data_virginica = data[data["species"] == 2]

x1_p = np.linspace(min(data['sepal_length']), max(data['sepal_length']), 1000)
x2_p = np.linspace(min(data['petal_length']), max(data['petal_length']), 1000)

X1_p, X2_p = np.meshgrid(x1_p, x2_p)
X_p = pd.DataFrame(
    np.vstack([X1_p.ravel(), X2_p.ravel()]).T, columns=["sepal_length", "petal_length"]
)

# fig, ax = plt.subplots(1, 3, sharex='col', sharey='row')

# ax[0].scatter(data_setosa["sepal_length"], data_setosa["petal_length"])
# ax[0].scatter(data_virginica["sepal_length"], data_virginica["petal_length"])
# ax[0].scatter(data_versicolor["sepal_length"], data_versicolor["petal_length"])

# X = data[["sepal_length", "petal_length"]]
# Y = data["species"]

# md  = 6
# model1 = DecisionTreeClassifier(max_depth=md)
# model1.fit(X, Y)
# y_p = model1.predict(X_p)
# ax[0].contourf(x1_p, x2_p, y_p.reshape((x1_p.shape[0], x2_p.shape[0])), alpha=0.3, levels=2, cmap="rainbow", zorder=1)


# ax[1].scatter(data_setosa["sepal_length"], data_setosa["petal_length"])
# ax[1].scatter(data_virginica["sepal_length"], data_virginica["petal_length"])
# ax[1].scatter(data_versicolor["sepal_length"], data_versicolor["petal_length"])



# model2 = DecisionTreeClassifier(max_depth=md)
# b = BaggingClassifier(model2, n_estimators=2, max_samples=0.5, random_state=1)
# b.fit(X, Y)
# y_p = b.predict(X_p)
# ax[1].contourf(x1_p, x2_p, y_p.reshape((x1_p.shape[0], x2_p.shape[0])), alpha=0.3, levels=2, cmap="rainbow", zorder=1)




# ax[2].scatter(data_setosa["sepal_length"], data_setosa["petal_length"])
# ax[2].scatter(data_virginica["sepal_length"], data_virginica["petal_length"])
# ax[2].scatter(data_versicolor["sepal_length"], data_versicolor["petal_length"])

# model3 = RandomForestClassifier(n_estimators=2, max_samples=0.5, random_state=1)
# model3.fit(X, Y)
# y_p = model3.predict(X_p)
# ax[2].contourf(x1_p, x2_p, y_p.reshape((x1_p.shape[0], x2_p.shape[0])), alpha=0.3, levels=2, cmap="rainbow", zorder=1)


# plt.show()


# X = data[["sepal_length", "petal_length"]]
# Y = data["species"]

# fig, ax = plt.subplots(1, 1, sharex='col', sharey='row')


# ax.scatter(data_setosa["sepal_length"], data_setosa["petal_length"])
# ax.scatter(data_virginica["sepal_length"], data_virginica["petal_length"])
# ax.scatter(data_versicolor["sepal_length"], data_versicolor["petal_length"])

# model = RandomForestRegressor(n_estimators=20)
# model.fit(X, Y)
# y_p = model.predict(X_p)
# ax.contourf(x1_p, x2_p, y_p.reshape((x1_p.shape[0], x2_p.shape[0])), alpha=0.3, levels=2, cmap="rainbow", zorder=1)


# plt.show()

