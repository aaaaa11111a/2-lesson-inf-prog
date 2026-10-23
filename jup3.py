import numpy as np
plt.figure(figsize=(5,5))
import matplotlib.pyplot as plt
x=np.arange(-20,20,0.01)
plt.plot(x,np.log((x**2+1)*np.exp(-abs(x)/10))/np.log(1+np.tan(1/(1+np.sin(x)**2))))
