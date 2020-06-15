# coding: utf-8
from tkinter import *
import random
import time
import numpy as np
#
#创建一个类，这个类含有两个参数，一个是画布，一个是球的颜色
#
class Ball:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_oval(10,10,25,25,fill=color)#创建一个圆，4个参数为圆XY顶点，fill为圆的颜色
        self.canvas.move(self.id,245,100)#移动到距离画布左上角的位置

        #来回反弹
        #--self.x = 0
        #--self.y = -1
        starts = [-3,-2,-1,1,2,3]
        random.shuffle(starts)#将start元素随机排列
        self.x = starts[0]
        self.y = -3
        #winfo_height()函数来获取画布当前的高度，赋值给对象变量
        self.canvas_height = self.canvas.winfo_height()
        #获取X轴坐标
        self.canvas_width = self.canvas.winfo_width()
    def draw(self):
        #获取小球起始点
        start= self.canvas.coords(self.id)#获取小球的坐标点

        self.canvas.move(self.id,self.x,self.y)#开始移动移动到距离圆的左上角距离
        #获取某个对象在画布的坐标，返回一个数组（两个坐标，左上角的坐标和右下角的两个坐标）
        pos = self.canvas.coords(self.id)#获取小球的坐标点
        #打印获取的坐标
        print(pos)
        self.canvas.create_polygon((start[0] + start[2])/2,(start[1] + start[3])/2,(pos[0] + pos[2])/2,(pos[1] + pos[3])/2,width = 12,outline='blue',fill='')
        #self.canvas.create_line((start[0] + start[2])/2,(start[1] + start[3])/2,(pos[0] + pos[2])/2,(pos[1] + pos[3])/2,width = 12,fill='blue')
        #如果最上面的纵轴坐标在顶上，则往下移动一个像素
        y_v = [1,2,3]
        y_vv = [-1,-2,-3]
        #利用三角形斜边长度决定随机方向
        Triangle_hypotenuse = 4
        random.shuffle(y_v)#将元素随机排列
        random.shuffle(y_vv)#将元素随机排列
        if pos[1] <= 0:
            self.y = y_v[0]
        #如果最下面的纵轴坐标在底上，则向上移动
        if pos[3] > self.canvas_height:
            self.y = y_vv[0]
        #宽度控制#
        #如果在左边框了，那么向右边移动  像素
        if pos[0] <= 0:
            self.x = int(np.sqrt(np.square( Triangle_hypotenuse) - np.square( self.y)))
        #如果到右边框了，左移动  像素
        if pos[2] > self.canvas_width:
            self.x = int(-np.sqrt(np.square( Triangle_hypotenuse) - np.square( self.y)))


def func():
    #创建画布
    tk = Tk()
    tk.title("Game_ball")
    tk.resizable(0,0)# 调整窗口大小。0不可修改窗口大小
    tk.wm_attributes("-topmost",1)#窗口置顶
    #bd=0,highlightthickness=0 画布之外没有边框
    canvas = Canvas(tk,width=800,height=600,bd=0,highlightthickness=0)
    canvas.pack()# frame1.pack()：这句话是指使用包管理器将frame1放到容器中。
    tk.update()

    #创建对象
    ball = Ball(canvas,'red')

    #一直保持循环
    while 1:
        ball.draw()
        #快速刷新屏幕
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)

if __name__ == '__main__':
    func()

