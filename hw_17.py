import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import seaborn as sns
import random
from sklearn.datasets import make_regression 
from numpy.linalg import inv, qr
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, KFold, cross_val_score


# iris = sns.load_dataset("iris")
#
# print(iris.head())
# print(type(iris))
#
# print(type(iris.values))
# print(iris.values.shape)
# print(iris.columns)
# print(iris.index)


# np.random.seed(1)
# x = 10 * np.random.rand(50)

# y = 2 * x + np.random.randn(50)

# plt.scatter(x, y)

# model = LinearRegression()
# model = LinearRegression(fit_intercept=False)


# print(x.shape)
# print(y.shape)
# X = x[:, np.newaxis]

# model.fit(X, y)
# print(model.coef_[0])  
# print(model.intercept_)  #

# x_ = np.linspace(0, 10, 30)
# y_ = model.coef_[0] * x_ + model.intercept_

# plt.plot(x_, y_)

# xfit = np.linspace(0, 10, 5)
# yfit = model.predict(xfit[:, np.newaxis])

# plt.scatter(xfit, yfit)

# plt.show()



# features, target = make_regression(n_samples=100, n_features=1, n_informative=1,
#                                    n_targets=1, noise=15, random_state=1)
# print(features.shape)
# print(target.shape)
#
# model = LinearRegression().fit(features, target)
#
# plt.scatter(features, target)
#
# x = np.linspace(features.min(), features.max(), 100)
# # y = kx + b
# plt.plot(x, model.coef_[0] * x + model.intercept_, color='red')
#
# plt.show()


# data = np.array(
#     [
#         [1, 5],
#         [2, 7],
#         [3, 7],
#         [4, 10],
#         [5, 11],
#         [6, 14],
#         [7, 17],
#         [8, 19],
#         [9, 22],
#         [10, 28]
#     ]
# )

# x = data[:, 0]
# y = data[:, 1]

# n = len(x)

# w_1 = (n * sum(x[i] * y[i] for i in range(n)) - sum(x[i] for i in range(n)) * sum(y[i] for i in range(n))
#       ) / (n * sum(x[i] ** 2 for i in range(n)) - sum(x[i] for i in range(n)) ** 2)
#
# w_0 = ((sum(y[i] for i in range(n))) / n) - w_1 * (sum(x[i] for i in range(n))) / n
#
# print(w_1, w_0)
# 2.4 -118.0

# x_1 = np.vstack([x, np.ones(len(x))]).T
# w = inv(x_1.transpose() @ x_1) @ (x_1.transpose() @ y)
#
# print(w)

# Q, R = qr(x_1)
# w = inv(R).dot(Q.transpose()).dot(y)
#
# print(w)


# def f(x):
#     return (x - 3) ** 2 + 4


# def dx_f(x):
#     return 2 * x - 6

# x = np.linspace(-10, 10, 100)
#
# ax = plt.gca()
# ax.xaxis.set_major_locator(plt.MultipleLocator(0.5))
#
# # plt.plot(x, f(x))
# plt.plot(x, dx_f(x))
# plt.grid()
#
# plt.show()

# L = 0.001  # скорость обучения (шаг)
# iterations = 100_000
#
# x = random.randint(0, 5)
# for i in range(iterations):
#     d_x = dx_f(x)
#     x -= L * d_x
# print(x, f(x))
# # x = 3, f(x) = 4


# data = np.array(
#     [
#         [1, 5],
#         [2, 7],
#         [3, 7],
#         [4, 10],
#         [5, 11],
#         [6, 14],
#         [7, 17],
#         [8, 19],
#         [9, 22],
#         [10, 28]
#     ]
# )
#
# x = data[:, 0]
# y = data[:, 1]
#
# n = len(x)
#
# w1 = 0.0
# w0 = 0.0
#
# L = 0.001
# iterations = 100_000
#
# for it in range(iterations):
#     D_w0 = 2 * sum((-y[i] + w0 + w1 * x[i]) for i in range(n))
#     D_w1 = 2 * sum(x[i] * (-y[i] + w0 + w1 * x[i]) for i in range(n))
#     w1 -= L * D_w1
#     w0 -= L * D_w0
# print(w1, w0)

# w1 = np.linspace(-10, 10, 100)
# w0 = np.linspace(-10, 10, 100)


# def E(w1, w0, x, y):
#     return sum((y[i] - (w0 + w1 * x[i])) ** 2 for i in range(len(x)))

# W1, W0 = np.meshgrid(w1, w0)
# EW = E(W1, W0, x, y)

# fig = plt.figure()
# ax = plt.axes(projection="3d")
# ax.plot_surface(W1, W0, EW)

# w1_fit = 2.4
# w0_fit = 0.8

# E_fit = E(w1_fit, w0_fit, x, y)
# ax.scatter(w1_fit, w0_fit, E_fit, color="red")

# plt.show()

# data = np.array(
#     [
#         [1, 5],
#         [2, 7],
#         [3, 7],
#         [4, 10],
#         [5, 11],
#         [6, 14],
#         [7, 17],
#         [8, 19],
#         [9, 22],
#         [10, 28]
#     ]
# )

# x = data[:, 0]
# y = data[:, 1]

# n = len(x)
#
# w1 = 0.0
# w0 = 0.0
#
# L = 0.001
#

# sample_size = 2
#
# iterations = 100_000
#
# for it in range(iterations):
#     idx = np.random.choice(n, sample_size, replace=False)
#     D_w0 = 2 * sum(-y[idx] + w0 + w1 * x[idx])
#     D_w1 = 2 * sum(x[idx] * (-y[idx] + w0 + w1 * x[idx]))
#     w1 -= L * D_w1
#     w0 -= L * D_w0
# print(w1, w0)


# data_df = pd.DataFrame(data)
# print(data_df.corr(method="pearson"))
#
# data_df[1] = data_df[1].value[::-1]
# print(data_df.corr(method="pearson"))


# X = data_df.values[:, : -1]
# Y = data_df.values[:, 1]
#
# X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=1/3)
# print(X_train)
# print(Y_train)
#
# print(X_test)
# print(Y_test)

# model = LinearRegression()
# model.fit(X_train, Y_train)

# r = model.score(X_test, Y_test)
# print(r)

# kfold = KFold(n_splits=3, random_state=1, shuffle=True) # 3-x кратная перекр. валид.
# model = LinearRegression()
# results = cross_val_score(model, X, Y, cv=kfold)
#
# print(results)
# print(results.mean(), results.std())

# data_df = pd.read_csv('multiple_independent_variable_linear.csv')
# print(data_df.head())

# X = data_df.values[:, :-1]
# Y = data_df.values[:, -1]

# model = LinearRegression().fit(X, Y)

# print(model.coef_, model.intercept_)

# x1 = X[:, 0]
# x2 = X[:, 1]
# y = Y

# fig = plt.figure()
# ax = plt.axes(projection="3d")
# ax.scatter3D(x1, x2, y)

# x1_ = np.linspace(min(x1), max(x1), 100)
# x2_ = np.linspace(min(x2), max(x2), 100)

# X1_, X2_ = np.meshgrid(x1_, x2_)
# Y = model.intercept_ +  model.coef_[0] * X1_ + model.coef_[1] * X2_

# ax.plot_surface(X1_, X2_, Y, cmap="Greys", alpha=0.1)

# plt.show()