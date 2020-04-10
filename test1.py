# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time         : 2020/3/30 13:51
# @Author       : Huanhuan sun
# @Email        : sun58454006@163.com
# @File         : test1.py
# @Software     : PyCharm
# @Project      : normal

import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
from netCDF4 import Dataset
from def_store import sort_file_by_windows_rule as winsort
import cartopy.feature as cfeat
from cartopy.mpl.gridliner import LATITUDE_FORMATTER, LONGITUDE_FORMATTER
from cartopy.io.shapereader import Reader as shpreader
import matplotlib.ticker as mticker
from def_store import shp2clip
# ==============================================================================
# plt.switch_backend('Agg')       # 非交互式端口，不显示图片,QT5Agg可显示图片

# 读入数据
track = "e:/DATA/nc_data/"
extent = [70, 140, 15, 55]  # xy轴显示范围
file = winsort(track, file_style='*CN-Reanalysis-daily-2017120200*.nc')
f = Dataset(file[0])
# print(f)  # 查看f这个nc文件的信息，相当于matlab的ncdisp(f)
pm = np.squeeze(np.array(f.variables['pm25']))
so2 = np.squeeze(np.array(f.variables['so2']))
lat = np.array(f.variables['lat2d'])
lon = np.array(f.variables['lon2d'])
# 画图前的设置
fig = plt.figure(figsize=[10, 8])  # , dpi=250)  # 创建图层
proj = ccrs.PlateCarree()  # 设置投影
cmap = plt.get_cmap('jet')  # 色靶颜色方案
lev = list(range(0, pm.max().astype('int'), 10))  # 色靶值域，pm.max()为float32，不能在range中，.astype('int')转化为numpy.int格式
# ax = plt.subplot(111, projection=proj)
ax = fig.add_subplot(111, projection=proj)      #  两句都行
ax.set_global()  # 使得轴域（Axes即两条坐标轴围城的区域）适应地图的大小
# ax.coastlines()  # 画出海岸线
ax.set_extent(extent, crs=proj)  # extent这两句设置横纵坐标显示范围，等同于plt.xlim(a,b)
# xrange = list(range(60, 150, 10))     # 这里不用写xy轴标签，否则会和“绘制网格点”哪里的经纬度重合，不好看
# yrange = list(range(10, 60, 5))
# ax.set_xticks(xrange, crs=proj)       # 标注坐标轴
# ax.set_yticks(yrange, crs=proj)
lon_formatter = LongitudeFormatter(zero_direction_label=True)  # zero_direction_label=False 用来设置经度的0度加不加E和W
lat_formatter = LatitudeFormatter()
ax.xaxis.set_major_formatter(lon_formatter)
ax.yaxis.set_major_formatter(lat_formatter)  # 标注坐标轴是否加E和N，取决于两个formatter
#  加中国省界
province_territory = shpreader('d:/shp/CHN_adm0.shp')#d:/china_shp/China_provinces/China_provinces.shp')                  # cartopy中的
# province_territory = shapefile.Reader('d:/shp/bou2_4p.shp')         # shapefile中的
feature = cfeat.ShapelyFeature(province_territory.geometries(), proj,
                               edgecolor='black', facecolor='none')   #  cfeat.COLORS['land'])
ax.add_feature(feature, linewidth=1)
#  作图
pic = plt.contourf(lon, lat, pm, 15, levels=lev, cmap=cmap, extend='both')
position = fig.add_axes([0.15, 0.13, 0.7, 0.02])                      # 这里要fig——对应subplot的句柄
cbar = plt.colorbar(pic, cax=position, orientation='horizontal')
plt.tick_params(size=0, labelsize=12, gridOn=True, grid_color='white')
#  -------------白化---------------------------#
clipextent = list(range(49, 50))
clip = shp2clip(pic, ax, 'd:/shp/CHN_adm0.shp', clipextent)
#--------------白化---------------------------#

# 添加自带地形数据
# ax.stock_img()
# ----绘制网格点
gridpoint = ax.gridlines(crs=proj, draw_labels=True, linewidth=1.2, color='k', alpha=0.5, linestyle='--')
gridpoint.xlabels_top = False                           # 关闭顶端的经纬度标签
gridpoint.ylabels_right = False                         # 关闭右端的经纬度标签
gridpoint.xformatter = LONGITUDE_FORMATTER              # x轴设为经度的格式
gridpoint.yformatter = LATITUDE_FORMATTER               # y轴设为纬度的格式
gridpoint.xlocator = mticker.FixedLocator(np.arange(extent[0], extent[1]+10, 10))   # 手动设置x轴刻度
gridpoint.ylocator = mticker.FixedLocator(np.arange(extent[2], extent[3]+10, 5))    # 手动设置x轴刻度

plt.show()
# plt.savefig('e:/python_out/CN-sheng-A.png')
