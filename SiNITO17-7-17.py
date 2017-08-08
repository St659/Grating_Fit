import numpy as np
import os
import matplotlib.pyplot as plt

directory= '/Users/st659/Google Drive/ITO SiN images'
plt.style.use('seaborn-white')
files = os.listdir(directory)
print(files)


ito_325 = os.path.join(directory,files[2])
ito_325_background = os.path.join(directory, files[1])

wave, reflectance= np.genfromtxt(ito_325, unpack=True, delimiter=',')
wave, background = np.genfromtxt(ito_325_background, unpack=True, delimiter=',')
print(wave)

fig, (ax,ax2) = plt.subplots(1,2)

ax.plot(wave, reflectance)
ax.plot(wave,background)
ax2.plot(wave, np.divide(reflectance,background))
ax.set_ylabel('Reflectance')
ax.set_xlabel('Wavelength (nm)')
ax2.set_ylabel('Grating Reflectance - background reflectance')
plt.show()