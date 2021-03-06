# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time         : 2020/3/30 13:52
# @Author       : Huanhuan sun
# @Email        : sun58454006@163.com
# @File         : test_with_pyecharts_BMap.py
# @Software     : PyCharm
# @Project      : normal

import pyecharts.options as opts
from pyecharts.charts import BMap
from pyecharts.globals import BMapType  # 设置缩放比例尺

data = [
    ["海门", 9],
    ["鄂尔多斯", 12],
    ["招远", 12],
    ["舟山", 12],
    ["齐齐哈尔", 14],
    ["盐城", 15],
    ["赤峰", 16],
    ["青岛", 18],
    ["乳山", 18],
    ["金昌", 19],
    ["泉州", 21],
    ["莱西", 21],
    ["日照", 21],
    ["胶南", 22],
    ["南通", 23],
    ["拉萨", 24],
    ["云浮", 24],
    ["梅州", 25],
    ["文登", 25],
    ["上海", 25],
    ["攀枝花", 25],
    ["威海", 25],
    ["承德", 25],
    ["厦门", 26],
    ["汕尾", 26],
    ["潮州", 26],
    ["丹东", 27],
    ["太仓", 27],
    ["曲靖", 27],
    ["烟台", 28],
    ["福州", 29],
    ["瓦房店", 30],
    ["即墨", 30],
    ["抚顺", 31],
    ["玉溪", 31],
    ["张家口", 31],
    ["阳泉", 31],
    ["莱州", 32],
    ["湖州", 32],
    ["汕头", 32],
    ["昆山", 33],
    ["宁波", 33],
    ["湛江", 33],
    ["揭阳", 34],
    ["荣成", 34],
    ["连云港", 35],
    ["葫芦岛", 35],
    ["常熟", 36],
    ["东莞", 36],
    ["河源", 36],
    ["淮安", 36],
    ["泰州", 36],
    ["南宁", 37],
    ["营口", 37],
    ["惠州", 37],
    ["江阴", 37],
    ["蓬莱", 37],
    ["韶关", 38],
    ["嘉峪关", 38],
    ["广州", 38],
    ["延安", 38],
    ["太原", 39],
    ["清远", 39],
    ["中山", 39],
    ["昆明", 39],
    ["寿光", 40],
    ["盘锦", 40],
    ["长治", 41],
    ["深圳", 41],
    ["珠海", 42],
    ["宿迁", 43],
    ["咸阳", 43],
    ["铜川", 44],
    ["平度", 44],
    ["佛山", 44],
    ["海口", 44],
    ["江门", 45],
    ["章丘", 45],
    ["肇庆", 46],
    ["大连", 47],
    ["临汾", 47],
    ["吴江", 47],
    ["石嘴山", 49],
    ["沈阳", 50],
    ["苏州", 50],
    ["茂名", 50],
    ["嘉兴", 51],
    ["长春", 51],
    ["胶州", 52],
    ["银川", 52],
    ["张家港", 52],
    ["三门峡", 53],
    ["锦州", 54],
    ["南昌", 54],
    ["柳州", 54],
    ["三亚", 54],
    ["自贡", 56],
    ["吉林", 56],
    ["阳江", 57],
    ["泸州", 57],
    ["西宁", 57],
    ["宜宾", 58],
    ["呼和浩特", 58],
    ["成都", 58],
    ["大同", 58],
    ["镇江", 59],
    ["桂林", 59],
    ["张家界", 59],
    ["宜兴", 59],
    ["北海", 60],
    ["西安", 61],
    ["金坛", 62],
    ["东营", 62],
    ["牡丹江", 63],
    ["遵义", 63],
    ["绍兴", 63],
    ["扬州", 64],
    ["常州", 64],
    ["潍坊", 65],
    ["重庆", 66],
    ["台州", 67],
    ["南京", 67],
    ["滨州", 70],
    ["贵阳", 71],
    ["无锡", 71],
    ["本溪", 71],
    ["克拉玛依", 72],
    ["渭南", 72],
    ["马鞍山", 72],
    ["宝鸡", 72],
    ["焦作", 75],
    ["句容", 75],
    ["北京", 79],
    ["徐州", 79],
    ["衡水", 80],
    ["包头", 80],
    ["绵阳", 80],
    ["乌鲁木齐", 84],
    ["枣庄", 84],
    ["杭州", 84],
    ["淄博", 85],
    ["鞍山", 86],
    ["溧阳", 86],
    ["库尔勒", 86],
    ["安阳", 90],
    ["开封", 90],
    ["济南", 92],
    ["德阳", 93],
    ["温州", 95],
    ["九江", 96],
    ["邯郸", 98],
    ["临安", 99],
    ["兰州", 99],
    ["沧州", 100],
    ["临沂", 103],
    ["南充", 104],
    ["天津", 105],
    ["富阳", 106],
    ["泰安", 112],
    ["诸暨", 112],
    ["郑州", 113],
    ["哈尔滨", 114],
    ["聊城", 116],
    ["芜湖", 117],
    ["唐山", 119],
    ["平顶山", 119],
    ["邢台", 119],
    ["德州", 120],
    ["济宁", 120],
    ["荆州", 127],
    ["宜昌", 130],
    ["义乌", 132],
    ["丽水", 133],
    ["洛阳", 134],
    ["秦皇岛", 136],
    ["株洲", 143],
    ["石家庄", 147],
    ["莱芜", 148],
    ["常德", 152],
    ["保定", 153],
    ["湘潭", 154],
    ["金华", 157],
    ["岳阳", 169],
    ["长沙", 175],
    ["衢州", 177],
    ["廊坊", 193],
    ["菏泽", 194],
    ["合肥", 229],
    ["武汉", 273],
    ["大庆", 279],
]

