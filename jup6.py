import numpy as np
import matplotlib.pyplot as plt
a=0.5
b=3
N=100
x=np.linspace(-2,2,10000)
y=np.zeros_like(x)
for n in range (N):
    y+=(a**n)*np.cos((b**n)*np.pi*x)
plt.plot(x,y)
plt.grid()
plt.show()
