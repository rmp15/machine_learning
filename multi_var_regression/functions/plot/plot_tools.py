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


# plots scatter plot coloured and faceted
def scatplot_facet(x, y, facet_col, data, hue, title_main, x_label, y_label, output, col_wrap=5,):

    # create facet grid
    temp = sns.FacetGrid(data=data, col=facet_col, hue=hue, col_wrap=col_wrap)

    # create scatter plot
    temp.map(plt.scatter, x, y, edgecolor="w")

    # adjust main title position to not overlap
    #plt.subplots_adjust(top=0.01)

    # add plot details
    temp.fig.suptitle(title_main)
    temp.set_axis_labels(x_label, y_label)
    temp.set_titles('{col_name}')
    temp.add_legend()

    #plt.show()
    rc('figure', figsize=(11.69, 8.27))
    savefig('../output/' + output + '.pdf', bbox_inches='tight')


# plots line plot coloured and faceted
def linplot_facet(x, y, facet_col, data, hue, title_main, x_label, y_label, output, col_wrap=5, ):

    # create facet grid
    temp = sns.FacetGrid(data=data, col=facet_col, hue=hue, col_wrap=col_wrap)

    # create scatter plot
    temp.map(plt.plot, x, y,)

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


# plots line plot coloured and faceted
def linplot_facet_2(x, y, facet_col, data, title_main, x_label, y_label, output, col_wrap=5, ):

    # create facet grid
    temp = sns.FacetGrid(data=data, col=facet_col, col_wrap=col_wrap)

    # create scatter plot
    temp.map(plt.plot, x, y,)

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
