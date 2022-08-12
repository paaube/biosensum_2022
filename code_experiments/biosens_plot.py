import matplotlib.pyplot as plt
import time
import numpy as np
from math import pi

from seabreeze_test import get_spectre

def plot_two_data(df1, df2):
    df1 = df1.rename(columns={'intensities': 'df1'})
    df2 = df2.rename(columns={'intensities': 'df2'})
    #df1[['df1']] = df1[['df1']]/1.5
    ax = df1.plot(x='wavelengths', y='df1')
    df2.plot(x='wavelengths', y='df2', ax=ax)
    plt.show()


def live_plot():

    data_init = get_spectre().T
    x = data_init[['wavelengths']]
    y = data_init[['intensities']]

    fig = plt.figure()
    ax = fig.add_subplot(111)

    plot1, = ax.plot(x, y)

    plt.title("Ocean Optics Light Spectrum", fontsize=20)

    plt.xlabel("Wavelengths")
    plt.ylabel("Intensities")

    plt.ion()

    i = True

    while i == True:
        data = get_spectre().T
            
        plot1.set_xdata(data[['wavelengths']]) 
        plot1.set_ydata(data[['intensities']])
        
        fig.canvas.draw()
        fig.canvas.flush_events()
        time.sleep(0.1)
        i = False
        
    plt.ioff()


#if __name__=="__main__":
#    live_plot()
