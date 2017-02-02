import pandas as pd

from data.file_paths import *
from functions.plot.scatplot_facet import scatplot_facet
from functions.table import rate_multiply

dat = pd.read_csv(TEMP_TEST_1, index_col=0)

# create unique id based on year and month MAKE FUNCTION
dat['year_month'] = dat.year.astype(str) + dat.month.astype(str)

# create death rate per 100,000 MAKE FUNCTION
#dat['rate_100000'] = dat['rate.adj'] * 100000
rate_multiply(dat, "rate_adj", 100000)

# rename column names MAKE FUNCTION
dat.rename(columns={'state.name': 'state_name'}, inplace=True)

# unique names of states MAKE FUNCTION
state_names = dat.state_name.unique()
state_names = state_names.tolist()

print(state_names)

print(type(state_names))

# plot data factored
scatplot_facet(x='year', y='rate_100000', facet_col='state_name',
                 hue='month', data=dat, title_main='Death rates by state',
                 x_label='Year', y_label='Death rate (per 100,000)')
