import os

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hamming, periodogram
from scipy.fftpack import fft
from matplotlib.mlab import specgram, window_hanning

import utils

script_path = os.path.realpath(__file__)
src_dir = os.path.dirname(script_path)
root_dir = os.path.realpath(os.path.join(src_dir, '..'))
raw_dir, tmp = utils.config_paths(root_dir)

trial_number = '020'
paths = utils.trial_file_paths(raw_dir, trial_number)

gait_data = utils.load_data(trial_number, 'Longitudinal Perturbation',
                            paths, tmp)

time = gait_data.data.index.values.astype(float)
belt_speed = gait_data.data['LeftBeltSpeed'].values
belt_speed -= belt_speed.mean()

N = len(time)
T = 1.0 / 100.0

yf = fft(belt_speed)
window = hamming(N)
ywf = fft(belt_speed * window)

xf = np.linspace(0.0, 1.0 / (2.0 * T), N / 2)

amp_f = 2.0 / N * np.abs(yf[1:N / 2])
amp_wf = 2.0 / N * np.abs(ywf[1:N / 2])

fig, ax = plt.subplots()
ax.semilogy(xf[1:N / 2], amp_f, '-b')
ax.semilogy(xf[1:N / 2], utils.smooth(amp_wf, 20), '-r')
ax.set_xlim((0.0, 8.0))
ax.legend(['FFT', 'FFT Moving Average'])

fig, ax = plt.subplots()
ax.semilogy(xf[1:N / 2], utils.smooth(amp_f, 20), '-b')
ax.semilogy(xf[1:N / 2], utils.smooth(amp_wf, 20), '-r')
ax.set_xlim((0.0, 8.0))
ax.legend(['FFT', 'FFT w. window'])

plt.grid()

# Periodogram

belt_speed = gait_data.data['LeftBeltSpeed'].values
f, Pxx = periodogram(belt_speed, fs=100.0, window='hamming', nfft=len(time),
                     detrend='constant')
fig, ax = plt.subplots()
ax.semilogy(f, Pxx)
ax.set_xlim((0.0, 8.0))

# Spectogram
fig, ax = plt.subplots(2)
ax[0].specgram(belt_speed,
               NFFT=100,
               Fs=100,
               detrend='mean',
               window=window_hanning,
               noverlap=50)

spectrum, freqs, t = specgram(belt_speed,
                              NFFT=100,
                              Fs=100,
                              detrend='mean',
                              window=window_hanning,
                              noverlap=50)

amp = spectrum.mean(axis=1)
ax[1].semilogy(freqs, amp)
ax[1].set_xlim((0.0, 8.0))

plt.show()
