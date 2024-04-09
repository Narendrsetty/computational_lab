import numpy as np
t=np.arange(0,1,0.01)
f=5
x=np.sin(2*np.pi*f*t)
with open("sine_2.txt","w") as k:
	k.write(str(x))
with open("sine_2.txt","r") as l:
	l.read ()
