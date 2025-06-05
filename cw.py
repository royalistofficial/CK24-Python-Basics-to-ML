import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


# x = np.linspace(0, 10, 100)
#
# fig = plt.figure()
# plt.plot(x, np.sin(x))
# plt.plot(x, np.cos(x))
#
# plt.show()

# 2 IPython
# %matplotlib
# import matplotlib.pyplot as plt
# plt.plot(...)
# plt.draw()

# 3 Jupyter
# %matplotlib inline - в блокнот добавляется статическая картинка
# %matplotlib notebook - в блокнот добавляются интерактивные графики

#fig.savefig('saved_images.png')

#print(fig.canvas.get_supported_filetypes())


# x = np.linspace(0, 10, 100)

# plt.figure()
#
# plt.subplot(2, 1, 1)
# plt.plot(x, np.sin(x))
#
# plt.subplot(2, 1, 2)
# plt.plot(x, np.cos(x))
#
# plt.show()


# fig, ax = plt.subplots(2)
# ax[0].plot(x, np.sin(x))
# ax[1].plot(x, np.cos(x))


# fig = plt.figure()
# ax = plt.axes()
#
# ax.plot(x, np.sin(x), color='blue')

# ax.plot(x, np.sin(x - 1), color='g', linestyle='solid')
# ax.plot(x, np.sin(x - 2), color='0.75', linestyle='dashed')
# ax.plot(x, np.sin(x - 3), color='#FF00EE', linestyle='dashdot')
# ax.plot(x, np.sin(x - 4), color=(1.0, 0.2, 0.3), linestyle='dotted')
# ax.plot(x, np.sin(x - 5), color='salmon')
# ax.plot(x, np.sin(x - 6), '--g')
#
# fig, ax = plt.subplots(4)
#
# ax[0].plot(x, np.sin(x))
# ax[1].plot(x, np.sin(x))
# ax[2].plot(x, np.sin(x))
# ax[3].plot(x, np.sin(x))
#
# ax[1].set_xlim(-2, 12)
# ax[1].set_ylim(-1.5, 1.5)
#
# ax[1].set_xlim(12, -2)
# ax[1].set_ylim(1.5, -1.5)
#
# ax[2].set_xlim(12, -2)
# ax[2].set_ylim(1.5, -1.5)
#
# ax[3].autoscale(tight=True)
#
# plt.subplot(3, 1, 1)
# plt.plot(x, np.sin(x))
# plt.title("Синус")
# plt.xlabel("x")
# plt.ylabel("sin(x)")
#
# plt.subplot(3, 1, 2)
# plt.plot(x, np.sin(x), '-g', label='sin(x)')
# plt.plot(x, np.cos(x), ':b', label='cos(x)')
# plt.title("Синус и косинус")
# plt.xlabel("x")
# plt.legend()
#
# plt.subplot(3, 1, 3)
# plt.plot(x, np.sin(x), '-g', label='sin(x)')
# plt.plot(x, np.cos(x), ':b', label='cos(x)')
# plt.title("Синус и косинус")
# plt.xlabel("x")
# plt.axis('equal')
# plt.legend()
#
# plt.subplots_adjust(hspace=0.5)
#
# x = np.linspace(0, 10, 30)
# plt.plot(x, np.sin(x), 'o', color='green')  # рисуются точки
# plt.plot(x, np.sin(x) + 1, '>', color='green')
# plt.plot(x, np.sin(x) + 2, '^', color='green')
# plt.plot(x, np.sin(x) + 3, 's', color='green')
#
# plt.plot(x, np.sin(x), '--p', markersize=15, linewidth=4,
#          markerfacecolor='white', markeredgecolor='gray', markeredgewidth=2)
#

# rng = np.random.default_rng(0)
# colors = rng.random(30)
# sizes = 100 * rng.random(30)
# plt.scatter(x, np.sin(x), marker='o', c=colors, s=sizes)
# plt.colorbar()

# x = np.linspace(0, 10, 50)
# dy = 0.4
# y = np.sin(x) + dy * np.random.randn(50)
#
# plt.errorbar(x, y, yerr=dy, fmt=',k')
# plt.fill_between(x, y - dy, y + dy, color='red', alpha=0.4)  # alpha - прозрачность

