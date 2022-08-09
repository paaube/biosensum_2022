from collect_spectrum import load_pkl, save_to_pkl, plot_spectre
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter


def absorbance(ref, test):

    ref = load_pkl(ref).T
    test = load_pkl(test).T

    test = test.assign(absorbance=filter_data(np.ravel(np.log10(ref[['intensities']] / test[['intensities']])))).drop(
        columns=['intensities']
    )
    test.plot(x='wavelengths', y='absorbance')
    
    plt.show()
    
    return test


def filter_data(df):
    return savgol_filter(df, 105, 3)


if __name__=="__main__":
    
    #absorbance("calibration_curve/c1500_4_ref", "calibration_curve/c1500_4_t4")
    save_to_pkl(absorbance("calibration_curve/c1500_4_ref", "calibration_curve/c1500_4_t4"), "calibration_curve/c1500_4_t4_abs")

    #data = load_pkl("test_abs_autosave")
    #x = data[['wavelengths']]
    #y = data[['absorbance']]
    #plot_spectre(x, y)




