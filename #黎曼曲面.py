#黎曼曲面
from matplotlib import cm
from matplotlib.colors import LightSource
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


x=np.linspace(-1,1,45)
y=x
xx,yy=np.meshgrid(x,y)
u=xx*xx-yy*yy
v=xx*yy


fig=plt.figure()
ax=Axes3D(fig)

ls=LightSource()
colors=ls.shade(v,cmap=cm.hsv )

surf=ax.plot_surface(xx,yy,u,facecolors=colors)


plt.show()
