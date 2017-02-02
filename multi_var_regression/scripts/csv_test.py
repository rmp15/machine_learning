import pandas as pd
import seaborn as sns
from data.file_paths import *

# load data
dat = pd.read_csv(TEMP_TEST_1, index_col=0)

# print data
print(dat)


