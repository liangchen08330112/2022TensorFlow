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
#生成10000个正态分布数组
norm_data = np.random.normal(size=[10000])
figure,axes = plt.subplots(1,2)
#将数据分置于10个桶中
axes[0].hist(norm_data,bins=10,label='hist')
axes[0].set_title('Histogram with 10 bins')
axes[0].legend()
#将数据分置于1000个桶中
axes[1].hist(norm_data,bins=1000,label='hist')
axes[1].set_title('Histogram with 1000 bins')
axes[1].legend()
#展示图形
plt.show()