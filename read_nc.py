# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time         : 2020/3/30 13:49
# @Author       : Huanhuan sun
# @Email        : sun58454006@163.com
# @File         : read_nc.py
# @Software     : PyCharm
# @Project      : normal

import netCDF4 as nc
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap,cm
import numpy as np

data=nc.Dataset('d:\\201301.nc')    # 要\\
print(data)     # 查看nc文件有啥东西
print('------------------')


print(data.variables.keys())    # 查看nc文件中的变量
for i in data.variables.keys(): # 后面一定要有冒号，没有就错
    print(i)                    # 显示变量名称
   # print(df.variables[i])    # 显示变量详细 或者 直接用 print(df.variables['lon2d'])
    print(data.variables[i].ncattrs())  # 查看每个变量的属性
    # print(df.variables[i]._Fillvalue)   # 报错，可能是该nc文件没fillvalue属性
    # print(df.variables['lon2d'].units)    # 报错，有ncattrs显示lon2d输出为[]
    # print(df.variables[i].units)
    print('===============')
lat=(data.variables['lat2d'][:])    # ()加不加没关系
lon=data.variables['lon2d'][:]
pm25=data.variables['pm25'][:]

#--------------作图---------------------------#
m=Basemap(resolution='l',area_thresh=10000,projection='cyl',llcrnrlon=50,urcrnrlon=150,llcrnrlat=0,urcrnrlat=70)
fig1 = plt.figure()
ax = fig1.add_axes([0.1, 0.1, 0.8, 0.8])
# clevls_hgt=[-80,-60,-40,-20,0,20,40,60,80]
x, y = m(lon, lat)
m.drawparallels(np.arange(0, 70, 10.), labels=[1, 1, 0, 0], fontsize=15)
m.drawmeridians(np.arange(50, 150, 20), labels=[0, 0, 0, 1], fontsize=15)
# curve=m.contour(lon_province_territory,lat_province_territory,u[0,:,:],colors='k')
CS2 = m.contourf(x, y, u[0, :, :])
m.colorbar(CS2)
m.drawcoastlines(linewidth=0.2)
plt.title('U', size=20)

plt.show()