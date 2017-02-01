import pandas as pd
from data.file_paths import *
from functions.plot.sinplot import sineplot

dat = pd.read_csv(TEMP_TEST_1, index_col=0)

# plot sin data
sineplot()
