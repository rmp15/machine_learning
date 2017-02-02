import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pyplot import savefig


def scatplot_facet(x, y, facet_col, data, hue, title_main, title_sub, x_label, y_label, col_wrap=5):

    # create facet grid
    temp = sns.FacetGrid(data=data, col=facet_col, hue=hue, col_wrap=col_wrap)

    # create scatter plot
    temp.map(plt.scatter, x, y, edgecolor="w")

    # adjust main title position to not overlap
    #plt.subplots_adjust(top=0.2)

    # add plot details
    temp.fig.suptitle(title_main)
    temp.set_axis_labels(x_label, y_label)
    temp.set_titles(title_sub)
    # temp.add_legend()

    #plt.show()
    savefig('../output/test.pdf', bbox_inches='tight')
