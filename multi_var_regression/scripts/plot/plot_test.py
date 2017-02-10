import os

from multi_var_regression.data.file_paths import TEMP_TEST_2
from multi_var_regression.functions.data_manip.data_tools import *
from multi_var_regression.functions.plot.plot_tools import plot_facet

dat = pd.read_csv(TEMP_TEST_2, index_col=0, nrows=1000)

# create unique id based on year and month FIX FUNCTION
# compound_key(dat, 'year', 'month')
dat['year_month'] = dat.year.astype(str) + dat.month.astype(str)
dat['year_month'] = pd.factorize(dat.year_month)[0] + 1

# create death rate per x
per_num = 100000
rate_multiply(dat, 'rate.adj', per_num)

# rename column names
dat.rename(columns={'state.name': 'state_name'}, inplace=True)

# scatter plot of data factored by month and faceted by state
plot_facet(plot='scatter', x='year_month', y=('rate_' + str(per_num)), data=dat, facet_col='state_name',
           hue='month', title_main='Death rates by state coloured by month',
           x_label='Time', y_label='Death rate (per ' + str(per_num) + ')', output='scatplot_facet_1')

# line plot of data factored by month and faceted by state
plot_facet(plot='line', x='year_month', y=('rate_' + str(per_num)), data=dat,
           facet_col='state_name', hue='month', title_main='Death rates by state coloured by month',
           x_label='Time', y_label='Death rate (per ' + str(per_num) + ')', output='linplot_facet_1')

# line plot of data faceted by state only
plot_facet(plot='line', x='year_month', y=('rate_' + str(per_num)), data=dat,
           facet_col='state_name', title_main='Death rates by state',
           x_label='Time', y_label='Death rate (per ' + str(per_num) + ')', output='linplot_facet_2')
