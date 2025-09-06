import numpy as np
import matplotlib.pyplot as plt

# Sampling specs
fs = 500            # Sampling frequency (Hz)
t = np.arange(0, 1, 1/fs)

# Simulated signal: low-frequency + high-frequency content
signal = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 80 * t)

# 🔧 High-pass FIR filter using windowed sinc
N = 101                      # Filter length
fc = 20 / fs                # Cutoff frequency (normalized)

# Create high-pass using spectral inversion of low-pass
n = np.arange(N)
h_lp = np.sinc(2 * fc * (n - (N - 1) / 2))          # Low-pass prototype
window = np.hamming(N)
h_lp *= window
h_lp /= np.sum(h_lp)

h_hp = -h_lp                          # Spectral inversion
h_hp[(N - 1) // 2] += 1               # Add delta at center

# 💥 Apply convolution
filtered = np.convolve(signal, h_hp, mode='same')

# 📊 Plot results
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title("Original Signal: Low + High Frequency")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(t, filtered)
plt.title("Filtered Signal: High-Pass FIR Applied")
plt.xlabel("Time [s]")
plt.grid(True)

plt.tight_layout()
plt.show()
