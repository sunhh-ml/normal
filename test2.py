# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time         : 2020/3/30 13:51
# @Author       : Huanhuan sun
# @Email        : sun58454006@163.com
# @File         : test2.py
# @Software     : PyCharm
# @Project      : normal

# import numpy as np
# import matplotlib.pyplot as plt
# import cartopy.crs as ccrs
# from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
# from netCDF4 import Dataset
# from def_store import sort_file_by_windows_rule as winsort
# import cartopy.feature as cfeat
# from cartopy.mpl.gridliner import LATITUDE_FORMATTER, LONGITUDE_FORMATTER
# from cartopy.io.shapereader import Reader as shpreader
# import matplotlib.ticker as mticker
# from def_store import shp2clip
# import shapely.geometry as sgeom


# track = "e:/DATA/nc_data/"
# extent = [60, 150, 10, 55]  # xy轴显示范围
# file = winsort(track, file_style='*CN-Reanalysis-daily-2017120200*.nc')
# f = Dataset(file[0])
# print(f)  # 查看f这个nc文件的信息，相当于matlab的ncdisp(f)
# pm = np.squeeze(np.array(f.variables['pm25']))
# so2 = np.squeeze(np.array(f.variables['so2']))
# lat = np.array(f.variables['lat2d'])
# lon = np.array(f.variables['lon2d'])
## 画图前的设置
# fig = plt.figure(figsize=[10, 8])  # , dpi=350)  # 创建图层
# proj = ccrs.PlateCarree()  # 设置投影
# cmap = plt.get_cmap('jet')  # 色靶颜色方案
# lev = list(range(0, pm.max().astype('int'), 10))  # 色靶值域，pm.max()为float32，不能在range中，.astype('int')转化为numpy.int格式
# ax = plt.subplot(111, projection=proj)
# # ax = fig.add_subplot(111, projection=proj)      #  两句都行
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
# plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# plt.title(r'中国地区 PM${_2}{_.}{_5}$', fontdict=(dict(fontsize=24)))  # 图名
#
# ax.set_global()  # 使得轴域（Axes即两条坐标轴围城的区域）适应地图的大小
# # ax.coastlines()  # 画出海岸线
# ax.set_extent(extent, crs=proj)  # extent这两句设置横纵坐标显示范围，等同于plt.xlim(a,b)
# # ----------xy轴标签设置部分，由于绘制网格点哪里同样有xy轴设置，所以这里可忽略
# xrange = list(range(60, 150, 10))     # 这里不用写xy轴标签，否则会和“绘制网格点”哪里的经纬度重合，不好看
# yrange = list(range(10, 60, 5))
# ax.set_xticks(xrange, crs=proj)       # 标注坐标轴
# ax.set_yticks(yrange, crs=proj)
# lon_formatter = LongitudeFormatter(zero_direction_label=True)  # zero_direction_label=False 用来设置经度的0度加不加E和W
# lat_formatter = LatitudeFormatter()
# ax.xaxis.set_major_formatter(lon_formatter)
# ax.yaxis.set_major_formatter(lat_formatter)  # 标注坐标轴是否加E和N，取决于两个formatter
# # ----------xy轴标签设置部分，由于绘制网格点哪里同样有xy轴设置，所以这里可忽略
#
# #  加中国省界
# province_territory = shpreader('d:/shp/CHN_adm0.shp')  # cartopy中的
# # province_territory = shapefile.Reader('d:/shp/bou2_4p.shp')         # shapefile中的
# feature = cfeat.ShapelyFeature(province_territory.geometries(), proj,
#                                edgecolor='black', facecolor='none')  # cfeat.COLORS['land'])
# ax.add_feature(feature, linewidth=1)
# #  作图
# pic = plt.contourf(lon, lat, pm, 15, levels=lev, cmap=cmap, extend='both')
# position = fig.add_axes([0.91, 0.17, 0.012, 0.65])  # 这里要fig——对应subplot的句柄
# cbar = plt.colorbar(pic, cax=position, orientation='vertical')  # vertical    horizontal
# plt.tick_params(size=0, labelsize=12, gridOn=True, grid_color='white')
# cbar.set_label(r'${\mu}g/m{^3}$')
#
# #  -------------白化---------------------------#
# clipextent = list(range(49, 50))
# clip = shp2clip(pic, ax, 'd:/shp/CHN_adm0.shp', clipextent)
# 添加自带地形数据
# ax.stock_img()
## ----绘制网格点
# gridpoint = ax.gridlines(crs=proj, draw_labels=True, linewidth=1.2, color='k', alpha=0.5, linestyle='--')
# gridpoint.xlabels_top = False  # 关闭顶端的经纬度标签
# gridpoint.ylabels_right = False  # 关闭右端的经纬度标签
# gridpoint.xformatter = LONGITUDE_FORMATTER  # x轴设为经度的格式
# gridpoint.yformatter = LATITUDE_FORMATTER  # y轴设为纬度的格式
# gridpoint.xlocator = mticker.FixedLocator(np.arange(extent[0], extent[1] + 10, 10))  # 手动设置x轴刻度
# gridpoint.ylocator = mticker.FixedLocator(np.arange(extent[2], extent[3] + 10, 5))  # 手动设置x轴刻度