geoCoordMap = {
    "海门": [121.15, 31.89],
    "鄂尔多斯": [109.781327, 39.608266],
    "招远": [120.38, 37.35],
    "舟山": [122.207216, 29.985295],
    "齐齐哈尔": [123.97, 47.33],
    "盐城": [120.13, 33.38],
    "赤峰": [118.87, 42.28],
    "青岛": [120.33, 36.07],
    "乳山": [121.52, 36.89],
    "金昌": [102.188043, 38.520089],
    "泉州": [118.58, 24.93],
    "莱西": [120.53, 36.86],
    "日照": [119.46, 35.42],
    "胶南": [119.97, 35.88],
    "南通": [121.05, 32.08],
    "拉萨": [91.11, 29.97],
    "云浮": [112.02, 22.93],
    "梅州": [116.1, 24.55],
    "文登": [122.05, 37.2],
    "上海": [121.48, 31.22],
    "攀枝花": [101.718637, 26.582347],
    "威海": [122.1, 37.5],
    "承德": [117.93, 40.97],
    "厦门": [118.1, 24.46],
    "汕尾": [115.375279, 22.786211],
    "潮州": [116.63, 23.68],
    "丹东": [124.37, 40.13],
    "太仓": [121.1, 31.45],
    "曲靖": [103.79, 25.51],
    "烟台": [121.39, 37.52],
    "福州": [119.3, 26.08],
    "瓦房店": [121.979603, 39.627114],
    "即墨": [120.45, 36.38],
    "抚顺": [123.97, 41.97],
    "玉溪": [102.52, 24.35],
    "张家口": [114.87, 40.82],
    "阳泉": [113.57, 37.85],
    "莱州": [119.942327, 37.177017],
    "湖州": [120.1, 30.86],
    "汕头": [116.69, 23.39],
    "昆山": [120.95, 31.39],
    "宁波": [121.56, 29.86],
    "湛江": [110.359377, 21.270708],
    "揭阳": [116.35, 23.55],
    "荣成": [122.41, 37.16],
    "连云港": [119.16, 34.59],
    "葫芦岛": [120.836932, 40.711052],
    "常熟": [120.74, 31.64],
    "东莞": [113.75, 23.04],
    "河源": [114.68, 23.73],
    "淮安": [119.15, 33.5],
    "泰州": [119.9, 32.49],
    "南宁": [108.33, 22.84],
    "营口": [122.18, 40.65],
    "惠州": [114.4, 23.09],
    "江阴": [120.26, 31.91],
    "蓬莱": [120.75, 37.8],
    "韶关": [113.62, 24.84],
    "嘉峪关": [98.289152, 39.77313],
    "广州": [113.23, 23.16],
    "延安": [109.47, 36.6],
    "太原": [112.53, 37.87],
    "清远": [113.01, 23.7],
    "中山": [113.38, 22.52],
    "昆明": [102.73, 25.04],
    "寿光": [118.73, 36.86],
    "盘锦": [122.070714, 41.119997],
    "长治": [113.08, 36.18],
    "深圳": [114.07, 22.62],
    "珠海": [113.52, 22.3],
    "宿迁": [118.3, 33.96],
    "咸阳": [108.72, 34.36],
    "铜川": [109.11, 35.09],
    "平度": [119.97, 36.77],
    "佛山": [113.11, 23.05],
    "海口": [110.35, 20.02],
    "江门": [113.06, 22.61],
    "章丘": [117.53, 36.72],
    "肇庆": [112.44, 23.05],
    "大连": [121.62, 38.92],
    "临汾": [111.5, 36.08],
    "吴江": [120.63, 31.16],
    "石嘴山": [106.39, 39.04],
    "沈阳": [123.38, 41.8],
    "苏州": [120.62, 31.32],
    "茂名": [110.88, 21.68],
    "嘉兴": [120.76, 30.77],
    "长春": [125.35, 43.88],
    "胶州": [120.03336, 36.264622],
    "银川": [106.27, 38.47],
    "张家港": [120.555821, 31.875428],
    "三门峡": [111.19, 34.76],
    "锦州": [121.15, 41.13],
    "南昌": [115.89, 28.68],
    "柳州": [109.4, 24.33],
    "三亚": [109.511909, 18.252847],
    "自贡": [104.778442, 29.33903],
    "吉林": [126.57, 43.87],
    "阳江": [111.95, 21.85],
    "泸州": [105.39, 28.91],
    "西宁": [101.74, 36.56],
    "宜宾": [104.56, 29.77],
    "呼和浩特": [111.65, 40.82],
    "成都": [104.06, 30.67],
    "大同": [113.3, 40.12],
    "镇江": [119.44, 32.2],
    "桂林": [110.28, 25.29],
    "张家界": [110.479191, 29.117096],
    "宜兴": [119.82, 31.36],
    "北海": [109.12, 21.49],
    "西安": [108.95, 34.27],
    "金坛": [119.56, 31.74],
    "东营": [118.49, 37.46],
    "牡丹江": [129.58, 44.6],
    "遵义": [106.9, 27.7],
    "绍兴": [120.58, 30.01],
    "扬州": [119.42, 32.39],
    "常州": [119.95, 31.79],
    "潍坊": [119.1, 36.62],
    "重庆": [106.54, 29.59],
    "台州": [121.420757, 28.656386],
    "南京": [118.78, 32.04],
    "滨州": [118.03, 37.36],
    "贵阳": [106.71, 26.57],
    "无锡": [120.29, 31.59],
    "本溪": [123.73, 41.3],
    "克拉玛依": [84.77, 45.59],
    "渭南": [109.5, 34.52],
    "马鞍山": [118.48, 31.56],
    "宝鸡": [107.15, 34.38],
    "焦作": [113.21, 35.24],
    "句容": [119.16, 31.95],
    "北京": [116.46, 39.92],
    "徐州": [117.2, 34.26],
    "衡水": [115.72, 37.72],
    "包头": [110, 40.58],
    "绵阳": [104.73, 31.48],
    "乌鲁木齐": [87.68, 43.77],
    "枣庄": [117.57, 34.86],
    "杭州": [120.19, 30.26],
    "淄博": [118.05, 36.78],
    "鞍山": [122.85, 41.12],
    "溧阳": [119.48, 31.43],
    "库尔勒": [86.06, 41.68],
    "安阳": [114.35, 36.1],
    "开封": [114.35, 34.79],
    "济南": [117, 36.65],
    "德阳": [104.37, 31.13],
    "温州": [120.65, 28.01],
    "九江": [115.97, 29.71],
    "邯郸": [114.47, 36.6],
    "临安": [119.72, 30.23],
    "兰州": [103.73, 36.03],
    "沧州": [116.83, 38.33],
    "临沂": [118.35, 35.05],
    "南充": [106.110698, 30.837793],
    "天津": [117.2, 39.13],
    "富阳": [119.95, 30.07],
    "泰安": [117.13, 36.18],
    "诸暨": [120.23, 29.71],
    "郑州": [113.65, 34.76],
    "哈尔滨": [126.63, 45.75],
    "聊城": [115.97, 36.45],
    "芜湖": [118.38, 31.33],
    "唐山": [118.02, 39.63],
    "平顶山": [113.29, 33.75],
    "邢台": [114.48, 37.05],
    "德州": [116.29, 37.45],
    "济宁": [116.59, 35.38],
    "荆州": [112.239741, 30.335165],
    "宜昌": [111.3, 30.7],
    "义乌": [120.06, 29.32],
    "丽水": [119.92, 28.45],
    "洛阳": [112.44, 34.7],
    "秦皇岛": [119.57, 39.95],
    "株洲": [113.16, 27.83],
    "石家庄": [114.48, 38.03],
    "莱芜": [117.67, 36.19],
    "常德": [111.69, 29.05],
    "保定": [115.48, 38.85],
    "湘潭": [112.91, 27.87],
    "金华": [119.64, 29.12],
    "岳阳": [113.09, 29.37],
    "长沙": [113, 28.21],
    "衢州": [118.88, 28.97],
    "廊坊": [116.7, 39.53],
    "菏泽": [115.480656, 35.23375],
    "合肥": [117.27, 31.86],
    "武汉": [114.31, 30.52],
    "大庆": [125.03, 46.58],
}


