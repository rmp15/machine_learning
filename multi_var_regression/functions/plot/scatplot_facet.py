import matplotlib.pyplot as plt
import seaborn as sns


def scatplot_facet(x, y, facet_row, facet_col, hue, data):

    temp = sns.FacetGrid(data=data, row=facet_row, col=facet_col, hue=hue)
    temp.map(plt.scatter, x, y, edgecolor="w")

    plt.show()
