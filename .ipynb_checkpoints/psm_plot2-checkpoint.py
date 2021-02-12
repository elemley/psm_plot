from math import *
import sympy as sympy
import numpy as np
import matplotlib.pyplot as plt

np.
"""
UCO PSM Plotting Library

Form of functions are:

xxyyzzPlot###

xxyyzz = Plot type (Line, Scatter, etc...)

Multiple types are meant to be series on a single plot... arguments are in this same order

### =

first digit = # of rows
second digit = # of cols
third digit = # of series per plot

Arguments are in row, then column order

"""
class psm_plot:
    'Base Class for psm_plot'
    
    def __init__(self,name):
        self.name = name
        plt.

