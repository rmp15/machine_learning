import pandas as pd

from data.file_paths import *
from functions.plot.scatterplot import scatplot

dat = pd.read_csv(TEMP_TEST_1, index_col=0)

print(dat)

# plot sin data
scatplot('variable', 'rate.adj', dat)