# def f(x, y):
#     return np.sin(x) ** 5 + np.cos(20 + x * y) * np.cos(x)
#
# x = np.linspace(0, 5, 50)
# y = np.linspace(0, 5, 40)
# X, Y = np.meshgrid(x, y)
#
# Z = f(X, Y)
# plt.contour(X, Y, Z, cmap='RdGy')
# plt.contourf(X, Y, Z, cmap='RdGy')  # заливка
# plt.colorbar()

# c = plt.contour(X, Y, Z, color='red')
# plt.clabel(c)
# plt.imshow(Z, extent=[0, 5, 0, 5], cmap='RdGy', interpolation='gaussian',
#            origin='lower', aspect='equal')
# plt.colorbar()

# plt.show()




# rng = np.random.default_rng(1)
# data = rng.normal(size=1000)

# plt.hist(data,
#          bins=30, 
#          density=True,  
#          alpha=0.5,
#          histtype='step',
#          edgecolor='red'
#          )

# x1 = rng.normal(0, 0.8, 1000)
# x2 = rng.normal(-2, 1, 1000)
# x3 = rng.normal(3, 2, 1000)

# args = dict(
#     alpha=0.3,
#     bin=40
# )

# plt.hist(x1, **args)
# plt.hist(x2, **args)
# plt.hist(x3, **args)

# print(np.histogram(x1, bins=1))
# print(np.histogram(x2, bins=2))
# print(np.histogram(x3, bins=40))

# mean = [0, 0]
# cov = [[1, 1], [1, 2]]

# x, y = rng.multivariate_normal(mean, cov, 10000).T

# plt.hist2d(x, y, bins=30)
# plt.hexbin(x, y, gridsize=30)
# cb = plt.colorbar()
# cb.set_label('Point in interval')

# print(np.histogram2d(x, y, bins=1))
# print(np.histogram2d(x, y, bins=10))


# x = np.linspace(1, 10, 1000)

# fig, ax = plt.subplots()
# y = np.sin(x[:, np.newaxis] + np.pi * np.arange(0, 2, 0.5))

# lines = plt.plot(x, y) 
# plt.legend(lines, ['1', 'второй', 'third', '4-ый'], loc='upper left')

# plt.legend(lines[:2], ['1', '2'])

# ax.plot(x, np.sin(x), label='Синус')
# ax.plot(x, np.cos(x), label='Косинус')
# ax.plot(x, np.cos(x) + 2)
# ax.axis('equal')

# ax.legend(
#     frameon=False,
#     fancybox=True,
#     shadow=True
# )

# cities = pd.read_csv('./data/california_cities.csv')

# lat, lon, pop, area = cities['latd'], cities['longd'], \
#     cities['population_total'], cities['area_total_km2']

# plt.scatter(lon, lat, c=np.log10(pop), s=area) 
# plt.xlabel('Широта')
# plt.ylabel('Долгота')
# plt.colorbar()
# plt.clim(3, 7)  

# plt.scatter([], [], c='k', alpha=0.5, s=100, label='100 $km^2$')
# plt.scatter([], [], c='k', alpha=0.5, s=300, label='300 $km^2$')
# plt.scatter([], [], c='k', alpha=0.5, s=500, label='500 $km^2$')

# plt.legend(labelspacing=3, frameon=False)


# fig, ax = plt.subplots()
# lines = []
# styles = ['-', '--', '-,', ':']
# x = np.linspace(0, 10, 1000)
# for i in range(4):
#     lines += ax.plot(
#         x,
#         np.sin(x - i + np.pi / 2),
#         styles[i]
#     )

# ax.axis('equal')
# ax.legend(lines[:2], ['line 1', 'line 2'], loc='upper right')

# leg = mpl.legend.Legend(ax, lines[1:], ['line 2', 'line 3', 'line 4'], loc='lower left')
# ax.add_artist(leg)



# x = np.linspace(0, 10, 1000)
# y = np.sin(x) * np.cos(x[:, np.newaxis])

# plt.imshow(y, cmap='binary')
# plt.imshow(y, cmap='viridis')
# plt.colorbar()

# plt.imshow(y, cmap='RdBu')
# plt.imshow(y, cmap='PuOr')
# plt.colorbar()

# plt.imshow(y, cmap='rainbow')
# plt.imshow(y, cmap='jet')

# plt.colorbar()


# plt.figure()
# plt.subplot(1, 2, 1)
# plt.imshow(y, cmap='viridis')
# plt.colorbar()

