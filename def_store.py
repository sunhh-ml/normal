# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time         : 2020/3/30 13:48
# @Author       : Huanhuan sun
# @Email        : sun58454006@163.com
# @File         : def_store.py
# @Software     : PyCharm
# @Project      : normal

import warnings  # 引入警告用于提示，基本每个def都要用到
#   sort_file_by_windows_rule
import fnmatch
import os.path
from natsort import natsorted
#   shp2clip
import shapefile
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import pyproj  # 支持多投影时，需要转换xy坐标——库
import shapely.geometry as sgeom  # 支持多投影时，需要转换xy坐标——cartopy
#    write_matrix_to_xls
import xlwt
import numpy as np
import os  # 保存数据时，没有该路径则创建


# 所有def需要import的库
# 按照windows原则排序file_address下后缀为file_style的文件，以便读取
# Sort the files suffixed with file_style under file_address according to the windows principle, so as to read
# ******************** update ****************************
#   2020-3-17   finish first demo


def sort_file_by_windows_rule(file_address, file_style):
    if file_style[0] == '.':
        style_for_file_list = '*' + file_style[file_style.find('.'):len(file_style)]
    else:
        style_for_file_list = file_style

    file_list = fnmatch.filter(os.listdir(file_address),
                               style_for_file_list)  # style_for_life_list注意：一定不能为'.nc'，'.'前至少要有个'*'
    file_list = natsorted(file_list)
    style_for_file_path = file_style[file_style.find('.'):len(file_style)]

    total_doc = []
    for i in range(len(file_list)):
        file_path = file_address + file_list[i]
        if os.path.splitext(file_path)[1] == style_for_file_path:  # 这里的则一定要为'.nc'，'.'前不能有任何东西
            total_doc.append(file_path)
    return total_doc


# Copyright: Huanhuan Sun   All rights reserved.
# If you have any problem, please contact me: sun58454006@163.com

# =====================================================================================================================#
# =====================================================================================================================#

# 将数据按照矩阵的方式，直接存入excel指定sheet，指定行列，数据为多维矩阵(m*n1*n2...)时自动转为二维数组(m*n)
#
# ******************** update ****************************
#   2020-3-19   finish first demo


def write_matrix_to_xls(matrix, file_path, file_name, sheet_name, title, row=0, col=0):
    """
        Save data in Excel specified sheet and specified row and col in the form of matrix directly, and the data
        should be at  most two-dimensional array.
    :param matrix: ndarray
        The pre saving data.
    :param file_path:  string
        The path of the pre save file.
    :param file_name: string
        The name of the pre save file.
    :param sheet_name:  optional, string
        The name to use for this sheet, as it will appear in the  tabs at the bottom
        of the Excel application. The default is 'sheet1'.
    :param row:  optional, int
        The start row of the saving data. The default is 0. And the row should not bigger than 65536.
    :param col:  optional, int
        The start column of the saving data. The default is 0. And the col should not bigger than 256.
    :param title:  optional, list, string
        The name of each column of data. The default is nan.
    :return:
    """

    outdata = matrix.reshape(matrix.shape[0], -1)
    if len(matrix.shape) > 2 or len(matrix.shape) == 1:
        msg = """
            The pre stored matrix's dimension is not 2 but greater than 2 or only 1, 
            so the array will be automatically converted to m * n dimensions, 
            where m is the first dimension of the pre stored matrix.
        """
        warnings.warn(msg)
    book = xlwt.Workbook(style_compression=0)
    sheet = book.add_sheet(sheet_name, cell_overwrite_ok=False)  # cell那个设置是否覆盖数据，重复写入
    row_sum = outdata.shape[0]
    col_sum = outdata.shape[1]
    col_title = len(title)
    for jcol in range(col, col_title + col):
        sheet.write(row, jcol, title[jcol - col])
    for irow in range(row + 1, row_sum + row + 1):
        for jcol in range(col, col_sum + col):
            sheet.write(irow, jcol, outdata[irow - row - 1, jcol - col])
    if not os.path.exists(file_path):  # 如果路径不存在
        os.makedirs(file_path)
        msg = """
            Custom path does not exist, and has be created now
        """
        warnings.warn(msg)
    book.save(file_path + file_name)


# Copyright: Huanhuan Sun   All rights reserved.
# If you have any problem, please contact me: sun58454006@163.com

# =====================================================================================================================#
# =====================================================================================================================#

# def shp2clip(originfig, ax, shpfile, region):
#     sf = shapefile.Reader(shpfile)
#     vertices = []  ######这块是已经修改的地方
#     codes = []  ######这块是已经修改的地方
#     for shape_rec in sf.shapeRecords():
#         # if shape_rec.record[3] == region:  ####这里需要找到和region匹配的唯一标识符，record[]中必有一项是对应的。
#         if shape_rec.record[0] in region:  ######这块是已经修改的地方
#             pts = shape_rec.shape.points
#             prt = list(shape_rec.shape.parts) + [len(pts)]
#             for i in range(len(prt) - 1):
#                 for j in range(prt[i], prt[i + 1]):
#                     vertices.append((pts[j][0], pts[j][1]))
#                 codes += [Path.MOVETO]
#                 codes += [Path.LINETO] * (prt[i + 1] - prt[i] - 2)
#                 codes += [Path.CLOSEPOLY]
#             clip = Path(vertices, codes)
#             clip = PathPatch(clip, transform=ax.transData)
#     for contour in originfig.collections:
#         contour.set_clip_path(clip)
#     return clip
def shp2clip(originfig, ax, shpfile, region):
    sf = shapefile.Reader(shpfile)
    vertices = []
    codes = []
    for shape_rec in sf.shapeRecords():
        if shape_rec.record[0] in region:
            pts = shape_rec.shape.points
            prt = list(shape_rec.shape.parts) + [len(pts)]
            for i in range(len(prt) - 1):
                for j in range(prt[i], prt[i + 1]):
                    # vertices.append(m(pts[j][0], pts[j][1]))
                    vertices.append(proj_trans(pts[j][0], pts[j][1]))  # 转换坐标
                codes += [Path.MOVETO]
                codes += [Path.LINETO] * (prt[i + 1] - prt[i] - 2)
                codes += [Path.CLOSEPOLY]
            clip = Path(vertices, codes)
            clip = PathPatch(clip, transform=ax.transData)
    for contour in originfig.collections:
        contour.set_clip_path(clip)
    return clip


def proj_trans(shp_lon, shp_lat):
    proj = '102012'  # 投影坐标的WKID
    proj1 = pyproj.Proj(init='4326')  # 定义shp文件经纬度坐标系 https://developers.arcgis.com/javascript/3/jshelp/gcs.htm
    proj2 = pyproj.Proj(init=proj)
    lon, lat = proj1(shp_lon, shp_lat)
    proj_lon, proj_lat = pyproj.transform(proj1, proj2, lon, lat, radians=True)
    return proj_lat, proj_lat



