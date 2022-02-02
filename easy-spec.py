import numpy as np
from scipy.io import wavfile
from scipy import signal
from scipy.fft import fftshift
from matplotlib import mlab
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt


def spec(file_to_path):
  sample_rate, samples = wavfile.read(file_to_path)
  freq, t, spec = signal.spectrogram(samples[:, 0], sample_rate)
  return freq, t, spec


def spec3d(freq, t, spec):
  X, Y, Z = t[None, :], freq[:, None],  20.0 * np.log10(spec)
  ax = plt.axes(projection='3d')
  ax.plot_surface(X, Y, Z, cmap='plasma')
  ax.set_xlabel('time (s)')
  ax.set_ylabel('frequencies (Hz)')
  ax.set_zlabel('amplitude (dB)')
  ax.set_zlim(-140, 0)
  return ax


file_to_path = './lacri.wav'
freq, t, spec = spec(file_to_path)
ax = spec3d(freq, t, spec)
plt.show()