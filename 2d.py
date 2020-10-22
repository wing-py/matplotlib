from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

low=lambda x:10000 if x>10000 else -10000 if x<-10000 else x
f=lambda x:x**5
start=-10
stop=10
step=0.01
num=(stop-start)/step
x=np.linspace (start,stop,num)
y=f(x)
for i in range(len(y)):
    y[i]=low(y[i])
z=y
#构建函数模型

fig=plt.figure(figsize=(6,6))
plt.plot(x,y,label="first curve")
plt.grid (True)
plt.axis ('equal')
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.plot([z*min(x),z*max(x)],[0,0])
plt.plot([0,0],[z*min(y),z*max(y)])
plt.legend()
plt.show()
#设置图形界面框架，并实现函数模型的映射
