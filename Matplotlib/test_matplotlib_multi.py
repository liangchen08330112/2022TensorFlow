#用条形图的形式绘制正弦函数图像
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
data_x,data_y = sin(start,end)
noise_y = np.random.randn(*data_y.shape)/2
noise_data_y = data_y+noise_y
figure,axes = plt.subplots()
axes.bar(data_x,data_y,label='Sin(x)',linewidth=5)
axes.legend()
axes.grid()
#展示图形
plt.show()