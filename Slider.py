#Slider
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

def f(x,a=1):
    return a*x
x=np.linspace (-3,3,12)
y=f(x)
plt.subplots_adjust ()
line,=plt.plot(x,y,color=(0,1,1))



ax=plt.axes ([0.1,0.02,0.8,0.03])
slid=Slider(ax,'a',valmin=-1,valmax=1,valinit=0,valstep=0.01)

def A(aval):
    aval=slid.val
    line.set_ydata(f(x,aval))
    plt.draw()

slid.on_changed(A)

plt.show()
