import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def scatplot(x, y, file_loc):

    dat = pd.read_csv(file_loc, index_col=0)
    sns.jointplot(x, y, dat)
    plt.show()
