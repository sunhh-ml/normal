# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time         : 2020/3/30 13:52
# @Author       : Huanhuan sun
# @Email        : sun58454006@163.com
# @File         : test_with_cartopy.py
# @Software     : PyCharm
# @Project      : normal

import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from matplotlib import patheffects

plt.switch_backend('Qt5Agg')


# ---------------eg.1-----------------------------#
# ax = plt.axes(projection=ccrs.Robinson(central_longitude=150))
# ax.coastlines()
# ax.gridlines(linestyle='--')
# plt.show()
# ---------------eg.1-----------------------------#
# ---------------eg.2-----------------------------#
def main():
    fig = plt.figure(figsize=(20, 5))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.Robinson())  # ax图句柄，1,1,1分图，projection投影
    ax.set_global()
    ax.stock_img()
    ax.coastlines()
    ax.plot(-0.08, 51.53, 'o', transform=ccrs.PlateCarree())  # 图上打点
    ax.plot([-0.08, 132], [51.53, 43.17], transform=ccrs.PlateCarree())  # 直线连接
    ax.plot([-0.08, 132], [51.53, 43.17], transform=ccrs.Geodetic())  # 曲线连接

    plt.show()


if __name__ == '__main__':
    main()  # 没有括号不出图不报错
    title_text = plt.title('world map', fontsize=16, verticalalignment='bottom')  # 写title
    title_text.set_path_effects([patheffects.withSimplePatchShadow()])  # title加阴影
    offset_xy = (1, -1)  # 偏移量
    rgbRed = (1, 0, 0)  # 颜色
    alpha = 0.8  # 透明度
    pe = patheffects.withSimplePatchShadow((1, -1), rgbRed, 0.8)  # 定义调色板模块
    xlabel_obj = plt.xlabel('x_label', fontsize=14, alpha=0.5)
    xlabel_obj.set_path_effects([pe])  # 无非是用了plt.xlabel().set_path_effects()的格式
    ylabel_obj = plt.ylabel('This is lat_province_territory label', fontsize=14, alpha=0.5)
    ylabel_obj.set_path_effects([pe])
    # 上面同理无非是用了plt.ylabel().set_path_effects()的格式去设定样式，最后的（）里面调用调色板模块
# ---------------eg.2-----------------------------#
