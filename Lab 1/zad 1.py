import matplotlib.pyplot as plt
import numpy as np


def function(x):
    return x**2+5


# Zad 2
for id_, val in enumerate([np.linspace(-1, 1), np.linspace(-6, 6), np.linspace(0, 5)]):
    plt.subplot(3, 1, id_+1)
    plt.plot(val, function(val))
plt.show()

