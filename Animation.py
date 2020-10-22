#Animation

from matplotlib.animation import FuncAnimation
from matplotlib import pyplot as plt
import numpy as np

x=np.linspace(0,10,100)
y=x
fig=plt.figure()
point,=plt.plot(0,0,'o')
plt.plot(x,y+1)

def A(a):
    point.set_data(a/10,a/10)
    return point,

ani=FuncAnimation(fig,A,frames=100,interval=2,blit=True)

plt.show()
    
