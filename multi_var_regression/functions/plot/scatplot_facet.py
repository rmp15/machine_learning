import matplotlib.pyplot as plt
import seaborn as sns


def scatplot_facet(x, y, facet, data):

    temp = sns.FacetGrid(data=data, row=facet, col=facet)
    temp.map(plt.scatter, y, x, edgecolor="w")

    plt.show()
