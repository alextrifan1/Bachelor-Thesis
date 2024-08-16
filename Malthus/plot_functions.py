import matplotlib.pyplot as plt
import numpy as np
def plot_populatie(timp, populatie, u_label):
    plt.plot(timp, populatie, 'bo', label = u_label)

def plot_malthus(y0, timp, r, u_label):
    timp_np = np.array(timp)
    y = y0*np.exp(r*(timp_np-timp_np[0]))

    plt.plot(timp_np, y, color = 'g', marker = 'o', linestyle = '-', linewidth = 2, label = u_label)
