from multi_var_regression.data.file_paths import *
from multi_var_regression.functions.ml_algorithms.log_regr import log_regr

# regression on one age group with features below
regr_1 = log_regr(TEMP_TEST_1, ['rate.adj', 'temperature'], ['year', 'sex', 'age', 'fips'], 'season')
print("success rate is %.3f " % regr_1)

# as above but with fewer age features
regr_2 = log_regr(TEMP_TEST_1, ['rate.adj'], ['sex', 'fips'], 'season')
print("success rate is %.3f " % regr_2)

# regression with all age groups with features below
regr_3 = log_regr(TEMP_TEST_1, ['rate.adj'], ['sex', 'fips'], 'season')
print("success rate is %.3f " % regr_3)

