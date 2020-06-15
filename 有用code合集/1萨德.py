# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 09:59:34 2016
#轰炸萨德
@author: Administrator
"""
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
font=FontProperties(fname=r"c:\windows\fonts\simsun.ttc",size=20)
# 创建一个fig对象，自定义fig的size
fig = plt.figure(figsize=(60,60))
# 划分fig并且选择一个子图给ax变量
ax = fig.add_subplot(1,1,1)
#width=2000,height=2000
m = Basemap(projection='mill', llcrnrlat=30, urcrnrlat=50, llcrnrlon=90, urcrnrlon=150)
m.drawcoastlines()
m.drawcountries(linewidth=2)
#m.drawrivers()
# bjlat, bjlon are lat/lon of Bei jing北京的经纬度
bjlat = 40; bjlon = 116
#tokyolat,tokyolon 表示萨德部署地的经纬度
THAADlat,THAADlon=36.119485,128.3445734
# draw parallels
m.drawparallels(np.arange(10,90,20),labels=[1,1,0,1])
# draw meridians
m.drawmeridians(np.arange(-180,180,30),labels=[1,1,0,1])
#m.drawmapboundary(fill_color='aqua')
# fill continents, set lake color same as ocean color.
#m.fillcontinents(color='coral',lake_color='aqua')
def Draw_position(lon,lat,city,mark,markersize=100):
    xpt,ypt=m(lon,lat)
    #convert back to lat/lon
    lonpt,latpt=m(xpt,ypt,inverse=True)
    m.plot(xpt,ypt,mark,markersize) #plot a blue dot there
    plt.text(xpt+100000,ypt+100000,city)
#绘制萨德坐标
Draw_position(128.3445734,36.119485,"THAAD",'c*',100)
#绘制北京坐标
Draw_position(116,40,"Beijign",'g^',100)
#链接北京和萨德的路线
m.drawgreatcircle(bjlon,bjlat,THAADlon,THAADlat,linewidth=2,color='b')
m.etopo()
#添加图例，文字说明
plt.legend(loc=4)
plt.title("轰炸萨德，制作人Toby!",fontproperties=font)
plt.show()