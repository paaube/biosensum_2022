from divide_spectrum import filter_data
from collect_spectrum import load_pkl
import matplotlib.pyplot as plt

def extract_max(df):
    pass

def plot_abs(df):
    x = df[['wavelengths']]
    y = df[['absorbance']]

    plt.plot(x, y)

    plt.show()

plot_abs(load_pkl("calibration_curve/c1500_3_t4_abs"))
