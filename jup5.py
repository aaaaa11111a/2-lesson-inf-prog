import numpy as np
import matplotlib.pyplot as plt
x=np.array([1,2,3,4,5])
y=np.array([0.99,0.49,0.35,0.253,0.18])
x_err=0.05
y_err=0.1
p1=np.polyfit(x,y,deg=1)
f1=np.poly1d(f1)
p2=np.polyfit(x,y,deg=2)
f2=np.poly1d(f2)
line=np.linspace(0.5,5.5,100)
plt.errorbar(x,y,xerr=x_err,yerr=y_err)
plt.plot(line,p1(line))
plt.plot(line,p2(line))
plt.show()
