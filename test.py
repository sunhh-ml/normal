# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time         : 2020/3/30 13:51
# @Author       : Huanhuan sun
# @Email        : sun58454006@163.com
# @File         : test.py
# @Software     : PyCharm
# @Project      : normal

from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
import os,sys
import matplotlib as mplot
import xarray as xr
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from copy import copy
from cartopy.mpl.gridliner import LATITUDE_FORMATTER, LONGITUDE_FORMATTER
import shapely.geometry as sgeom
from def_store import sort_file_by_windows_rule as winsort
import test1


# plt.switch_backend('Agg')       # 非交互式端口，不显示图片,QT5Agg可显示图片
# 设置图框
proj = ccrs.LambertConformal(central_longitude=105, central_latitude=90,
                             false_easting=400000, false_northing=400000)   # ,standard_parallels=(46, 49))
fig = plt.figure(figsize=[10, 8], frameon=True)
# 设置投影和主图格式
ax = fig.add_axes([0.08, 0.05, 0.8, 0.94], projection=proj)
# 设置图片范围
ax.set_extent([80, 130, 15, 55], crs=ccrs.PlateCarree())
ax.set_title('China', fontsize=20)  # 例子中这行注释掉了
# 画边界

# Add ocean, land, rivers and lakes
ax.add_feature(cfeature.OCEAN.with_scale('50m'))
ax.add_feature(cfeature.LAND.with_scale('50m'))
ax.add_feature(cfeature.RIVERS.with_scale('50m'))
ax.add_feature(cfeature.LAKES.with_scale('50m'))
# *必须*调用draw以获取用于添加记号的轴边界
fig.canvas.draw()
# 定义网格线位置并使用cartopy的内置网格线绘制线
xticks = [55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165]
yticks = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
ax.gridlines(xlocs=xticks, ylocs=yticks, linestyle='--', lw=1, color='dimgrey')
# 使用自定义记号标记器标记网格线的端点
ax.xaxis.set_major_formatter(LONGITUDE_FORMATTER)
ax.yaxis.set_major_formatter(LATITUDE_FORMATTER)
# def
test1.lambert_xticks(ax, xticks)
test1.lambert_yticks(ax, yticks)
# 以子图形式画南海区域
sub_ax = fig.add_axes([0.592, 0.189, 0.14, 0.155], projection=ccrs.LambertConformal(
    central_latitude=90, central_longitude=115))
sub_ax.add_feature(cfeature.OCEAN.with_scale('50m'))
sub_ax.add_feature(cfeature.LAND.with_scale('50m'))
sub_ax.add_feature(cfeature.RIVERS.with_scale('50m'))
sub_ax.add_feature(cfeature.LAKES.with_scale('50m'))
# 画子图的边界

# 设置子图的范围
sub_ax.set_extent([105, 125, 0, 25], crs=ccrs.PlateCarree())
# 作图所用数据
track = "e:/DATA/nc_data/"
file = winsort(track, file_style='*CN-Reanalysis-daily-2017120200*.nc')
q = Dataset(file[0])
longitude = np.array(q.variables['lon2d'])
latitude = np.array(q.variables['lat2d'])
lad = np.squeeze(np.array(q.variables['pm25']))

# 区域选择
lon_range = longitude[(longitude>60) & (longitude<150)]
lat_range = latitude[(latitude>10) & (latitude<60)]
temp_region = temp.sel(longitude=lon_range, latitude=lat_range,time='2017-12-03')
temp_mask = mask(temp_region, 'ocean')






# fig = plt.contourf(longitude, latitude, lad, cmap='jet', norm=mplot.colors.Normalize(vmin=0, vmax=400))
# cbar = plt.colorbar(fig)
# plt.xlim(60, 140)
# plt.ylim(15, 55)




plt.show()

# plt.savefig('e:/python_out/test.png')
