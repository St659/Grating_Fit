from GratingDataCollector import single_file, chunker, grating_fit
from openpyxl import Workbook
import os
import csv
import matplotlib.pyplot as plt

from peakdetect import detect_peaks
import numpy as np
from scipy import optimize as sci
from scipy import stats as stat

directory = '/Users/st659/Documents/SiN Grating Local/SHU_MG1655_10-6_130417'

if __name__ == '__main__':
    sorted_file = '/Users/st659/Documents/SiN Grating Local/SHU_MG1655_10-6_130417/Output/Sorted.csv'


    fit_initial = [float(6), 10, 4, 858, 0.63235924622541]
    spectrum = np.linspace(498.6174,1103.161,3648)

    #fig = plt.figure()
    #ax3 = fig.add_subplot(111)
    with open(sorted_file, 'r') as input_file:
        reader = csv.reader(input_file, delimiter=',')

        wavelength = list()
        time = list()
        time_peak = list()
        peaks = list()
        for row in reader:
            data = row[1:]

            peak = detect_peaks.detect_peaks(data, mph=5.7, mpd = 1000)
            #if peak and peak >2000:
            #    peaks.append(peak[0])
            #    time_peak.append(row[0])
            peak_data = data[2110:2300]
            x = spectrum[2110:2300]

            peak_data = [float(data) for data in peak_data]
            try:

                a = sci.curve_fit(grating_fit,x, peak_data, p0 =fit_initial)
                print(row[0])
                time.append(row[0])
                wavelength.append(a[0][3])
            except RuntimeError:
                print("Fit Failed")


            #if int(row[0]) > 100 and int(row[0])< 104 :
                #ax3.plot(peak_data)
            #if int(row[0]) > 2100 and int(row[0])< 2110:
                #ax3.plot(peak_data)

            #if int(row[0]) > 2200:
                #break

    plt.style.use(['seaborn-white', 'seaborn-notebook'])
    wavelength_mean = list()
    wavelength_std = list()
    time_mean = list()
    for values, times in zip(chunker(wavelength, 50), chunker(time, 50)):
        wavelength_mean.append(np.mean(values, axis=0))
        wavelength_std.append(stat.sem(values, axis=0))
        time_mean.append(float(times[0])/60)

    figure = plt.figure()
    ax = figure.add_subplot(111)

    ax.set_xlabel('Time (min)')
    ax.set_ylabel('Peak Wavelength (nm)')

    print(len(time_mean))
    print(wavelength_mean)
    print(wavelength_std)
    #ax.set_ylim(851.0,852.4)
    ax.errorbar(time_mean, wavelength_mean, wavelength_std, fmt='o')
    ax.errorbar((8600.0/60, 8600.0/60), (851.0, 852.4),(0,0), fmt='--', color='k')


    plt.show()