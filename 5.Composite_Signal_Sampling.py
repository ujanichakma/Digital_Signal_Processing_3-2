'''
Problem statement: 
Consider the analog signal: xa(t)=3cos(200πt)+5sin(600πt)+10cos(1200πt). 
Show the effect of sampling rate.  

'''

import numpy as np
import matplotlib.pyplot as plt

n = n1 = np.linspace(0, 0.01, 800)


input_signal = 3 * np.cos(200*np.pi*n) + 5*np.sin(600*np.pi*n) + 10*np.cos(1200*np.pi*n)
plt.subplot(4,1,1)
plt.plot(n, input_signal, label = 'input signal')
plt.grid(True)


n = np.arange(0, 0.01, 1/800)
low_sampled = 3 * np.cos(200*np.pi*n) + 5*np.sin(600*np.pi*n) + 10*np.cos(1200*np.pi*n)
plt.subplot(4,1,2)
plt.plot(n1, input_signal,'lightgray')
plt.stem(n, low_sampled, label = 'sampled at low of nyquist')
plt.grid(True)


n = np.arange(0, 0.01, 1/1200)
low_sampled = 3 * np.cos(200*np.pi*n) + 5*np.sin(600*np.pi*n) + 10*np.cos(1200*np.pi*n)
plt.subplot(4,1,3)
plt.plot(n1, input_signal,'lightgray')
plt.stem(n, low_sampled, label = 'sampled at nyquist')
plt.grid(True)

n = np.arange(0, 0.01, 1/2000)
low_sampled = 3 * np.cos(200*np.pi*n) + 5*np.sin(600*np.pi*n) + 10*np.cos(1200*np.pi*n)
plt.subplot(4,1,4)
plt.plot(n1, input_signal,'lightgray')
plt.stem(n, low_sampled, label = 'sampled at high of nyquist')
plt.grid(True)

plt.legend()
plt.tight_layout()
plt.show()
