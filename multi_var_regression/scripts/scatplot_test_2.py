import pandas as pd

from data.file_paths import *
from functions.plot.scatplot_facet import scatplot_facet

# load data
dat = pd.read_csv(TEMP_TEST_1, index_col=0, nrows=1000)

print(dat)

# plot data factored
scatplot_facet('year', 'rate.adj', facet_row='age', facet_col='state.name', hue='month', data=dat)

