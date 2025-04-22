import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier


iris = sns.load_dataset("iris")


print(iris.head())

# data = iris[["sepal_length", "petal_length", "species"]]
# data_df = data[(data["species"] == "setosa") | (data["species"] == "versicolor")]


# X = data_df[["sepal_length", "petal_length"]]
# Y = data_df["species"]

# data_df_setosa = data[data["species"] == "setosa"]
# data_df_versicolor = data[data["species"] == "versicolor"]


# plt.scatter(data_df_setosa["sepal_length"], data_df_setosa["petal_length"])
# plt.scatter(data_df_versicolor["sepal_length"], data_df_versicolor["petal_length"])


# model = SVC(kernel="linear", C=10000)
# model.fit(X, Y)

# print(model.support_vectors_)
# plt.scatter(
#     model.support_vectors_[:, 0], 
#     model.support_vectors_[:,1], 
#     s = 400, 
#     facecolor='none',
#     edgecolors='black')


# x1_p = np.linspace(min(data_df["sepal_length"]), max(data_df["sepal_length"]), 100)
# x2_p = np.linspace(min(data_df["petal_length"]), max(data_df["petal_length"]), 100)

# X1_p, X2_p = np.meshgrid(x1_p, x2_p)

# X_p = pd.DataFrame(
#     np.vstack([X1_p.ravel(), X2_p.ravel()]).T,
#     columns=["sepal_length", "petal_length"]
# )



# y_p = model.predict(X_p)

# X_p["species"] = y_p

# X_p_setosa = X_p[X_p["species"] == "setosa"]
# X_p_versicolor = X_p[X_p["species"] == "versicolor"]

# plt.scatter(X_p_setosa["sepal_length"], X_p_setosa["petal_length"], alpha=0.1)
# plt.scatter(X_p_versicolor["sepal_length"], X_p_versicolor["petal_length"], alpha=0.1)


# дз убрать из iris на которых обучаемся и убедится что на предсказания влеяют только опорные вектора





# data = iris[["sepal_length", "petal_length", "species"]]
# data_df = data[(data["species"] == "virginica") | (data["species"] == "versicolor")]


# X = data_df[["sepal_length", "petal_length"]]
# Y = data_df["species"]

# data_df_virginica = data[data["species"] == "virginica"]
# data_df_versicolor = data[data["species"] == "versicolor"]

# C_val = [[10000, 1000, 100, 10], [1, 0.1, 0.01, 0.001]]

# fig, ax = plt.subplots(2, 4, sharex='col', sharey='row')
# for i in range(2):
#     for j in range(4):
#         ax[i, j].scatter(data_df_virginica["sepal_length"], data_df_virginica["petal_length"])
#         ax[i, j].scatter(data_df_versicolor["sepal_length"], data_df_versicolor["petal_length"])


#         model = SVC(kernel="linear", C=C_val[i][j])

#         model.fit(X, Y)

#         print(model.support_vectors_)
#         ax[i, j].scatter(
#             model.support_vectors_[:, 0], 
#             model.support_vectors_[:,1], 
#             s = 400, 
#             facecolor='none',
#             edgecolors='black')


#         x1_p = np.linspace(min(data_df["sepal_length"]), max(data_df["sepal_length"]), 100)
#         x2_p = np.linspace(min(data_df["petal_length"]), max(data_df["petal_length"]), 100)

#         X1_p, X2_p = np.meshgrid(x1_p, x2_p)

#         X_p = pd.DataFrame(
#             np.vstack([X1_p.ravel(), X2_p.ravel()]).T,
#             columns=["sepal_length", "petal_length"]
#         )



#         y_p = model.predict(X_p)

#         X_p["species"] = y_p

#         X_p_virginica = X_p[X_p["species"] == "virginica"]
#         X_p_versicolor = X_p[X_p["species"] == "versicolor"]

#         ax[i, j].scatter(X_p_virginica["sepal_length"], X_p_virginica["petal_length"], alpha=0.1)
#         ax[i, j].scatter(X_p_versicolor["sepal_length"], X_p_versicolor["petal_length"], alpha=0.1)


# plt.show()




