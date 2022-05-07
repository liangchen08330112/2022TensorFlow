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
rows=2;columns=3;
data_x,data_y = sin(start,end)
figure,axes = plt.subplots(rows, columns)
for i in range(rows):
    for j in range(columns):
        #以索引的形式取出每个axes
        axes[i][j].plot(data_x,data_y,label='Sin(x)')
        axes[i][j].set_title('Plot of Sin(x) at [{},{}]'.format(i,j))
        axes[i][j].legend()
#设置大标题
plt.suptitle('All 2*3 plots')
#展示图形
plt.show()