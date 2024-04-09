import numpy as np
t=np.arange(0,1,0.01)
f=5
x=np.sin(2*np.pi*f*t)
with open("sine.txt","wb") as k:
	k.write(x)
with open("sine.txt","rb") as l:
	l.read()
