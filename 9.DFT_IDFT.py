import numpy as np
import matplotlib.pyplot as plt

#========================   define parameter =================================
N = 128
fs = 8000
Ts = 1 / fs
t = np.arange(N) * Ts
n = np.arange(N)
freq = np.arange(N) * fs / N



#======================   define signal  ====================================
def sig(ts):
  return np.sin(2*np.pi*1000*ts) + 0.5 * np.sin(2*np.pi*2000*ts + 4 * np.pi)



#========================= window  function ==========================
def han(N):
  return [(0.5 - 0.5 * np.cos(2*np.pi*n/(N-1))) for n in range(N)]

def ham(N):
  return [(0.54 - 0.46 * np.cos(2*np.pi*n / (N-1))) for n in range(N)]

#======================= magnitude, phase, power ============================
def mag(X):
  return [(np.sqrt(c.real **2 + c.imag**2)) for c in X]

def pha(X):
  return [(np.arctan2(c.imag, c.real)) for c in X]

def power(X):
  return [(c.real**2 + c.imag**2)for c in X]


#========================= plot original signal ============================
ta = np.linspace(0, (N-1)*Ts, 1000)
x = sig(ta)

plt.figure(figsize=(16,14))
plt.subplot(5,2,1)
plt.plot(ta, x , label = 'original signal')
plt.legend()
plt.grid(True)



#=========================   plot window =============================

plt.subplot(5,2,2)
plt.plot(n, ham(N), label = 'window')
plt.legend()
plt.grid(True)


#======================== plot sampled signal and windowed sample ===========================
plt.subplot(5,2,3)
signal = sig(t)
plt.stem(n, signal, label = 'sampled signal')
plt.grid(True)
plt.legend()

window = ham(N)
singal_windowed = signal * window

plt.subplot(5,2,4)
plt.stem(n, singal_windowed, label = 'windowed sampled')
plt.legend()
plt.grid(True)


#===========================  dft calculation function ========================
def dft_cal(x):
  X = np.zeros(N, dtype=complex)
  for m in range(N):
    sum = 0
    for n in range(N):
      sum += x[n] * np.exp(-2j*np.pi*n*m / N)
    X[m] = sum
  return X

X = dft_cal(signal)
X_w = dft_cal(singal_windowed)


#======================== idft calculation function ===================================

def idft(X):
  N = len(X)
  res = np.zeros(N, dtype=complex)

  for m in range(N):
    sum = 0
    for n in range(N):
      sum += X[n] * np.exp(2j*np.pi*n*m/N)
    res[m] = (sum / N)
  return res

#==================== magnitude spectrum ====================================
mg = mag(X)
mg_w = mag(X_w)

plt.subplot(5,2,5)
plt.stem(freq, mg, label = 'magnitude spectrum')
plt.legend()
plt.grid(True)

plt.subplot(5,2,6)
plt.stem(freq, mg_w, label = 'windowed magnitude spectrum')
plt.legend()
plt.grid(True)


#=====================   phase spectrum =========================
phase = pha(X)
phase_w = pha(X_w)

plt.subplot(5,2,7)
plt.stem(freq, phase, label = 'phase spectrum')
plt.legend()
plt.grid(True)

plt.subplot(5,2,8)
plt.stem(freq, phase_w, label = 'windowed phase spectrum')
plt.legend()
plt.grid(True)


#===================  idft calculation ===========================

x_idft = idft(X)
xidft_w = idft(X_w)

plt.subplot(5,2,9)
plt.plot(n, x_idft, label = 'idft')
plt.legend()
plt.grid(True)

plt.subplot(5,2,10)
plt.plot(n, xidft_w, label = 'idft of windowed')
plt.legend()
plt.grid(True)


plt.tight_layout()
plt.show()
