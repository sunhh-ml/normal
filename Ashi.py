# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time         : 2020/3/30 13:46
# @Author       : Huanhuan sun
# @Email        : sun58454006@163.com
# @File         : Ashi.py
# @Software     : PyCharm
# @Project      : normal

from pandas import Series
import pandas
from matplotlib import pyplot
from pandas.plotting import autocorrelation_plot
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import numpy as np
from scipy import stats
import statsmodels.api as sm  # 统计相关的库
import matplotlib.pyplot as plt
from def_store import  write_matrix_to_xls

data = pandas.read_excel('d:/pm25.xlsx')
m = 52580  # 我们检验m个自相关系数

acf, q, p = sm.tsa.acf(data, nlags=m, qstat=True)  ## 计算自相关系数 及p-value
out = np.c_[range(1, m + 1), acf[1:], q, p]
output = pandas.DataFrame(out, columns=['lag', "AC", "Q", "P-value"])
output = output.set_index('lag')

temp1 = np.array(data)  # pm2.5
temp = temp1
model = sm.tsa.SARIMAX(temp)  # sm.tsa.AutoReg
results_AR = model.fit()
ar_pm = results_AR.fittedvalues
plt.figure(figsize=(10, 4))
plt.plot(temp, 'b', label='PM2.5')
plt.plot(ar_pm, 'r', label='AR model')
plt.legend()

# filepath = 'd:/我的/'
# filename = '预测.xls'
# sheetname = 'pm25'
# title = ['预测值']
# write_matrix_to_xls(ar_pm, filepath, filename, sheetname, title, row=1, col=0)



# fig = plt.figure(figsize=(20, 5))
# ax1 = fig.add_subplot(111)
# fig = sm.graphics.tsa.plot_pacf(temp, ax=ax1)
#
# pi, sin, cos = np.pi, np.sin, np.cos
# r1 = 1
# theta = np.linspace(0, 2 * pi, 360)
# x1 = r1 * cos(theta)
# y1 = r1 * sin(theta)
# plt.figure(figsize=(6, 6))
# plt.plot(x1, y1, 'k')  # 画单位圆
# roots = 1 / results_AR.arroots  # 注意，这里results_AR.roots 是计算的特征方程的解，特征根应该取倒数
# for i in range(len(roots)):
#     plt.plot(roots[i].real, roots[i].imag, '.r', markersize=8)  # 画特征根
# plt.show()



#
# fig = plt.figure(figsize=(20, 5))
# ax1 = fig.add_subplot(111)
# fig = sm.graphics.tsa.plot_pacf(temp, ax=ax1)
#
# aicList = []
# bicList = []
# hqicList = []
# for i in range(1, 11):  # 从1阶开始算
#     order = (i, 0)  # 这里使用了ARMA模型，order 代表了模型的(p,q)值，我们令q始终为0，就只考虑了AR情况。
#     tempModel = sm.tsa.ARMA(temp, order).fit()
#     aicList.append(tempModel.aic)
#     bicList.append(tempModel.bic)
#     hqicList.append(tempModel.hqic)
#
# plt.figure(figsize=(15, 6))
# plt.plot(aicList, 'r', label='aic value')
# plt.plot(bicList, 'b', label='bic value')
# plt.plot(hqicList, 'k', label='hqic value')
# plt.legend(loc=0)

# series = pandas.read_excel('d:/pm25.xlsx')
# autocorrelation_plot(series)
# plot_acf(series)
# plot_pacf(series)
# pyplot.show()
