import numpy as np
import matplotlib.pyplot as plt

#===================== sampling setup =========================

fs = 1200
t = np.arange(0, 1, 1/fs)
x = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 50 * t)



#===================  convolution definition =========================
def convolution(x, h):
  N = len(x) + len(h) - 1
  y = []

  for i in range(N):
    sum = 0
    for k in range(len(x)):
      if 0<= i-k < len(h):
        sum  += x[k] * h[i-k]
    y.append(sum)
  return y


#=====================  impulse response definition ===================
def hann(N):
  return [(0.5 - 0.5 * np.cos(2*np.pi * n / (N-1))) for n in range(N)]

def gen_impulse(N, fc, fs):    
  center = (N-1) / 2  
  n = np.arange(N)
  h = np.sinc(2 * fc * (n - center) / fs )  * hann(N)
  h = h / np.sum(h)
  return h



#=======================   parameter ===============================
N = 51
fc = 10

h = gen_impulse(N, fc, fs)
x_f = convolution(x,h)
t1 = np.arange(len(x_f)) / fs


#====================  plot orginal signal =========================

plt.plot(t, x, color = 'gray', label ="input signal")
plt.plot(t1, x_f, color = 'b', label = 'filtered signal')
plt.legend()
plt.grid(True)

plt.show()
