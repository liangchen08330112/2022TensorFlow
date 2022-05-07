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
noise_data_y = noise_y+data_y
#得到figure与axes的对象，使用subplots只生成一个axes
figure,axes = plt.subplots()
#散点图绘制
axes.scatter(data_x,noise_data_y,label='Sin(x) with noise scatter')
#显示plot定义的label
axes.legend()
#显示网格
axes.grid()
#展示图形
plt.show()