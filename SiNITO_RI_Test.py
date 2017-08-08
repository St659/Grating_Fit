import numpy as np
import os
import matplotlib.pyplot as plt

directory= '/Users/st659/Google Drive/SiN ITO Grating ITO Thickness Test/2min etch/Photonics/RI Test'
plt.style.use('seaborn-white')
files = os.listdir(directory)
print(files)



ito_325_background = os.path.join(directory, files[3])
fig, (ax,ax2) = plt.subplots(1,2)
for file in files[:3]:
    ito_325 = os.path.join(directory,file)
    wave, reflectance= np.genfromtxt(ito_325, unpack=True, delimiter=',')
    wave, background = np.genfromtxt(ito_325_background, unpack=True, delimiter=',')
    ax.plot(wave, reflectance)
    ax.plot(wave,background)
    ax2.plot(wave, np.divide(reflectance,background))

ax2.set_xlim([760, 800])
ax.set_ylabel('Reflectance')
ax.set_xlabel('Wavelength (nm)')
ax2.set_ylabel('Grating Reflectance - background reflectance')
plt.show()