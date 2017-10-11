import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))
file = '/Users/st659/Downloads/i-t for python test.xlsx'



data = pd.read_excel(file)
print(data.columns)


time_raw = data[' Time']
time = list()
isd = data[' Isd']
isd_mean = list()
isd_std = list()
isd_rms = list()
isd_min = list()

samples = 100
try:
    ig = data[' Ig']
    ig_mean = list()
    ig_std = list()
    ig_rms = list()
    ig_min = list()
    ig = np.asarray(ig)
    ig = chunker(ig, samples)

except KeyError:
    print('Isd Column Missing')
    ig = False




time_raw = np.asarray(time_raw)

isd = np.asarray(isd)


fig, (ax,ax2, ax3, ax4) = plt.subplots(1,4)

ax4.plot(time_raw, isd)


time_raw = chunker(time_raw, samples)
isd = chunker(isd, samples)





for t, i in zip(time_raw, isd):
    time.append(t[0])
    isd_mean.append(np.mean(i, axis=0))
    isd_std.append(np.std(i,axis=0))
    isd_rms.append(np.sqrt(np.mean(np.square(i),axis=0)))
    isd_min.append(np.min(i))

ig_header = 'Time,Ig_mean,Ig_std,Ig_rms,Ig_min'
header = 'Time,Isd_mean,Isd_std,Isd_rms,Isd_min'

ax.errorbar(time,isd_mean, isd_std)
ax2.plot(time, isd_rms)
ax3.plot(time, isd_min)

if ig:
    for i in ig:
        ig_mean.append(np.mean(i, axis=0))
        ig_std.append(np.std(i,axis=0))
        ig_rms.append(np.sqrt(np.mean(np.square(i),axis=0)))
        ig_min.append(np.min(i))
    ax.errorbar(time,ig_mean, ig_std)
    ax2.plot(time, ig_rms)
    ax3.plot(time, ig_min)
    data_to_save = np.array([time, isd_mean,isd_std,isd_rms,isd_min, ig_mean,ig_std,ig_rms,ig_min, ])
    header = header + ig_header
else:
    data_to_save = np.array([time, isd_mean,isd_std,isd_rms,isd_min])

print(data_to_save.shape)

np.savetxt('output.txt', np.transpose(data_to_save),delimiter=',', header=header)



ax.set_ylabel('Current (mA)')
ax.set_xlabel('Time (s)')

ax2.set_ylabel('RMS Current (mA)')
ax2.set_xlabel('Time (s)')

ax3.set_ylabel('Current (mA)')
plt.show()