## 南海小框
## sub_ax = fig.add_axes([0.77, 0.175, 0.12, 0.2])  # 就这样的时候，南海方框刚刚好
## sub_ax = plt.axes([0.77, 0.175, 0.12, 0.2])
## sub_feature = cfeat.ShapelyFeature(province_territory.geometries(), proj,
##                                edgecolor='black', facecolor='none')   #  cfeat.COLORS['land'])
## sub_ax.set_feature(sub_feature, linewidth=1)
## sub_ax.get_feature(sub_feature, linewidth=1)
## sub_ax.set_xticks([])
## sub_ax.set_yticks([])
## sub_ax.xaxis.set_major_formatter([])
## sub_ax.xaxis.set_major_formatter([])
# plt.show()
## plt.savefig('e:/python_out/CHN_adm0.png', dpi=120)# , bbox_inches='tight')  # bbox命令会提示回调异常，但不影响保存结果


from copy import copy
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from netCDF4 import Dataset
from def_store import sort_file_by_windows_rule as winsort
import cartopy.feature as cfeat
from cartopy.mpl.gridliner import LATITUDE_FORMATTER, LONGITUDE_FORMATTER
from cartopy.io.shapereader import Reader as shpreader
import shapely.geometry as sgeom


track = "e:/DATA/nc_data/"
extent = [80, 133, 15, 53]  # xy轴显示范围
file = winsort(track, file_style='*CN-Reanalysis-daily-2017120200*.nc')
f = Dataset(file[0])
# print(f)  # 查看f这个nc文件的信息，相当于matlab的ncdisp(f)
pm = np.squeeze(np.array(f.variables['pm25']))
so2 = np.squeeze(np.array(f.variables['so2']))
lat = np.array(f.variables['lat2d'])
lon = np.array(f.variables['lon2d'])
## 画图前的设置
# fig = plt.figure(figsize=[10, 8])  # , dpi=350)  # 创建图层
# proj = ccrs.PlateCarree()  # 设置投影
cmap = plt.get_cmap('jet')  # 色靶颜色方案
lev = list(range(0, pm.max().astype('int')+10, 10))  # 色靶值域，pm.max()为float32，不能在range中，.astype('int')转化为numpy.int格式

def find_side(ls, side):
    """
 Given a shapely LineString which is assumed to be rectangular, return the
 line corresponding to a given side of the rectangle.

 """
    minx, miny, maxx, maxy = ls.bounds
    points = {'left': [(minx, miny), (minx, maxy)],
              'right': [(maxx, miny), (maxx, maxy)],
              'bottom': [(minx, miny), (maxx, miny)],
              'top': [(minx, maxy), (maxx, maxy)], }
    return sgeom.LineString(points[side])


def lambert_xticks(ax, ticks):
    """Draw ticks on the bottom x-axis of a Lambert Conformal projection."""
    te = lambda xy: xy[0]
    lc = lambda t, n, b: np.vstack((np.zeros(n) + t, np.linspace(b[2], b[3], n))).T
    xticks, xticklabels = _lambert_ticks(ax, ticks, 'bottom', lc, te)
    ax.xaxis.tick_bottom()
    ax.set_xticks(xticks)
    ax.set_xticklabels([ax.xaxis.get_major_formatter()(xtick) for xtick in xticklabels])


def lambert_yticks(ax, ticks):
    """Draw ricks on the left y-axis of a Lamber Conformal projection."""
    te = lambda xy: xy[1]
    lc = lambda t, n, b: np.vstack((np.linspace(b[0], b[1], n), np.zeros(n) + t)).T
    yticks, yticklabels = _lambert_ticks(ax, ticks, 'left', lc, te)
    ax.yaxis.tick_left()
    ax.set_yticks(yticks)
    ax.set_yticklabels([ax.yaxis.get_major_formatter()(ytick) for ytick in yticklabels])


