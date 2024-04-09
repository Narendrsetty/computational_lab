import numpy as np
from matplotlib import pyplot as plt
t=np.arange(0,1,0.01)
f=5
x=np.cos(2*np.pi *f*t)
plt.plot(t,x)
plt.xlabel('time')
plt.ylabel('amplitude')
plt.title('cos wave')
plt.show()
