import pandas as pd

from data.file_paths import *
from functions.plot.scatplot_facet import scatplot_facet

# load data
dat = pd.read_csv(TEMP_TEST_1, index_col=0)

# plot data
scatplot_facet('year', 'rate.adj', 'state.name', dat)

