
### ЗАДАЧА НА ПРАКТИКУ № 1
# Обучение с учителем (классификация). Выбрать ДВА ЛЮБЫХ СОРТА и для них реализовать.
# 1. Метод опорных векторов
# 2. Метод главных компонент

# Обучение без учителя (классификация).
# 3. Метод k средних

# Требуется предоставить три программы и для каждой график, визуально показывающий решение

import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import seaborn as sns

iris = sns.load_dataset("iris")
data = iris[["sepal_length", "petal_length", "species"]].copy()
mapping = {"setosa": 0, "versicolor": 1, "virginica": 2}
data["species"] = data["species"].map(mapping)
data_df = data[(data["species"] == 1) | (data["species"] == 2)]  

X = data_df[["sepal_length", "petal_length"]].values
y = data_df["species"].values

svm = SVC(kernel='linear')
svm.fit(X, y)

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 500), np.linspace(y_min, y_max, 500))
Z = svm.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

plt.contourf(xx, yy, Z, alpha=0.3)
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()


pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

svm_pca = SVC(kernel='linear')
svm_pca.fit(X_pca, y)

Z = svm_pca.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

plt.contourf(xx, yy, Z, alpha=0.3)
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()


kmeans = KMeans(n_clusters=2)
kmeans.fit(X)

Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

plt.contourf(xx, yy, Z, alpha=0.3)
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()



### ЗАДАЧА НА ПРАКТИКУ № 2 (со звездочкой)
# Написать нейросеть, которая будет складывать два небольших числа (от 0 до 10)

# import numpy as np
# from tensorflow import keras
# from tensorflow.keras import layers

# X = []
# y = []
# for a in range(11):
#     for b in range(11):
#         X.append([a, b])
#         y.append(a + b)
# X = np.array(X, dtype=float)
# y = np.array(y, dtype=float)

# indices = np.arange(len(X))
# np.random.shuffle(indices)
# X = X[indices]
# y = y[indices]

# split = int(0.8 * len(X))
# X_train, X_test = X[:split], X[split:]
# y_train, y_test = y[:split], y[split:]

# model = keras.Sequential([
#     layers.Dense(16, activation='relu', input_shape=(2,)),
#     layers.Dense(16, activation='relu'),
#     layers.Dense(1)
# ])
# optimizer = keras.optimizers.Adam(learning_rate=1e-3)
# model.compile(optimizer=optimizer, loss='mse', metrics=['mae'])
# model.summary()

# history = model.fit(
#     X_train, y_train,
#     epochs=1000,
#     batch_size=16,
#     validation_split=0.1,
#     verbose=0
# )

# loss, mae = model.evaluate(X_test, y_test, verbose=0)
# print(f"loss: {loss:.4f}, mae: {mae:.4f}")

# for pair in [[3, 5], [10, 2], [7, 8]]:
#     pred = model.predict(np.array([pair], dtype=float))[0][0]
#     print(f"{pair[0]} + {pair[1]} = {pred:.2f}")
