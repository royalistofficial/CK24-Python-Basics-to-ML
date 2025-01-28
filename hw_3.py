import numpy as np
import pandas as pd

rnd = np.random.default_rng()

# 1. Привести различные способы создания объектов типа Series
# Для создания Series можно использовать
# - списки Python или массивы NumPy
# - скалярные значение
# - словари

# s1 = pd.Series([1, 2, 3, 4, 5])
# s2 = pd.Series(np.array([1, 2, 3, 4, 5]))
# s3 = pd.Series(5, index=[0, 1, 2, 3, 4])
# s4 = pd.Series({'a': 1, 'b': 2, 'c': 3})

# 2. Привести различные способы создания объектов типа DataFrame
# DataFrame. Способы создания
# - через объекты Series
# - списки словарей
# - словари объектов Series
# - двумерный массив NumPy
# - структурированный массив Numpy


# s1 = pd.Series([0.25, 0.5, 0.75, 1.0])
# s2 = pd.Series([0.25, 0.5, 0.75, 1.0])
# df1 = pd.DataFrame({'A': s1, 'B': s2})

# data2 = [{'A': 1, 'B': 4}, {'A': 2, 'B': 5}, {'A': 3, 'B': 6}]
# df2 = pd.DataFrame(data2)

# s3 = pd.Series([0.25, 0.5, 0.75, 1.0])
# s4 = pd.Series([0.25, 0.5, 0.75, 1.0])
# data3 = {'A': s3, 'B': s4}
# df3 = pd.DataFrame(data3)

# data4 = np.array([[1, 1], [1, 1], [1, 1]])
# df4 = pd.DataFrame(data4, columns=['A', 'B'])

# data5 = np.array([(1, 1), (1, 1), (1, 1)], dtype=[('A', int), ('B', int)])
# df5 = pd.DataFrame(data5)


# 3. Объедините два объекта Series с неодинаковыми множествами ключей
# (индексов) так, чтобы вместо NaN было установлено значение 1


# s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
# s2 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'd', 'e'])


# print(s1.combine_first(s2).fillna(1))

# 4. Переписать пример с транслирование для DataFrame так, чтобы вычитание
# происходило по СТОЛБЦАМ

# df = pd.DataFrame(rnd.integers(0, 10, (3, 4)), columns=['a', 'b', 'c', 'd'])

# print(df.T.iloc[0])

# print((df.T - df.T.iloc[0]).T)

# 5. На примере объектов DataFrame продемонстрируйте использование методов
# ffill() и bfill()

# dfA = pd.DataFrame({'a': [1, np.nan, 3, np.nan, 5],
#                     'b': [np.nan, 2, np.nan, 4, np.nan]})

# print(dfA.ffill())
# print(dfA.bfill())



















# series, DAtaframe, Index


# data = pd.Series([0.25, 0.5, 0.75, 1.0])


# print(data)
# print(type(data))

# print(data.values)
# print(type(data.values))

# print(data.index)
# print(type(data.index))


# data = pd.Series([0.25, 0.5, 0.75, 1.0])

# print(data[0])
# print(data[1:3])

# data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
# print(data)
# print(data['a'])
# print(data['b':'d'])

# print(data.index)

# data = pd.Series([0.25, 0.5, 0.75, 1.0], index=[1, 10, 7, 'd'])

# print(data)
# print(data[1])
# print(data[10:'d'])


# population_dict = {
#     "city_1": 1001,
#     "city_2": 1002,
#     "city_3": 1003,
#     "city_4": 1004,
#     "city_5": 1005,
# }

# population = pd.Series(population_dict)
# print(population)

# print(population['city_4'])
# print(population['city_4':'city_5'])


# population_dict = {
#     "city_1": 1001,
#     "city_2": 1002,
#     "city_3": 1003,
#     "city_4": 1004,
#     "city_5": 1005,
# }

# area_dict = {
#     "city_1": 9991,
#     "city_2": 9992,
#     "city_3": 9993,
#     "city_4": 9994,
#     "city_5": 9995,
# }


# population = pd.Series(population_dict)

# area = pd.Series(area_dict)

# print(population)
# print(area)

# states = p
#     'population1': population,
#     'area1': area
# })

# print(states)


# print(states.values)
# print(states.index)
# print(states.columns)


# print(type(states.values))
# print(type(states.index))
# print(type(states.columns))


# print(states['area1'])

# ind = pd.Index([2, 3, 5, 7, 11])
# print(ind[1])
# print(ind[::2])

# indA = pd.Index([1, 2, 3, 4, 5])
# indB = pd.Index([1, 2, 3, 4, 6])

