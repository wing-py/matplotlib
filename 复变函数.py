import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import *

r = np.arange(0,30).reshape(30,1) / 30
theta = np.pi * np.arange(-30,30) / 30

z = r * np.exp(1j * theta)
w = z**3

x = np.real(z)
y = np.imag(z)
u = np.real(w)
v = np.imag(w)

s = np.ones(z.shape)
m=np.min(u)

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

#surf1 = ax.plot_wireframe(x,y,m*s,cmap=plt.cm.hsv)
surf2 = ax.plot_surface(x,y,u,cmap=plt.cm.hsv)
plt.show()    



    
