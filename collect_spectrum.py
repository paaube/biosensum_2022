import matplotlib.pyplot as plt
import pandas as pd

from seabreeze.spectrometers import Spectrometer

def get_spectre():

       spec = Spectrometer.from_first_available()
       spec.integration_time_micros(20000)
       x = spec.wavelengths()
       y = spec.intensities()

       plot_spectre(x, y)

       output = pd.DataFrame(index=["wavelengths", "intensities"], data=[x, y])

       return output


def plot_spectre(x, y):

       fig, ax = plt.subplots()
       ax.plot(x, y)

       ax.set(xlabel='wavelength', ylabel='intensities', title='OceanOptics light spectrum')
       ax.grid()

       plt.show()


def save_to_pkl(df, filename):
       df.to_pickle(f"data/{filename}.pkl")


def load_pkl(filename):
       return pd.read_pickle(f"data/{filename}.pkl")


if __name__=="__main__":
       #get_spectre()
       save_to_pkl(get_spectre(), "3_types_of_fiber/normal_tip")


