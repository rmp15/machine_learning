import pandas as pd

from data.file_paths import *
from functions.plot.scatplot_facet import scatplot_facet

dat = pd.read_csv(TEMP_TEST_1, index_col=0)

# create unique id based on year and month
dat['year_month'] = dat.year.astype(str) + '_' + dat.month.astype(str)

# create death rate per 100,000
dat['rate_100000'] = dat['rate.adj'] * 100000

# rename column names
dat.rename(columns={'state.name': 'state_name'}, inplace=True)

# unique names of states
state_names = dat.state_name.unique()

print(state_names)

# plot data factored
scatplot_facet(x='year', y='rate_100000', facet_col='state_name',
                 hue='month', data=dat, title_main='Death rates by state', title_sub='',
                 x_label='Year', y_label='Death rate (per 100,000)')
