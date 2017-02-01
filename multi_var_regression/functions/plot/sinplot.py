import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def sineplot(flip=1):

    x = np.linspace(0, 14, 100)

    sns.set_style('dark')
    sns.despine()

    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)

    plt.show()
