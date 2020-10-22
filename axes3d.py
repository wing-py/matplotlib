from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import numpy as np

fig=plt.figure()
ax=Axes3D(fig)
theta=np.linspace(-4*np.pi,4*np.pi,100)
z=np.linspace(-1,2,100)
r=z**z+1
x=r*np.sin(theta)
y=r*np.cos(theta)

ax.plot(x,y,z)
plt.show()
