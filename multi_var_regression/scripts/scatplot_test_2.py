import pandas as pd

from multi_var_regression.data.file_paths import TEMP_TEST_1
from multi_var_regression.functions.data_manip.rate_multiply import rate_multiply
from multi_var_regression.functions.plot.scatplot import scatplot_facet

dat = pd.read_csv(TEMP_TEST_1, index_col=0)

# create unique id based on year and month MAKE FUNCTION
dat['year_month'] = dat.year.astype(str) + dat.month.astype(str)

# create death rate per 100,000
rate_multiply(dat, 'rate.adj', 1000000)

# rename column names
dat.rename(columns={'state.name': 'state_name'}, inplace=True)

# unique names of states MAKE FUNCTION
state_names = dat.state_name.unique()
state_names = state_names.tolist()

print(state_names)

print(type(state_names))

# plot data factored
scatplot_facet(x='year', y='rate_1000000', facet_col='state_name',
                 hue='month', data=dat, title_main='Death rates by state',
                 x_label='Year', y_label='Death rate (per 1,000,000)')
