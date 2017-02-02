import matplotlib.pyplot as plt
import pandas as pd

from data.file_paths import *

# load data
dat = pd.read_csv(TEMP_TEST_1, index_col=0, nrows=1000)

# create unique id based on year and month
dat['year_month'] = dat.year.astype(str) + '_' + dat.month.astype(str)

print(dat)

dat.set_index('year_month').plot("rate.adj")

plt.show()

# plot data factored
#scatplot_facet('year_month', 'rate.adj', facet_row='age', facet_col='state.name', hue='month', data=dat)

