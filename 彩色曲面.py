import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
x=np.linspace (-5,5,1000)
y=x
xx,yy=np.meshgrid(x,y)
z=xx*xx+yy*yy
'''
print('x',x)
print('y',y)
print('z',z)
print('xx',xx)
print('yy',yy)
'''
fig=plt.figure()
ax=Axes3D(fig)
ax.plot_surface(xx,yy,z,cmap=cm.hsv_r)

plt.show()
#彩色曲面