# print(indA.intersection(indB))


# data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
# print('a' in data)
# print('z' in data)

# print(data.keys())
# print(list(data.items()))

# data['a'] = 100
# data['z'] = 1000


# print(data)


# data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])

# print(data['a':'c'])

# print(data[0:2])

# print(data[(data > 0.5) & (data < 1)])


# data = pd.Series([0.25, 0.5, 0.75, 1.0], index=[1, 3, 5, 10])

# print(data[1])

# print(data.loc[1])
# print(data.iloc[1])

# pop = pd.Series({
#     "city_1": 1001,
#     "city_2": 1002,
#     "city_3": 1003,
#     "city_4": 1004,
#     "city_5": 1005,
# })

# area = pd.Series({
#     "city_1": 9991,
#     "city_2": 9992,
#     "city_3": 9993,
#     "city_4": 9994,
#     "city_5": 9995,
# })

# data = pd.DataFrame({
#     'pop': pop,
#     'pop1': pop,
#     'area': area
# })


# print(data)

# print(data['area'])

# print(data.area)

# print(data.pop is data['pop'])
# print(data.pop1 is data['pop1'])

# data['new'] = data['area']

# data['new1'] = data['area'] / data['pop1']


# print(data)


# pop = pd.Series({
#     "city_1": 1001,
#     "city_2": 1002,
#     "city_3": 1003,
#     "city_4": 1004,
#     "city_5": 1005,
# })

# area = pd.Series({
#     "city_1": 9991,
#     "city_2": 9992,
#     "city_3": 9993,
#     "city_4": 9994,
#     "city_5": 9995,
# })

# data = pd.DataFrame({
#     'pop': pop,
#     'pop1': pop,
#     'area': area
# })

# print(data)
# print(data.values)
# print(data.T)


# print(data['area'])
# print(data.values[0:2])

# print(data)
# print(data.iloc[:3, 1:2])
# print(data.loc['city_4', 'pop1': 'pop'])


# rnd = np.random.default_rng()
# s = pd.Series(rnd.integers(0, 10, 4))

# print(s)

# print(np.exp(s))


# pop = pd.Series({
#     "city_1": 1001,
#     "city_2": 1002,
#     "city_3": 1003,
#     "city_4": 1004,
#     "city_5": 1005,
# })

# area = pd.Series({
#     "city_1": 9991,
#     "city_2": 9992,
#     "city_3": 9993,
#     "city_4": 9994,
#     "city_5": 9995,
# })

# data = pd.DataFrame({
#     'pop': pop,
#     'area': area
# })

# print(data)


# dfA = pd.DataFrame(rnd.integers(0, 10, (2, 2)), columns=['a', 'b'])
# dfB = pd.DataFrame(rnd.integers(0, 10, (3, 3)), columns=['a', 'b', 'c'])

# print(dfA)
# print(dfB)

# print(dfA + dfB)

# A = rnd.integers(0, 10, (3, 4))
# print(A)
# print(A[0])
# print(A - A[0])

# df = pd.DataFrame(A, columns=['a', 'b', 'c', 'd'])
# print(df)

# print(df.iloc[0])

# print(df - df.iloc[0])

# print(df.iloc[0, ::2])

# print(df - df.iloc[0, ::2])


# val1 = np.array([1, 2, 3])

# print(val1.sum())

# val1 = np.array([1, None, 2, 3])

# print(val1.sum())


# val1 = np.array([1, np.nan, 2, 3])

# print(val1.sum())
# print(np.sum(val1))
# print(np.nansum(val1))


# x = pd.Series(range(10), dtype=int)
# print(x)
# x[0] = None
# x[1] = np.nan

# print(x)


# x1 = pd.Series(['a', 'b', 'c'])

# print(x1)

# x1[0] = None
# x1[1] = np.nan

# print(x1)


# x2 = pd.Series([1, 2, 3, np.nan, None, pd.NA])
# print(x2)


# x3 = pd.Series([1, 2, 3, np.nan, None, pd.NA], dtype='Int32')
# print(x3)
# print(x3.isnull())
# print(x3[x3.isnull()])

# print(x3.dropna())


# df = pd.DataFrame([
#     [1, 2, np.nan, 4, 5, 6],
#     [1, 2, None, None, 5, 6],
#     [1, None, None, 4, 5, 6],
# ])

# print(df)

# print(df.dropna())
# print(df.dropna(axis=1, how='all'))
# print(df.dropna(axis=1, how='any'))
# print(df.dropna(axis=1, thresh=2))