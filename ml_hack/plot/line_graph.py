import matplotlib.pyplot as plt


def plot_linear_regression(regr, x_data, y_data):
    plt.scatter(x_data, y_data, color='black')
    plt.plot(x_data, regr.predict(x_data), color='blue',
             linewidth=3)

    plt.xticks(())
    plt.yticks(())

    plt.show()