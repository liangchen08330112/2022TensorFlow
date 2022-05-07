import matplotlib.pyplot as plt
import numpy as np
#定义数据产生函数
def sin(start,end):
    #使用np.linspace产生1000个等间隔的数据
    x = np.linspace(start,end,num=1000)
    return x,np.sin(x)
#横轴：-10到10
start=-10
end=10
data_x,data_y=sin(start,end)
figure,axes = plt.subplots()
num=100
#定义带系数的正弦函数，以模拟不同时刻的数据
def sin_with_effi(start,end,effi):
    x = np.linspace(start,end,num=1000)
    return x,np.sin(effi*x)
#开启交互模式
plt.ion()
for i in range(num):
    #清除上一次绘图结果
    plt.cla()
    #取出当前时刻的数据
    data_x,data_y = sin_with_effi(start,end,effi=i/10)
    axes.plot(data_x,data_y)
    #暂停图像以显示最新结果
    plt.pause(0.001)
#关闭交互模式
plt.ioff()
plt.show()