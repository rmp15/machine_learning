from multi_var_regression.data.file_paths import *
from multi_var_regression.functions.ml_algorithms import log_regr


log_regr(TEMP_TEST_1, ['rate.adj', 'temperature'], ['year', 'sex', 'age', 'fips'], 'season')