def _lambert_ticks(ax, ticks, tick_location, line_constructor, tick_extractor):
    """Get the tick locations and labels for an axis of a Lambert Conformal projection."""
    outline_patch = sgeom.LineString(ax.outline_patch.get_path().vertices.tolist())
    axis = find_side(outline_patch, tick_location)
    n_steps = 30
    extent = ax.get_extent(ccrs.PlateCarree())
    _ticks = []
    for t in ticks:
        xy = line_constructor(t, n_steps, extent)
        proj_xyz = ax.projection.transform_points(ccrs.Geodetic(), xy[:, 0], xy[:, 1])
        xyt = proj_xyz[..., :2]
        ls = sgeom.LineString(xyt.tolist())
        locs = axis.intersection(ls)
        if not locs:
            tick = [None]
        else:
            tick = tick_extractor(locs.xy)
        _ticks.append(tick[0])
    # Remove ticks that aren't visible:
    ticklabels = copy(ticks)
    while True:
        try:
            index = _ticks.index(None)
        except ValueError:
            break
        _ticks.pop(index)
        ticklabels.pop(index)
    return _ticks, ticklabels

# 创建图层
fig = plt.figure(figsize=(10, 8), frameon=True)

# 主图投影，中心经纬度
# proj = ccrs.LambertConformal(central_longitude=105, central_latitude=35,
#                              false_easting=0, false_northing=0,
#                              standard_parallels=(30, 62))
proj = ccrs.LambertConformal(central_longitude=105, central_latitude=35,)   # 不设置东北为偏移图更好看
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], projection=proj)
ax.set_extent(extent, crs=ccrs.PlateCarree())
# plt.tight_layout()
# ax.coastlines(resolution='110m')

# 主图填色——这里要注意transform一定要有，不然图框就不是rectangle了
# pic = plt.contourf(lon, lat, pm, 15, transform=ccrs.PlateCarree(), cmap=cmap, levels=lev, extent='both')
pic = ax.contourf(lon, lat, pm, 15, transform=ccrs.PlateCarree(), cmap=cmap, levels=lev, extent='both')

# 图名，色靶等设置——放在小图之前
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.title(r'中国地区 PM${_2}{_.}{_5}$', fontdict=(dict(fontsize=24)))  # 图名
position = fig.add_axes([0.91, 0.17, 0.012, 0.65])  # 这里要fig——对应subplot的句柄
cbar = plt.colorbar(pic, cax=position, orientation='vertical')  # vertical    horizontal
plt.tick_params(size=0, labelsize=12, gridOn=True, grid_color='white')
cbar.set_label(r'${\mu}g/m{^3}$')

# 南海小图
sub_ax = fig.add_axes([0.73, 0.12, 0.1, 0.17],
                      projection=ccrs.LambertConformal(central_latitude=90,
                                                       central_longitude=115))
sub_ax.set_extent([105, 125, 0, 25], crs=ccrs.PlateCarree())
sub_pic = sub_ax.contourf(lon, lat, pm, 15, transform=ccrs.PlateCarree(), cmap=cmap, levels=lev)

#  白化
# clipextent = list(range(49, 50))
# clip = shp2clip(pic, ax, 'd:/shp/CHN_adm0.shp', clipextent)


#  加中国省界
province_territory = shpreader('d:/shp/CHN_adm0.shp')  # cartopy中的
# province_territory = shapefile.Reader('d:/shp/bou2_4p.shp')         # shapefile中的
feature = cfeat.ShapelyFeature(province_territory.geometries(), crs=ccrs.PlateCarree(),
                               edgecolor='black', facecolor='none')  # cfeat.COLORS['land'])
ax.add_feature(feature, linewidth=1)
sub_ax.add_feature(feature, linewidth=1)

# *must* call draw in order to get the axis boundary used to add ticks:
fig.canvas.draw()

# Define gridline locations and draw the lines using cartopy's built-in gridliner:
xticks = [60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
yticks = [15, 20, 25, 30, 35, 40, 45, 50, 55]
ax.gridlines(xlocs=xticks, ylocs=yticks)

# Label the end-points of the gridlines using the custom tick makers:
ax.xaxis.set_major_formatter(LONGITUDE_FORMATTER)
ax.yaxis.set_major_formatter(LATITUDE_FORMATTER)
lambert_xticks(ax, xticks)
lambert_yticks(ax, yticks)

