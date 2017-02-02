import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib import rc
from matplotlib.pyplot import savefig


def scatplot(x, y, file_loc):

    dat = pd.read_csv(file_loc, index_col=0)
    sns.jointplot(x, y, dat)
    plt.show()


def scatplot_facet(x, y, facet_col, data, hue, title_main, x_label, y_label, col_wrap=5):

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
    savefig('../output/test.pdf', bbox_inches='tight')
