#稳压电路
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider
import numpy as np
r=5
R=5
Ud=5
u=np.linspace(0,10,101)
i=u/(r+R)
I1=(u-Ud)/R
I2=np.linspace(1,1,101)#Ud/r
I3=I1-I2


plt.subplots_adjust(bottom=0.2)
# line,
line1,=plt.plot(u,i,color='red')
line2,=plt.plot(u,I1,color='blue')
line3,=plt.plot(u,I2,color='green')
line4,=plt.plot(u,I3,color='black')
line5=plt.plot(u,u-5,alpha=0)

#line2,=ax.plot(u,lable='')
ax1=plt.axes([0.03,0.04,0.8,0.03])
slid1=Slider(ax1,'r',valmin=0,valmax=10,valinit=5,valstep=0.1)
ax2=plt.axes([0.03,0.01,0.8,0.03])
slid2=Slider(ax2,'R',valmin=0,valmax=10,valinit=5,valstep=0.1)
ax3=plt.axes([0.03,0.07,0.8,0.03])
slid3=Slider(ax3,'Ud',valmin=0,valmax=10,valinit=5,valstep=0.1)

# slid>>val>>func
def A(val):
    val=slid1.val
    line1.set_ydata(u/(val+slid2.val))
    line3.set_ydata(I2*slid3.val/val)
    line4.set_ydata((u-slid3.val)/slid2.val-I2*slid3.val/slid1.val)
    plt.draw()
def B(val):
    val=slid2.val
    line1.set_ydata(u/(val+slid1.val))
    line2.set_ydata((u-slid3.val)/val)
    line4.set_ydata((u-slid3.val)/val-I2*slid3.val/slid1.val)
    plt.draw()
def C(val):
    val=slid3.val
    line2.set_ydata((u-val)/slid2.val)
    line3.set_ydata(I2*val/slid1.val)
    line4.set_ydata((u-slid3.val)/slid2.val-I2*slid3.val/slid1.val)
    plt.draw()
# on_changed
slid1.on_changed(A)
slid2.on_changed(B)
slid3.on_changed(C)

plt.ylim(-5,5)

plt.yticks ([-5,0,5])
#plt.title('red open,blue i1')
plt.show()


