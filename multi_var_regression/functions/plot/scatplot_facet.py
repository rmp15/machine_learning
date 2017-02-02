import matplotlib.pyplot as plt
import seaborn as sns


#def scatplot_facet_1(x, y, facet_col, data, **kwargs,*hue, *title_main, *title_sub, *x_label, *y_label):
def scatplot_facet_1(x, y, facet_col, data, **kwargs):

    for key, value in kwargs:
        print("%s == %s" % (key, value))

    # create facet grid
    temp = sns.FacetGrid(data=data, col=facet_col, hue=hue, col_wrap=5)

    # create scatter plot
    temp.map(plt.scatter, x, y, edgecolor="w")

    # adjust main title position to not overlap
    plt.subplots_adjust(top=0.9)

    # add plot details
    temp.fig.suptitle(title_main)
    temp.set_axis_labels(x_label, y_label)
    temp.set_titles(str(title_sub))
    temp.add_legend()

    plt.show()
