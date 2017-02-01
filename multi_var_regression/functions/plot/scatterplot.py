import seaborn as sns
import matplotlib.pyplot as plt


def scatplot(x,y,data):

    sns.jointplot(x,y,data)

    plt.show()
