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
#绘制曲线图
axes.plot(data_x,data_y,label='Sin(x)',linewidth=5)
#绘制散点图，此时axes对象仍处于活动状态，直接绘制即可。
axes.scatter(data_x,data_y,label='scatter noise data',color='yellow')
axes.legend()
axes.grid()
plt.show()