import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

fig,ax=plt.subplots(2, 2)
ax[0,0].plot(x,y)
ax[0,1].plot(y,x)
ax[1,0].plot(x+y,y)
ax[1,1].plot(x+y,y+x)
plt.show()
