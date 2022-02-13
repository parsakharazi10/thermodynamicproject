import numpy as np
import matplotlib.pyplot as plt
mass = 1
volume1 = 1 # mass and volume 1 are optional
pexternal = 10 ** 7
volume2 = []
quality= np.arange(0.5, 1.05, 0.05)
for t in range(11):
    volume2.append(quality[t] * (18.041 - 1.453) + 1.453)

w = [pexternal * mass * (volume2[i] - volume1) for i in range(11)]


plt.plot(quality , w , '-.')
plt.xlabel('quality')
plt.ylabel('work')
plt.show()