# plt.subplot(1, 2, 2)
# plt.imshow(y, cmap=plt.cm.get_cmap('viridis', 6))  
# plt.colorbar()
# plt.clim(-0.25, 0.25)


# ax1 = plt.axes()

# ax2 = plt.axes([0.4, 0.3, 0.2, 0.1])  


# fig = plt.figure()
# ax1 = fig.add_axes([0.1, 0.6, 0.8, 0.4])
# ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.4])
# ax1.plot(np.sin(x))
# ax2.plot(np.cos(x))

# fig.subplots_adjust(hspace=0.4, wspace=0.4)

# for i in range(1, 7):
#     ax = fig.add_subplot(2, 3, i)
#     ax.plot(np.sin(x + np.pi / 4 * i))

# plt.show()



from datetime import datetime

# fig, ax = plt.subplots(2, 3)
# fig, ax = plt.subplots(2, 3, sharex='col', sharey='row')
#
# for i in range(2):
#     for j in range(3):
#         ax[i, j].text(0.5, 0.5, str((i, j)), fontsize=16, ha='center')

# grid = plt.GridSpec(2, 3)

# plt.subplot(grid[:2, 0])
# plt.subplot(grid[0, 1:])  # [0, 1-2]
# plt.subplot(grid[1, 1])
# plt.subplot(grid[1, 2])


# mean = [0, 0]
# cov = [[1, 1], [1, 2]]
#
# rng = np.random.default_rng(1)
# x, y = rng.multivariate_normal(mean, cov, 3000).T
#
# fig = plt.figure()
# grid = plt.GridSpec(4, 4, hspace=0.5, wspace=0.5)
#
# main_ax = fig.add_subplot(grid[:-1, 1:])
#
# y_hist = fig.add_subplot(grid[:-1, 0], xticklabels=[], sharey=main_ax)
# x_hist = fig.add_subplot(grid[-1, 1:], yticklabels=[], sharex=main_ax)
#
# main_ax.plot(x, y, 'ok', markersize=3, alpha=0.2)
#
# y_hist.hist(y, 40, orientation='horizontal', color='gray',
#             histtype='stepfilled')
# x_hist.hist(x, 40, orientation='vertical', color='gray',
#             histtype='step')


# births = pd.read_csv('births-1969.csv')

# # births['day'] = births['day'].astype(int)
# births.index = pd.to_datetime(10000 * births.year + 100 * births.month + births.day, format='%Y%m%d')
# #print(births.head())
# births_by_date = births.pivot_table('births', [births.index.month, births.index.day])
# print(births_by_date.head())
# births_by_date.index = [
#     datetime(1969, month, day) for (month, day) in births_by_date.index
# ]
#
# fig, ax = plt.subplots()
# births_by_date.plot(ax=ax)
#
# style = dict(size=10, color='gray')
# ax.text('1969-01-01', 5500, "Новый год", **style)
# ax.text('1969-09-01', 4500, "День знаний", ha='right')
#
# ax.set(title="Рождаемость в 1969", ylabel='Число рождений')
#
# ax.xaxis.set_major_formatter(plt.NullFormatter())
# ax.xaxis.set_minor_formatter(mpl.dates.DateFormatter('%h'))
# ax.xaxis.set_minor_locator(mpl.dates.MonthLocator(bymonthday=5))


# fig = plt.figure()
# ax1 = plt.axes()

# ax2 = plt.axes([0.4, 0.3, 0.1, 0.2])
#
# ax1.set_xlim(0, 2)
# ax1.text(0.6, 0.8, "Data1 (0.6, 0.8)", transform=ax1.transData)

# ax1.text(0.6, 0.8, "Data2 (0.6, 0.8)", transform=ax2.transData)
#
# ax1.text(0.5, 0.1, "Data3 (0.5, 0.1)", transform=ax1.transAxes)
# ax1.text(0.5, 0.1, "Data4 (0.5, 0.1)", transform=ax2.transAxes)
#
# ax1.text(0.2, 0.2, "Data5 (0.2, 0.2)", transform=fig.transAxes)


# fig, ax = plt.subplots()
# x = np.linspace(0, 20, 1000)
# ax.plot(x, np.cos(x))
# ax.axis('equal')
#
# ax.annotate('Локальный максимум', xy=(6.28, 1), xytext=(10, 4), arrowprops=dict(facecolor='red'))
# ax.annotate('Локальный минимум', xy=(3.14, -1), xytext=(2, -6), arrowprops=dict(facecolor='blue', arrowstyle='->'))


