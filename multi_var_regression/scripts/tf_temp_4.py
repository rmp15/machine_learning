from multi_var_regression.data.file_paths import *
from multi_var_regression.functions.ml_algorithms.log_regr import log_regr

regr_1 = log_regr(TEMP_TEST_1, ['rate.adj', 'temperature'], ['year', 'sex', 'age', 'fips'], 'season')
print("success rate is %.3f " % regr_1)

regr_2 = log_regr(TEMP_TEST_1, ['rate.adj'], ['sex', 'fips'], 'season')
print("success rate is %.3f " % regr_2)