def convert_data():
    res = []
    for i in range(len(data)):
        # geo_coord = geoCoordMap[df[i][0]]  # df[i][0]为城市名，geoCoorMap[df[i][0]]为经纬度
        # geo_coord.append(df[i][1])  # df[i][1]为城市对应的pm25浓度值
        # res.append([df[i][0], geo_coord])     # 这里导致了放在黄点上会出现城市名+经纬度+数值

        res.append([data[i][0], data[i][1]])  # 上面三句改成这一句，则不会出现经纬度，鼠标放点上显示  北京：79

    return res


(
    BMap(
        init_opts=opts.InitOpts(
            width="1400px",
            height="800px"),
        is_ignore_nonexistent_coord=True,  # 是否忽略不存在的坐标，默认值为 False，即不忽略
    )
        .add(
        series_name="pm2.5",  # 系列名称，用于 tooltip 的显示，legend 的图例筛选。
        data_pair=convert_data(),  # 坐标点经纬度以及数值数据
        type_="effectScatter",  # 图类型————————散射效应图
        is_selected=True,  # 是否选中图例
        # symbol = "roundRect",  # 标记类型包括 ‘circle’, ‘rect’, ‘roundRect’, ‘triangle’,‘diamond’, ‘pin’, ‘arrow’, ‘none’,
        symbol_size=5,  # 散点大小
        color="red",  # 系列label的颜色
        is_polyline=False,  # 是否是多段线，在画 lines 图情况下
        is_large=True,  # 是否启用大规模线图的优化，在数据图形特别多的时候（>=5k）可以开启
        large_threshold=2000,  # 开启绘制优化的阈值
        # label_opts=opts.LabelOpts(formatter="{b}:{c}\n({d}%)", position="left", is_show=True),  # a/b/c,分别显示pm25/城市名/经纬度/
        label_opts=opts.LabelOpts(is_show=False),   # 还没搞懂formatter
        effect_opts=opts.EffectOpts(False),  # 涟漪特效功能
        linestyle_opts=opts.LineStyleOpts(is_show=True),    # 线样式配置项
        tooltip_opts=opts.TooltipOpts(is_show=True,trigger="item",trigger_on="mousemove|click"),
        itemstyle_opts=opts.ItemStyleOpts(color="yellow"),  # 图元样式配置项
    )
        .add_schema(
        baidu_ak="TV72R1obhPKWvnWvrlpclPYdlFExbCb1",  # 百度申请，打开最后保存的网页会提示你如何申请，这里我申请的是浏览器端地图的使用权限，“”内为百度AK码
        center=[107.114129, 33.550339],  # 不进行任何移动缩放之前的视角的中心点，用经纬度表示
        zoom=5,  # 不进行任何缩放之前能看到的网页面积，越小看到区域越大（远超过中国区域），越大看到区域越小（可能进显示一个城市），貌似仅能为整数,如5.5相当于5
        is_roam=True,  # True，网页可用鼠标滚轮缩放，False则不行
        map_style={
            "styleJson": [
                {
                    "featureType": "water",  # 这块儿里面的所有color建议都默认
                    "elementType": "all",
                    "stylers": {"color": "#044161"},  # stylers 网页有底色，styles网页没有底色（例图如直接百度地图）
                },  # 建议有底色 414行设置为黄色，没有底色的409设为红色
                {
                    "featureType": "land",
                    "elementType": "all",
                    "stylers": {"color": "#004981"},  # python控制台设置颜色
                },
                {
                    "featureType": "boundary",
                    "elementType": "geometry",
                    "stylers": {"color": "#064f85"},
                },
                {
                    "featureType": "railway",
                    "elementType": "all",
                    "stylers": {"visibility": "off"},
                },
                {
                    "featureType": "highway",
                    "elementType": "geometry",
                    "stylers": {"color": "#004981"},
                },
                {
                    "featureType": "highway",
                    "elementType": "geometry.fill",
                    "stylers": {"color": "#005b96", "lightness": 1},
                },
                {
                    "featureType": "highway",
                    "elementType": "labels",
                    "stylers": {"visibility": "off"},
                },
                {
                    "featureType": "arterial",  # 城市主干道
                    "elementType": "geometry",
                    "stylers": {"color": "#004981"},
                },
                {
                    "featureType": "arterial",
                    "elementType": "geometry.fill",
                    "stylers": {"color": "#00508b"},
                },
                {
                    "featureType": "poi",  # 某个地理位置周边的信息
                    "elementType": "all",
                    "stylers": {"visibility": "on"},
                },
                {
                    "featureType": "green",  # 绿色下垫面
                    "elementType": "all",
                    "stylers": {"color": "#056197", "visibility": "off"},
                },
                {
                    "featureType": "subway",
                    "elementType": "all",
                    "stylers": {"visibility": "off"},
                },
                {
                    "featureType": "manmade",  # 人造的，不知道是啥？？？
                    "elementType": "all",
                    "stylers": {"visibility": "off"},
                },
                {
                    "featureType": "local",
                    "elementType": "all",
                    "stylers": {"visibility": "off"},
                },
                {
                    "featureType": "arterial",
                    "elementType": "labels",
                    "stylers": {"visibility": "off"},
                },
                {
                    "featureType": "boundary",
                    "elementType": "geometry.fill",
                    "stylers": {"color": "#029fd4"},
                },
                {
                    "featureType": "building",
                    "elementType": "all",
                    "stylers": {"color": "#1a5787"},
                },
                {
                    "featureType": "label",
                    "elementType": "all",
                    "stylers": {"visibility": "off"},
                },
            ]
        },
    )
        .set_global_opts(
        title_opts=opts.TitleOpts(
            title="全国主要城市空气质量",
            subtitle="df from PM25.in",
            subtitle_link="http://www.pm25.in",  # 点击网页subtitle，可以进这个网站
            pos_left="left",  # 主副标题位置，最开始为center，会挡住PM25开关，改为左更好
            title_textstyle_opts=opts.TextStyleOpts(color="yellow"),  # 最开始颜色为#fff，但改为黄色更好看
        )
    )
        .add_control_panel(
        # navigation_control_opts=opts.BMapNavigationControlOpts(position=BMapType.ANCHOR_TOP_RIGHT),
        opts.BMapNavigationControlOpts(  # 地图的平移缩放控件
            position=0,  # 等同于anchor_top_left，1、2、3分别为右上，左下，右下
            offset_height=50,  # 距离上部偏移量
            offset_width=10,  # 距离左右偏移量
            type_=0,  # 0-4表示NAVIGATION_CONTROL_LARGE/SMALL/PAN/ZOOM,又标准平移缩放滑块/平移缩放/仅平移/仅缩放
            is_show_zoom_info=True,  # 是否显示级别提示信息
            is_enable_geo_location=True,  # 控件是否集成定位功能
        ),  # 若下面还有add_contorl_panel里面的空间调整，这里必须有“，”，若没有，可以没有逗号
        opts.BMapOverviewMapControlOpts(  # 缩略地图控件
            # position=0,  # 等同于anchor_top_left，1、2、3分别为右上，左下，右下
            # offset_height=50,  # 距离上部偏移量
            # offset_width=10,  # 距离左右偏移量
            is_open=True,
        ),
        opts.BMapScaleControlOpts(  # 比例尺控件
            # position=0,  # 等同于anchor_top_left，1、2、3分别为右上，左下，右下
            # offset_height=50,  # 距离上部偏移量
            # offset_width=10,  # 距离左右偏移量
        ),
        opts.BMapTypeControlOpts(  # 切换地图类型的控件
            # position=0,
            type_=2,  # MAPTYPE_CONTROL_HORIZONTAL/DROPDOWN/MAP，按钮水平方式展示为0,下拉列表为1，图片方式为2（设置该类型后无法指定 maptypes 属性）
        ),
        opts.BMapCopyrightTypeOpts(  # 版权控件，您可以在地图上添加自己的版权信息
            # position=0,
            # offset_height=50, # 距离上部偏移量
            # offset_width=10,  # 距离左右偏移量
            copyright_="made by shh",  # Copyright 的文本内容, 可以放入 HTML 标签
        ),
        opts.BMapGeoLocationControlOpts(  # 地图定位的控件，使用 HTML5 浏览器定位功能
            # position=0,
            # offset_height=50, # 距离上部偏移量
            # offset_width=10,  # 距离左右偏移量
            is_show_address_bar=True,  # 是否显示定位信息面板。默认显示定位信息面板
            is_enable_auto_location=True,  # 添加控件时是否进行定位。默认添加控件时不进行定位
        )
    )
        .render("e:/python_out/air_quality_baidu_map.html")
)
