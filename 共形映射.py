#共形映射
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

m=np.linspace(1,1,1001)
x=m
y=np.linspace(-50,50,1001)
#line1,=plt.plot(x,y,color='blue')
#w=1/z
u=x/(x*x+y*y)
v=-y/(x*x+y*y)
line2,=plt.plot(u,v,color='green')

plt.subplots_adjust()
ax=plt.axes([0.1,0.02,0.8,0.03])
slid=Slider(ax,'x=a',valmin=0.01,valmax=10.01,valinit=1,valstep=0.01)

def A(val):
    val=slid.val
    x=val*m
    #line1.set_xdata(x)
    line2.set_xdata(x/(x*x+y*y))
    line2.set_ydata(-y/(x*x+y*y))
    plt.draw()

slid.on_changed(A)
    

plt.show()
