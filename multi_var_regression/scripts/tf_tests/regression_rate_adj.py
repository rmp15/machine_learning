import time

from multi_var_regression.data.file_paths import *
from multi_var_regression.functions.ml_algorithms.regr import regr

# regression on one age group with features below
start = time.perf_counter()
regr_1 = regr(TEMP_TEST_1, ['rate.adj', 'temperature'], ['year', 'sex', 'age', 'fips'], 'season')
elapsed = round(time.perf_counter() - start,3)
print("success rate is %.3f and it took %.3f seconds" % (regr_1, elapsed))

# as above but with fewer age features
regr_2 = regr(TEMP_TEST_1, ['rate.adj'], ['sex', 'fips'], 'season')
print("success rate is %.3f " % regr_2)

# regression with all age groups with features below
start = time.perf_counter()
regr_3 = regr(os.path.join(str(TEMP_TEST_B), str('1982_2013'), 'mort_against_climate_complete.csv'),
                  ['rate.adj', 'variable'], ['year', 'sex', 'age', 'fips'], 'season')
elapsed = round(time.perf_counter() - start,3)
print("success rate is %.3f and it took %.3f seconds" % (regr_3, elapsed))

# regression with all age groups with using year numeric (for forecasting)
start = time.perf_counter()
regr_4 = regr(os.path.join(str(TEMP_TEST_B), str('1982_2013'), 'mort_against_climate_complete.csv'),
                  ['rate.adj', 'variable'], ['sex', 'age', 'fips'], 'season')
elapsed = round(time.perf_counter() - start,3)
print("success rate is %.3f and it took %.3f seconds" % (regr_4, elapsed))
