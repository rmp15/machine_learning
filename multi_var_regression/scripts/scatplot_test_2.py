import pandas as pd

from data.file_paths import *
from functions.plot import scatplot_facet_1

dat = pd.read_csv(TEMP_TEST_1, index_col=0, nrows=1000)

# create unique id based on year and month
#dat['year_month'] = dat.year.astype(str) + '_' + dat.month.astype(str)

# plot data factored
scatplot_facet_1('year', 'rate.adj', facet_row='age', facet_col='state.name', hue='month', data=dat)
#scatplot_facet()
