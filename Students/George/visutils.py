from numpy import genfromtxt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact
from ipywidgets import fixed

def load_and_prepare_cmd(filename):
    data = np.genfromtxt(filename, dtype=float, delimiter=',', names=True)
    g = data['g']
    gVal = np.where((g>14) & (g<24))
    data = data[gVal]
    g = data['g']
    r = data['r']
    gr = g-r
    grVal = np.where((gr>-0.5) & (gr<2.5))
    data = data[grVal]
    g = data['g']
    r = data['r']
    gr = g-r
    return g, gr

# (g, gr) = load_and_prepare_cmd('fieldA.csv')

def interactive_hess(g, gr):
    def plot_hess(g, gr, grd):
        plt.hexbin(gr, g, gridsize = grd, bins = 'log', cmap='gnuplot2')
        plt.show()
    interact(plot_hess, g=fixed(g), gr=fixed(gr), grd=(50,300,1))
