import numpy as np
from ml_hack.functions.linear.regression import run_csv_linear_regression
from ml_hack.functions.plot.line_graph import plot_linear_regression

from ml_hack.data.file_paths import TEMP_DATA

regr, x_test, y_test = run_csv_linear_regression(TEMP_DATA)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % np.mean((regr.predict(x_test) - y_test) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(x_test, y_test))

plot_linear_regression(regr, x_test, y_test)