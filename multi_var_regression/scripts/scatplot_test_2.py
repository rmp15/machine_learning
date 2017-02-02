import pandas as pd

from multi_var_regression.data.file_paths import TEMP_TEST_1
from multi_var_regression.functions.data_manip.data_tools import *
from multi_var_regression.functions.plot.plot_tools import scatplot_facet, linplot_facet

dat = pd.read_csv(TEMP_TEST_1, index_col=0)

# create unique id based on year and month FIX FUNCTION
#compound_key(dat, 'year', 'month')
dat['year_month'] = dat.year.astype(str) + dat.month.astype(str)
dat['year_month'] = pd.factorize(dat.year_month)[0] + 1

print(dat)

# create death rate per x
per_num = 100000
rate_multiply(dat, 'rate.adj', per_num)

# rename column names
dat.rename(columns={'state.name': 'state_name'}, inplace=True)

# plot data factored by month and faceted by state
scatplot_facet(x='year_month', y=('rate_'+str(per_num)), facet_col='state_name',
                 hue='month', data=dat, title_main='Death rates by state',
                 x_label='Year', y_label='Death rate (per '+str(per_num)+')')

linplot_facet(x='year_month', y=('rate_'+str(per_num)), facet_col='state_name',
                 hue='month', data=dat, title_main='Death rates by state',
                 x_label='Year', y_label='Death rate (per '+str(per_num)+')')
