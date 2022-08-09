from collect_spectrum import load_pkl
import matplotlib.pyplot as plt

min_lum = load_pkl("intensity_opt/min_lum").T
x_min = min_lum[['wavelengths']]
y_min = min_lum[['intensities']]

min_1 = load_pkl("intensity_opt/min+1_lum").T
x_min_1 = min_1[['wavelengths']]
y_min_1 = min_1[['intensities']]

max_1 = load_pkl("intensity_opt/max-1_lum").T
x_max_1 = max_1[['wavelengths']]
y_max_1 = max_1[['intensities']]

max_lum = load_pkl("intensity_opt/max_lum").T
x_max = max_lum[['wavelengths']]
y_max = max_lum[['intensities']]

fig, ax = plt.subplots()
ax.plot(x_min, y_min, label="intensity 1")
ax.plot(x_min_1, y_min_1, label="intensity 2")
ax.plot(x_max_1, y_max_1, label="intensity 3")
ax.plot(x_max, y_max, label="intensity 4")
ax.legend()

ax.set(xlabel='wavelength (nm)', ylabel='intensities (custom units)', title='OceanOptics light spectrum')
ax.grid()

plt.show()
