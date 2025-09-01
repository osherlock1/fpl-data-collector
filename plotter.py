import matplotlib.pyplot as plt
import numpy as np


class PlotManager:
    def __init__(self):
        pass

    def plot_scatter(self, x , y, labels, title ="Scatter Plot", xlabel = "X", ylabel="Y"):
        plt.figure(figsize=(10,6))
        plt.scatter(x, y)
        for i, label in enumerate(labels):
            plt.annotate(label, (x[i], y[i]), fontsize = 8, ha='right')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()