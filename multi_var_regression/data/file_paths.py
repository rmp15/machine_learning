import os

# Data sets

# tf test data
IRIS_TRAINING = "/Users/rmiparks/git/machine_learning/multi_var_regression/data/iris_training.csv"
IRIS_TEST = "/Users/rmiparks/git/machine_learning/multi_var_regression/data/iris_test.csv"

# tf mortality data test
TEMP_TEST = "/Users/rmiparks/git/mortality/USA/state/output/mort_against_climate/t2m/mean/1982_2013/"
TEMP_TEST_B = "/Users/rmiparks/git/mortality/USA/state/output/mort_against_climate/t2m/mean/"
DATA = os.path.join(TEMP_TEST, "male", "85", 'mort_against_climate_85_1_1982_2013_t2m_mean.csv')

# ADAPT TO GENERALISE TO EVERY COMBINATION POSSIBLE
TEMP_TEST_1 = os.path.join(TEMP_TEST, "male", "85", 'mort_against_climate_85_1_1982_2013_t2m_mean.csv')
TEMP_TEST_2 = os.path.join(TEMP_TEST, "male", "25", 'mort_against_climate_25_1_1982_2013_t2m_mean.csv')