# так проще заменять на числа и copy() чтобы небыло ошибки с изменением  iris
data = iris[["sepal_length", "petal_length", "species"]].copy()
mapping = {"setosa": 0, "versicolor": 1, "virginica": 2}
data["species"] = data["species"].map(mapping)
data_df = data[(data["species"] == 2) | (data["species"] == 1)]


X = data_df[["sepal_length", "petal_length"]]
Y = data_df["species"]

data_df_setosa = data[data["species"] == 0]
data_df_versicolor = data[data["species"] == 1]
data_df_virginica = data[data["species"] == 2]



# plt.scatter(data_df_setosa["sepal_length"], data_df_setosa["petal_length"])
plt.scatter(data_df_versicolor["sepal_length"], data_df_versicolor["petal_length"])
plt.scatter(data_df_virginica["sepal_length"], data_df_virginica["petal_length"])


model = DecisionTreeClassifier()
model.fit(X, Y)


x1_p = np.linspace(min(data_df["sepal_length"]), max(data_df["sepal_length"]), 100)
x2_p = np.linspace(min(data_df["petal_length"]), max(data_df["petal_length"]), 100)

X1_p, X2_p = np.meshgrid(x1_p, x2_p)

X_p = pd.DataFrame(
    np.vstack([X1_p.ravel(), X2_p.ravel()]).T,
    columns=["sepal_length", "petal_length"]
)



y_p = model.predict(X_p)
Z = y_p.reshape(X1_p.shape)

plt.contourf(X1_p, X2_p, Z, levels=1, alpha=0.3, cmap="coolwarm")

plt.show()






# дз



# data = iris[["sepal_length", "petal_length", "species"]]
# data_df = data[(data["species"] == "virginica") | (data["species"] == "versicolor")]


# X = data_df[["sepal_length", "petal_length"]]
# Y = data_df["species"]

# data_df_virginica = data[data["species"] == "virginica"]
# data_df_versicolor = data[data["species"] == "versicolor"]
# C_val = 1
# fraction = [[0.1, 0.15, 0.20, 0.25], [0.5, 0.75, 0.95, 1.]]

# fig, ax = plt.subplots(2, 4, figsize=(16, 8), sharex='col', sharey='row')

# for i in range(2):
#     for j in range(4):
#         f = fraction[i][j]

#         ax[i, j].scatter(data_df_virginica["sepal_length"], data_df_virginica["petal_length"])
#         ax[i, j].scatter(data_df_versicolor["sepal_length"], data_df_versicolor["petal_length"])



#         sample_indices = np.random.choice(X.index, size=int(len(X) * f), replace=False)
#         X_sample = X.loc[sample_indices]
#         Y_sample = Y.loc[sample_indices]

#         model = SVC(kernel="linear", C=C_val)
#         model.fit(X_sample, Y_sample)

#         ax[i, j].scatter(
#             model.support_vectors_[:, 0], 
#             model.support_vectors_[:, 1], 
#             s=200, facecolor='none', edgecolors='black', linewidths=1.5, label="support vectors"
#         )

#         x1_p = np.linspace(X["sepal_length"].min(), X["sepal_length"].max(), 100)
#         x2_p = np.linspace(X["petal_length"].min(), X["petal_length"].max(), 100)
#         X1_p, X2_p = np.meshgrid(x1_p, x2_p)
#         X_p = pd.DataFrame(np.vstack([X1_p.ravel(), X2_p.ravel()]).T, columns=["sepal_length", "petal_length"])
#         y_p = model.predict(X_p)
#         X_p["species"] = y_p

#         for species, color, alpha in zip(["virginica", "versicolor"], ["blue", "green"], [0.1, 0.1]):
#             mask = X_p["species"] == species
#             ax[i, j].scatter(X_p.loc[mask, "sepal_length"], X_p.loc[mask, "petal_length"], 
#                              color=color, alpha=alpha, label=f"predicted {species}" if f == 1.0 else None)

#         ax[i, j].set_title(f"{int(f * 100)}%")
#         ax[i, j].set_xlim(X["sepal_length"].min(), X["sepal_length"].max())
#         ax[i, j].set_ylim(X["petal_length"].min(), X["petal_length"].max())
#         ax[i, j].set_xlabel("sepal_length")
#         ax[i, j].set_ylabel("petal_length")

# plt.tight_layout()
# plt.show()
