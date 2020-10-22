#解析函数
import numpy as np
from matplotlib import pyplot as plt
x=np.linspace(-100,100,200)
y=x
xx,yy=np.meshgrid(x,y)
u=xx*xx-yy*yy
v=2*xx*yy
plt.contour(x,y,u,colors='blue')
plt.contour(x,y,v,colors='red')
plt.show()
