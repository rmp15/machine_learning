import pandas as pd

from data.file_paths import *
from functions.plot.scatplot import scatplot

dat = pd.read_csv(TEMP_TEST_1, index_col=0)

print(dat)

# plot sin data
scatplot('year', 'rate.adj', dat)

