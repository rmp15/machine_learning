import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import rc
from matplotlib.pyplot import savefig


# scatter plot of all points on one graph
def scatplot(x, y, file_loc):

    dat = pd.read_csv(file_loc, index_col=0)
    sns.jointplot(x, y, dat)
    plt.show()


# demo sine-wave plots
def sineplot(flip=1):

    x = np.linspace(0, 14, 100)

    sns.set_style('dark')
    sns.despine()

    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)

    plt.show()

# plot with various general parameters
def plot_facet(plot, x, y, facet_col, data, title_main, x_label, y_label, output, col_wrap=5, hue=None):

    # create facet grid
    if 'hue' is None:
        temp = sns.FacetGrid(data=data, col=facet_col, col_wrap=col_wrap)
    else:
        temp = sns.FacetGrid(data=data, col=facet_col, hue=hue, col_wrap=col_wrap)

    # create plot
    if plot is 'scatter':
        temp.map(plt.scatter, x, y)
    elif plot is 'line':
        temp.map(plt.plot, x, y)
    else:
        print('Please specify plot type with plot argument')

    # adjust main title position to not overlap
    # plt.subplots_adjust(top=0.01)

    # add plot details
    temp.fig.suptitle(title_main)
    temp.set_axis_labels(x_label, y_label)
    temp.set_titles('{col_name}')
    temp.add_legend()

    # plt.show()
    rc('figure', figsize=(11.69, 8.27))
    savefig('../output/' + output + '.pdf', bbox_inches='tight')