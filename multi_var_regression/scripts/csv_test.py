import pandas as pd

from multi_var_regression.data.file_paths import TEMP_TEST_1

dat = pd.read_csv(TEMP_TEST_1, index_col=0)

# print data
print(dat)


