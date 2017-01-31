import pandas as pd

from data.file_paths import *

dat = pd.read_csv(TEMP_TEST_1, index_col=0)

print(dat)

