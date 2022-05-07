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
#得到figure与axes的对象，使用subplots只生成一个axes
figure,axes = plt.subplots()
axes.plot(data_x,data_y,label='Sin(x)')
#显示plot定义的label
axes.legend()
#显示网格
axes.grid()
axes.set_title('Plot of Sin(x)')
#展示图形
plt.show()