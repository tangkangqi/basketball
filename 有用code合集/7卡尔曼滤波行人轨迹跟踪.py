#coding=utf-8
#---------------------------------------------------------------------------------------------------------------------------
#NumPy 通常与 SciPy（Scientific Python）和 Matplotlib（绘图库）一起使用，
# 这种组合广泛用于替代 MatLab，是一个强大的科学计算环境，有助于我们通过 Python 学习数据科学或者机器学习。
#SciPy 是一个开源的 Python 算法库和数学工具包。
#SciPy 包含的模块有最优化、线性代数、积分、插值、特殊函数、快速傅里叶变换、信号处理和图像处理、常微分方程求解和其他科学与工程中常用的计算。
#Matplotlib 是 Python 编程语言及其数值数学扩展包 NumPy 的可视化操作界面。它为利用通用的图形用户界面工具包，
# 如 Tkinter, wxPython, Qt 或 GTK+ 向应用程序嵌入式绘图提供了应用程序接口（API）。

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm  #正太分布密度函数有关的模块
#------------------------------------------------------------------------------------------------------------------------
#接着我们初始化行人状态x, 行人的不确定性（协方差矩阵）P，测量的时间间隔dt，处理矩阵F以及测量矩阵H
x = np.matrix([[0.0, 0.0, 0.0, 0.0]]).T#初始化行人的状态
print(x, x.shape)
P = np.diag([1000.0, 1000.0, 1000.0, 1000.0])#diag 初始化一个对角矩阵（协方差矩阵），行人的不确定性
print(P, P.shape)

dt = 0.1 # 确定时间步长
F = np.matrix([[1.0, 0.0, dt, 0.0],#处理矩阵F
              [0.0, 1.0, 0.0, dt],
              [0.0, 0.0, 1.0, 0.0],
              [0.0, 0.0, 0.0, 1.0]])
print(F, F.shape)

H = np.matrix([[0.0, 0.0, 1.0, 0.0],#初始化测量矩阵放大系数
              [0.0, 0.0, 0.0, 1.0]])
print(H, H.shape)


#-----------------------------------------------------------------------------------------------------------
#计算测量过程的噪声的协方差矩阵R和处理噪声（过程噪声）的协方差矩阵Q：
ra = 10.0**2#测量噪声协方差
R = np.matrix([[ra, 0.0],#初始化测量噪声协方差矩阵
              [0.0, ra]])
print(R, R.shape)

#ra = 0.09
#R = np.matrix([[ra, 0.0],
 #             [0.0, ra]])
#print(R, R.shape)


sv = 0.5#过程噪声
G = np.matrix([[0.5*dt**2],#G矩阵-过程噪声协方差系数
               [0.5*dt**2],
               [dt],
               [dt]])
Q = G*G.T*sv**2#过程噪声协方差矩阵
#SymPy是符号数学的Python库。它的目标是成为一个全功能的计算机代数系统，同时保持代码简洁、易于理解和扩展。
#Symbol 是一种基本数据类型
# Matrix矩阵运算库
from sympy import Symbol, Matrix
from sympy.interactive import printing
printing.init_printing() #根据环境选择输出方式
dts = Symbol('dt')#定义变量,此变量不是程序中认为的变量，而是数学公式里面的变量
Qs = Matrix([[0.5*dts**2],[0.5*dts**2],[dts],[dts]])
Qs*Qs.T
#-----------------------------------------------------------------------
# 初始化一个单位矩阵
I = np.eye(4)
print(I, I.shape)
#--------------------------------------------------------------------------------

m = 200 # 测量数
vx= 20 # in X
vy= 10 # in Y

mx = np.array(vx+np.random.randn(m))#生成200个X方向测量值
my = np.array(vy+np.random.randn(m))#生成200个Y方向测量值
measurements = np.vstack((mx,my))#生成二维矩阵

print(measurements.shape)
print('加速度测量的标准差=%.2f' % np.std(mx))
print('你假设 %.2f 在 R矩阵里.' % R[0,0])

fig = plt.figure(figsize=(16,5))#创建一个图片
plt.step(range(m),mx, label='$\dot x$')#step 阶梯图
plt.step(range(m),my, label='$\dot y$')
plt.ylabel(r'Velocity $m/s$')
plt.title('Measurements')
plt.legend(loc='best',prop={'size':18})#显示label
#---------------------------------------------------------------------------------

xt = []
yt = []
dxt= []
dyt= []
Zx = []
Zy = []
Px = []
Py = []
Pdx= []
Pdy= []
Rdx= []
Rdy= []
Kx = []
Ky = []
Kdx= []
Kdy= []

def savestates(x, Z, P, R, K):
    xt.append(float(x[0]))
    yt.append(float(x[1]))
    dxt.append(float(x[2]))
    dyt.append(float(x[3]))
    Zx.append(float(Z[0]))
    Zy.append(float(Z[1]))
    Px.append(float(P[0,0]))
    Py.append(float(P[1,1]))
    Pdx.append(float(P[2,2]))
    Pdy.append(float(P[3,3]))
    Rdx.append(float(R[0,0]))
    Rdy.append(float(R[1,1]))
    Kx.append(float(K[0,0]))
    Ky.append(float(K[1,0]))
    Kdx.append(float(K[2,0]))
    Kdy.append(float(K[3,0]))

for n in range(len(measurements[0])):#循环200次

    # 时间更新（预测）
    # ========================
    # 预测未来状态
    x = F*x

    # 预测误差协方差
    P = F*P*F.T + Q

    # 测量更新
    # ===============================
    # 计算卡尔曼增益
    S = H*P*H.T + R
    K = (P*H.T) * np.linalg.pinv(S)#pinv计算广义逆矩阵

    # 通过Z更新估算值
    Z = measurements[:,n].reshape(2,1)#获取测量值
    y = Z - (H*x)                            # 决定最优值偏向测量值还是预测值
    x = x + (K*y)

    # 更新误差协方差矩阵
    P = (I - (K*H))*P

    # 为打点保存数据
    savestates(x, Z, P, R, K)

def plot_x():
    fig = plt.figure(figsize=(16,9))#--创建图片
    plt.step(range(len(measurements[0])),dxt, label='$estimateVx$')
    plt.step(range(len(measurements[0])),dyt, label='$estimateVy$')

    plt.step(range(len(measurements[0])),measurements[0], label='$measurementVx$')
    plt.step(range(len(measurements[0])),measurements[1], label='$measurementVy$')

    plt.axhline(vx, color='#999999', label='$trueVx$')
    plt.axhline(vy, color='#999999', label='$trueV                                              y$')

    plt.xlabel('Filter Step')
    plt.title('Estimate (Elements from State Vector $x$)')
    plt.legend(loc='best',prop={'size':11})
    plt.ylim([0, 30])
    plt.ylabel('Velocity')

if __name__ == '__main__':
    plot_x()
    plt.show()
