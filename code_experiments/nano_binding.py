from collect_spectrum import load_pkl
import matplotlib.pyplot as plt
import numpy as np

nano = load_pkl("test2_nano2").T
bare = load_pkl("test2_bare2").T
avg = load_pkl("reference_avg").T

nano[['intensities']] = np.log10(avg[['intensities']] / nano[['intensities']])
bare[['intensities']] = np.log10(avg[['intensities']] / bare[['intensities']])

plt.plot(nano[['wavelengths']], nano[['intensities']])
plt.plot(bare[['wavelengths']], bare[['intensities']])

plt.show()


