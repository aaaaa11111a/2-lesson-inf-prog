import numpy as np
plt.figure(figsize=(5,5))
import matplotlib.pyplot as plt
x=np.arange(-2,4,0.01)
plt.plot(x,x**2-x-6)
plt.plot(x,x)
plt.grid()
plt.show()
