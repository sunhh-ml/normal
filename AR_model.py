# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time         : 2020/3/30 13:45
# @Author       : Huanhuan sun
# @Email        : sun58454006@163.com
# @File         : AR_model.py
# @Software     : PyCharm
# @Project      : normal

import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import matplotlib as mpl
import itertools
import warnings
import numpy as np
from statsmodels.tsa.stattools import adfuller
from statsmodels.stats.diagnostic import unitroot_adf, acorr_ljungbox
import xlwt
from def_store import write_matrix_to_xls

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

filepath = 'd:/'
filename = '预测.xls'
sheetname = 'pm25'

# 读取数据，指定或设置日期列的格式为Datetime格式
# df = pd.read_excel('d:/pm25.xlsx', encoding='utf-8')
# df.index = pd.to_datetime(df.index, unit='D', yearfirst=True, origin=pd.Timestamp('2013-1-1'))     # 将字符串索引转换成时间索引
df = pd.read_excel('d:/pm25 - 副本.xlsx', sheet_name=1, index_col='date', freq='D')  # 自动将date列识别为Datetime格式
data = df['精简']
f_data = data.values  # data为series/DataFrame时，data.values或是np.array(data)可以将data转化为ndarray
# adata = f_data.reshape(20, 3, 2)
idx = np.array(np.where(np.isnan(f_data)))  # 找到nan的位置(此时为tuple,无索引)，转化为ndarray，在转化为list(tuple不能直接转list)
idx = idx.tolist()
idx = idx[0]
idx.append(idx[-1])
id = []
for i in range(len(idx)-1):
    if idx[i]+1 != idx[i+1]:
        id.append(idx[i])
adata = []
id.append(id[-1])
j = 0
for i in range(len(id)-1):
    if i == 0:
        adata.append(f_data[0:idx[i]+1])
    else:
        adata.append(f_data[idx[j]+1:idx[i]+1])
    j = i







# 确定缺少值（nan 和 inf）
# data = data.fillna(data.bfill())  # 在填补nan或inf之前，用前一天的代替，ffill为后一天的代替
#
# # 自相关——————相关则可以用AR预测，不相关则不能
# sm.graphics.tsa.plot_acf(data).show()  # 自相关系数图，长期相关系数大于0，表明相关，且p从截尾n起
# # sm.graphics.tsa.plot_pacf(data).show()
#
# # 平稳性检验————————扩展迪基福勒检验，判断adf（单位根）t值是否小于critical values和p值是否小于0.05(0.01)，大于则不平稳
# adf = adfuller(data)  # 返回值依次为adf的tvalue、pvalue、usedlag、nobs、critical values、icbest、regresults、resstore
#
# # 不平稳序列平稳化————————通常为差分法
# D_data = data.diff().dropna()  # 一阶差分，第一个数肯定是nan，丢弃它
# D_data.columns = [u'一阶差分后数据']  # 更改列名
# diff_adf = adfuller(D_data)
#
# # 对n阶差分后序列做白噪音检验
# print(u'差分序列的白噪声检验结果为：', acorr_ljungbox(D_data, lags=1))  # 返回统计量和p值，p值远小于0.05，所以n阶差分之后序列为平稳非白噪音序列
#
# sm.graphics.tsa.plot_acf(D_data).show()  # 自相关系数图，长期相关系数大于0，表明相关，且p从截尾n起
#
# # 相对最优模型
# # data[u'一阶差分后数据'] = data[u'一阶差分后数据'].astype(float)  # Series转为float类型
# # 定阶
# pmax = int(len(D_data) / 10)  # 一般阶数不超过length/10
# qmax = int(len(D_data) / 10)  # 一般阶数不超过length/10
# bic_matrix = []  # bic矩阵
# for p in range(pmax + 1):
#     tmp = []
#     for q in range(qmax + 1):
#         try:  # 存在部分报错，所以用try来跳过报错。
#             tmp.append(sm.tsa.ARIMA(data, (p, 1, q)).fit().bic)         # 1阶差分后为平稳序列
#         except:
#             tmp.append(None)
#     bic_matrix.append(tmp)
#
# bic_matrix = pd.DataFrame(bic_matrix)  # 从中可以找出最小值
#
# p, q = bic_matrix.stack().idxmin()  # 先用stack展平，然后用idxmin找出最小值位置。
# print(u'BIC最小的p值和q值为：%s、%s' % (p, q))
#
# # BIC最小的p值和q值为：0、1
# model = sm.tsa.ARIMA(data, (p, 1, q)).fit()  # 建立ARIMA(0, 1, 1)模型
# model.summary2()  # 给出一份模型报告
#
# f_data = model.forecast(15)[0]      # forecast返回预测值，置信水平以及误差区间


# filepath = 'd:/我的/'
# filename = '预测.xls'
# sheetname = 'pm25'
# title = ['预测值', '没有了1', '没有了2', '没有了3', '没有了4', '没有了5', '没有了6']
# write_matrix_to_xls(adata, filepath, filename, sheetname, title, row=1, col=3)


# y = df.pm25
# y = y.fillna(y.bfill())
# ar_data = y[0:120]
# # y.plot(figsize=(15, 6))
# # plt.show()
#
# # Define the p, d and q parameters to take any value between 0 and 2
# p = d = q = range(0, 2)
#
# # Generate all different combinations of p, q and q triplets
# pdq = list(itertools.product(p, d, q))
#
# # Generate all different combinations of seasonal p, q and q triplets
# seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]       # 12季节参数，1年12个月
#
# print('Examples of parameter combinations for Seasonal ARIMA...')
# print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
# print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
# print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
# print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))
#
# warnings.filterwarnings("ignore")  # specify to ignore warning messages
#
# ar_aic_param_seasonal = []
#
# for param in pdq:
#     for param_seasonal in seasonal_pdq:
#         try:
#             mod = sm.tsa.statespace.SARIMAX(ar_data,
#                                             order=param,
#                                             seasonal_order=param_seasonal,
#                                             enforce_stationarity=False,
#                                             enforce_invertibility=False)
#             results = mod.fit()
#             ar_aic_param_seasonal.append([param, param_seasonal, results.aic])
#             # print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
#         except:
#             continue
# print('==========================================')
# mod = sm.tsa.statespace.SARIMAX(ar_data,
#                                 order=(1, 1, 1),
#                                 seasonal_order=(0, 1, 1, 12),
#                                 enforce_stationarity=False,
#                                 enforce_invertibility=False)
# results = mod.fit()
# print(results.summary().tables[1])  # 详细输出，results.summary()可以输出全部的模型计算参数表
#
# results.plot_diagnostics(figsize=(15, 12))
# plt.show()
#
# # pred = results.get_prediction(start=pd.to_datetime('2013/3/1'), dynamic=False)#预测值
# # pred_ci = pred.conf_int()#置信区间
