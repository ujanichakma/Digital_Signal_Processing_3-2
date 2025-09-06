'''
Filter realization using 6-point averaging, 6-point differencing equations. 
'''

import numpy as np
import matplotlib.pyplot as plt

# Sample input signal (analog-like)
np.random.seed(0)
n = np.linspace(0, 1, 200)
x = np.sin(2 * np.pi * 5 * n) + 0.5 * np.random.randn(len(n))  # 5 Hz sine + noise

# 6-point Averaging Filter
def avg_filter(x):
    y = np.zeros_like(x)
    for i in range(5, len(x)):
        y[i] = np.sum(x[i-5:i+1]) / 6
    return y

# 6-point Differencing Filter
def diff_filter(x):
    y = np.zeros_like(x)
    for i in range(5, len(x)):
        y[i] = (x[i] - x[i-1] + x[i-2] - x[i-3] + x[i-4] - x[i-5]) / 6
    return y

# Plotting function
def plot_signal(x, y, title, color='b'):
    plt.plot(x, y, color=color)
    plt.title(title)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)

# Apply filters
y_avg = avg_filter(x)
y_diff = diff_filter(x)

# Plot results
plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plot_signal(n, x, 'Original Analog-like Signal', 'gray')

plt.subplot(3, 1, 2)
plot_signal(n, y_avg, '6-Point Averaging Filter Output', 'green')

plt.subplot(3, 1, 3)
plot_signal(n, y_diff, '6-Point Differencing Filter Output', 'red')

plt.tight_layout()
plt.show()
