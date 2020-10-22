import numpy as np
import matplotlib.pyplot as plt
x=np.arange (0,1,0.1)
fig=plt.figure()
ax=fig.add_subplot()
for i in range(9):
	ax.plot(x[i:i+2],x[i:i+2],alpha=float(i)/9,color="blue")
plt.show()

#渐变线的方法是构建子类，对子类分段赋值




