import pandas as pd

from data.file_paths import *
from functions.plot import sinplot


dat = pd.read_csv(TEMP_TEST_1, index_col=0)

# print data
print(dat)

# plot sin data
sinplot()
