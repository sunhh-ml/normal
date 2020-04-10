# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time         : 2020/3/30 13:47
# @Author       : Huanhuan sun
# @Email        : sun58454006@163.com
# @File         : colouring_map.py
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

if __name__ == '__main__':
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
    fig = plt.figure(figsize=[10, 8])  # , dpi=350)  # 创建图层
    proj = ccrs.PlateCarree()  # 设置投影
    cmap = plt.get_cmap('jet')  # 色靶颜色方案
    lev = list(range(0, pm.max().astype('int'), 10))  # 色靶值域，pm.max()为float32，不能在range中，.astype('int')转化为numpy.int格式
    ax = plt.subplot(111, projection=proj)
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.title(r'中国地区 PM${_2}{_.}{_5}$', fontdict=(dict(fontsize=24)))  # 图名

    # ax = fig.add_subplot(111, projection=proj)      #  两句都行
    ax.set_global()  # 使得轴域（Axes即两条坐标轴围城的区域）适应地图的大小
    # ax.coastlines()  # 画出海岸线
    ax.set_extent(extent, crs=proj)  # extent这两句设置横纵坐标显示范围，等同于plt.xlim(a,b)
    # ----------xy轴标签设置部分，由于绘制网格点哪里同样有xy轴设置，所以这里可忽略
    # xrange = list(range(60, 150, 10))     # 这里不用写xy轴标签，否则会和“绘制网格点”哪里的经纬度重合，不好看
    # yrange = list(range(10, 60, 5))
    # ax.set_xticks(xrange, crs=proj)       # 标注坐标轴
    # ax.set_yticks(yrange, crs=proj)
    # lon_formatter = LongitudeFormatter(zero_direction_label=True)  # zero_direction_label=False 用来设置经度的0度加不加E和W
    # lat_formatter = LatitudeFormatter()
    # ax.xaxis.set_major_formatter(lon_formatter)
    # ax.yaxis.set_major_formatter(lat_formatter)  # 标注坐标轴是否加E和N，取决于两个formatter
    # ----------xy轴标签设置部分，由于绘制网格点哪里同样有xy轴设置，所以这里可忽略

    #  加中国省界
    province_territory = shpreader('d:/shp/CHN_adm0.shp')  # cartopy中的
    # province_territory = shapefile.Reader('d:/shp/bou2_4p.shp')         # shapefile中的
    feature = cfeat.ShapelyFeature(province_territory.geometries(), proj,
                                   edgecolor='black', facecolor='none')  # cfeat.COLORS['land'])
    ax.add_feature(feature, linewidth=1)
    #  作图
    pic = plt.contourf(lon, lat, pm, 15, levels=lev, cmap=cmap, extend='both')
    position = fig.add_axes([0.91, 0.17, 0.012, 0.65])  # 这里要fig——对应subplot的句柄
    cbar = plt.colorbar(pic, cax=position, orientation='vertical')  # vertical    horizontal
    plt.tick_params(size=0, labelsize=12, gridOn=True, grid_color='white')
    cbar.set_label(r'${\mu}g/m{^3}$')

    #  -------------白化---------------------------#
    clipextent = list(range(49, 50))
    clip = shp2clip(pic, ax, 'd:/shp/CHN_adm0.shp', clipextent)
    # 添加自带地形数据
    # ax.stock_img()
    # ----绘制网格点
    gridpoint = ax.gridlines(crs=proj, draw_labels=True, linewidth=1.2, color='k', alpha=0.5, linestyle='--')
    gridpoint.xlabels_top = False  # 关闭顶端的经纬度标签
    gridpoint.ylabels_right = False  # 关闭右端的经纬度标签
    gridpoint.xformatter = LONGITUDE_FORMATTER  # x轴设为经度的格式
    gridpoint.yformatter = LATITUDE_FORMATTER  # y轴设为纬度的格式
    gridpoint.xlocator = mticker.FixedLocator(np.arange(extent[0], extent[1] + 10, 10))  # 手动设置x轴刻度
    gridpoint.ylocator = mticker.FixedLocator(np.arange(extent[2], extent[3] + 10, 5))  # 手动设置x轴刻度

    # 南海小框
    sub_ax = fig.add_axes([0.77, 0.175, 0.12, 0.2])  # 就这样的时候，南海方框刚刚好
    # sub_ax = plt.axes([0.77, 0.175, 0.12, 0.2])
    # sub_feature = cfeat.ShapelyFeature(province_territory.geometries(), proj,
    #                                edgecolor='black', facecolor='none')   #  cfeat.COLORS['land'])
    # sub_ax.set_feature(sub_feature, linewidth=1)
    # sub_ax.get_feature(sub_feature, linewidth=1)
    # sub_ax.set_xticks([])
    # sub_ax.set_yticks([])
    # sub_ax.xaxis.set_major_formatter([])
    # sub_ax.xaxis.set_major_formatter([])
    plt.show()
    plt.savefig('e:/python_out/CHN_adm0.png', dpi=120)# , bbox_inches='tight')  # bbox命令会提示回调异常，但不影响保存结果