# fig, ax = plt.subplots(4, 4, sharex=True, sharey=True)
# for axi in ax.flat:
#     axi.xaxis.set_major_locator(plt.MaxNLocator(5))
#     axi.yaxis.set_major_locator(plt.MaxNLocator(3))


# x = np.random.randn(1000)

# fig = plt.figure(facecolor='gray')
# ax = plt.axes(facecolor='gray')

# plt.grid(color='w', linestyle='solid')

# plt.hist(x)

# plt.show()

import seaborn as sns

# fig = plt.figure()
# ax = plt.axes(projection='3d')

# z1 = np.linspace(0, 15, 1000)
# y1 = np.cos(z1)
# x1 = np.sin(z1)
#
# #ax.plot3D(x1, y1, z1, 'green')
#
# z2 = 15 * np.random.random(100)
# y2 = np.cos(z2) + 0.1 * np.random.random(100)
# x2 = np.sin(z2) + 0.1 * np.random.random(100)

#ax.scatter3D(x2, y2, z2, c=z2, cmap='Greens')

# def f(x, y):
#     return np.sin(np.sqrt(x ** 2 + y ** 2))

# x = np.linspace(-6, 6, 30)
# y = np.linspace(-6, 6, 30)
# X, Y = np.meshgrid(x, y)
# Z = f(X, Y)

# ax.contour3D(X, Y, Z, 40, cmap='binary')
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('z')

# ax.view_init(60, 45)


# ax.plot_wireframe(X, Y, Z)


# ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
# ax.set_title('Example')

# r = np.linspace(0, 6, 20)
# theta = np.linspace(-0.9 * np.pi, 0.8 * np.pi, 40)
#
# R, Theta = np.meshgrid(r, theta)
#
# X = r * np.sin(Theta)
# Y = r * np.cos(Theta)
# Z = f(X, Y)
#
# ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')


# theta = 2 * np.pi + np.random.random(1000)
# r = 6 * np.random.random(1000)
#
# x = r * np.sin(theta)
# y = r * np.cos(theta)
# z = f(x, y)
#
# ax.scatter3D(x, y, z, c=z, cmap='viridis')
#
# ax.plot_trisurf(x, y, z, cmap='viridis')
#



# data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], size=2000)
# data = pd.DataFrame(data, columns=['x', 'y'])
#
# print(data.head())

# fig = plt.figure()
# plt.hist(data['x'], alpha=0.5)
# plt.hist(data['y'], alpha=0.5)
#

# fig = plt.figure()
# sns.kdeplot(data=data, shade=True)


# iris = sns.load_dataset('iris')
# print(iris.head())
#
# sns.pairplot(iris, hue='species', height=2.5)

# grid = sns.FacetGrid(tips, row='sex', col='day', hue='time')
# grid.map(plt.hist, "total_bill", bins=np.linspace(0, 40, 15))


#sns.catplot(data='tips', x='day', y='total_bill', kind='box')

# sns.jointplot(data=tips, x='tip', y='total_bill', kind='hex')


# planets = sns.load_dataset('planets')
# print(planets.head())
#
# sns.catplot(data=planets, x='year', kind='count', hue='method', order=range(2005, 2015))


# tips = sns.load_dataset('tips')
# print(tips.head())

# sns.pairplot(tips)


# tips_corr = tips[['total_bill', 'tip', 'size']]
# sns.heatmap(tips_corr.corr(), cmap='RdBu_r', annot=True, vmin=-1, vmax=1)

# sns.scatterplot(data=tips, x='total_bill', y='tip', hue='sex')

# sns.regplot(data=tips, x='total_bill', y='tip')
#
# sns.relplot(data=tips, x='total_bill', y='tip', hue='sex')

# sns.lineplot(data=tips, x='total_bill', y='tip')

# sns.jointplot(data=tips, x='total_bill', y='tip')


# sns.barplot(data=tips, y='total_bill', x='day', hue='sex')

# sns.pointplot(data=tips, y='total_bill', x='day', hue='sex')


# sns.boxplot(data=tips, y='total_bill', x='day')

# sns.violinplot(data=tips, y='total_bill', x='day')

# sns.stripplot(data=tips, y='total_bill', x='day')

# plt.show()