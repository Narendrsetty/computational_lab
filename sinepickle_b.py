import pickle
import numpy as np
t=np.arange(0,1,0.01)
f=5
x=np.sin(2*np.pi*f*t)
with open("sinepickle_b.txt","wb") as k:
	pickle.dump(x,k)
with open("sinepickle_b.txt","rb") as l:
	pickle.load(l)
