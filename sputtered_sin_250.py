import numpy as np
import os
import matplotlib.pyplot as plt
import numpy as np
from peakdetect import detect_peaks

directory= '/Users/st659/Google Drive/Sputtered_SIN_250nm'
plt.style.use('seaborn-white')
files = os.listdir(directory)
print(files)


wave = np.linspace(498.6174,1103.161,3648)
raw_background = os.path.join(directory, files[-1])
fig, (ax,ax2) = plt.subplots(1,2)
files.remove('bac.csv')
print(files)
peak = list()
for file in files:
    ri_data = os.path.join(directory,file)
    wave, reflectance= np.genfromtxt(ri_data, unpack=True, delimiter=',')
    wave, background = np.genfromtxt(raw_background, unpack=True, delimiter=',')
    wave_min = np.argmax(wave >800)
    wave_max = np.argmax(wave > 950)
    normalised_reflectance = np.divide(reflectance,background)
    wave_normalised = wave[wave_min:wave_max]
    peak.append(wave_normalised[detect_peaks.detect_peaks(normalised_reflectance[wave_min:wave_max], mph=1, mpd = 1000)[0]])
    ax.plot(wave, reflectance)
    ax.plot(wave,background)

ax2.plot(peak,'o')
print(peak)



ax.set_ylabel('Reflectance')
ax.set_xlabel('Wavelength (nm)')
ax2.set_ylabel('Peak Wavelength')

plt.show()