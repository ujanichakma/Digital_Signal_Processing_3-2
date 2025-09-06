'''
Show that the highest rate of oscillation in a discrete-time sinusoidal is obtained 
when ω=π. 
'''

import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-10, 11, 1)
omegra = np.pi 
y = np.cos(np.pi*n  )

plt.title('cos(wn)')
plt.stem(n, y, label = 'cos(wn)')
plt.legend()
plt.xlabel('n')
plt.ylabel('amplitude')
plt.tight_layout()
plt.show()
