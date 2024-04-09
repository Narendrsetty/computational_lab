import numpy as np
t=np.arange(0,1,0.01)
f=5
x=np.sin(2*np.pi*f*t)
with open("sinenum_b.txt","wb") as k:
	np.save(k,x)
with open("sinenum_b.txt","rb") as l:
	np.load(l)
