import numpy as np
from matplotlib import pyplot as plt

x=np.linspace(0,15,150)
y1=np.linspace(0,10,100)
y2=np.linspace(10,0,50)
y=np.append(y1,y2)

f=(2*x+y)/(3**0.5)
h=(2*y+x)/(3**0.5)

#plt.subplot(30,30,1)
#plt.plot(x,y)

#plt.subplot(30,30,2)
plt.plot(f,h)

plt.show()

'''
图形横坐标为一维空间，纵坐标为时间，反斜率则为速度
图形中左方曲线象征着光的传播，右方为相对于原点的一个移动的探测者
图1表示原点探测者，图2表示运动探测者以自身为参考系的世界观
引入洛伦兹变换，同时实现参考系转换和光速不变原理
表示洛伦兹变换为相对绝对时空观更真实的时空观
洛伦兹变换得证
'''
