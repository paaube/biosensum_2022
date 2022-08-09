import numpy as np
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt
from collect_spectrum import load_pkl

def filter_data(df):
    return savgol_filter(df, 105, 3)

def plot_spectre_4(x1, y1, x2, y2):

       fig, ax = plt.subplots()
       ax.plot(x1, y1)
       ax.plot(x2, y2)

       ax.set(xlabel='wavelength', ylabel='intensities', title='OceanOptics light spectrum')
       ax.grid()

       plt.show()

def plot_spectre_2(x1, y1):

       fig, ax = plt.subplots()
       ax.plot(x1, y1)

       ax.set(xlabel='wavelength (nm)', ylabel='intensities (custom units)', title='Filtered light spectrum')
       ax.grid()

       plt.show()

data1 = load_pkl("calibration_curve/c1500_3_ref").T
data2 = load_pkl("calibration_curve/c1500_3_t4").T

max1 = (data1[(data1['wavelengths'] > 450) & (data1['wavelengths'] < 465)])[['intensities']].max()
max2 = (data2[(data2['wavelengths'] > 450) & (data2['wavelengths'] < 465)])[['intensities']].max()

data1[['intensities']] = data1[['intensities']] / (max1 / max2)

x1 = data1[['wavelengths']]
y1 = filter_data(np.ravel(data1[['intensities']]))
x2 = data2[['wavelengths']]
y2 = filter_data(np.ravel(data2[['intensities']]))

y3 = filter_data(np.ravel(np.log10(data1[['intensities']] / data2[['intensities']])))

plot_spectre_4(x1, y1, x2, y2)
plot_spectre_2(x1, y3)

y_test = data1[['intensities']]
plot_spectre_2(x1, y1)
plot_spectre_2(x1, y_test)


