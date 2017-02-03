import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rc
from matplotlib.pyplot import savefig


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

    # add plot details
    temp.fig.suptitle(title_main)
    temp.set_axis_labels(x_label, y_label)
    temp.set_titles('{col_name}')
    temp.add_legend()

    # plt.show()
    rc('figure', figsize=(11.69, 8.27))
    savefig('../output/' + output + '.pdf', bbox_inches='tight')
