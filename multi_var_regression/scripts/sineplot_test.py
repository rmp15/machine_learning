import pandas as pd
from multi_var_regression.data.file_paths import *
from multi_var_regression.functions.plot.plot_tools import sineplot

dat = pd.read_csv(TEMP_TEST_1, index_col=0)

# plot sin data
sineplot()
