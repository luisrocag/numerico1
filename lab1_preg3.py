# -*- coding: utf-8 -*-
import numpy as np 

import matplotlib.pyplot as plt

def y1(x):
    return np.log(1+x)/x

def y2(x):
    idx=((1+x)!=1)
    z=np.ones_like(x)
    z[idx]=np.log(1+x[idx])/((1+x[idx])-1)
    return z

x = np.linspace(-1E-15,1E-15,100)

y = y1(x)

z = y2(x)

plt.plot(x, y, '-')
plt.savefig('y1.png')

plt.plot(x, z, '-')
plt.savefig('y2.png')

#plt.show()

