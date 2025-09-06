''' 
Generating elementary signals like Unit Step, Ramp, Exponential, Sine, and 
Cosine sequences. 

'''

import numpy as np
import matplotlib.pyplot as plt


def ploting(x, y,  title, labeling , sub):
    plt.subplot(3,2,sub)
    plt.title(title)
    plt.stem(x, y, label = labeling)
    plt.legend()
    plt.xlabel('time axis')
    plt.ylabel('amplitude')
    plt.grid(True)
    plt.xticks(x)
    
    
    
    
    

n = np.arange(-10, 11, 1)
amplitude  = np.where(n>=0, 1, 0)
ploting(n, amplitude, 'unit_step', 'unit_step', 1)

amplitude = 0.8 ** n
ploting(n, amplitude, 'exponential', 'exponential', 2)

amplitude = np.where(n>=0, n, 0)
ploting(n, amplitude, 'unit_ramp', 'unit_ramp', 3)



amplitude = np.sin(2*np.pi*0.1*n)
ploting(n, amplitude, 'sin', 'sin', 4)

amplitude = np.cos(2*np.pi*0.1*n)
ploting(n, amplitude, 'cos', 'cos', 5)



plt.tight_layout()
plt.show()


