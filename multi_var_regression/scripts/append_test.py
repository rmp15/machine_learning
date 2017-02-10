import os

from multi_var_regression.data.categorical import ages, sexes_long_2
from multi_var_regression.data.file_paths import TEMP_TEST_B
from multi_var_regression.functions.data_manip.data_tools import data_append

# compile all ages for machine learning
complete = data_append(TEMP_TEST_B, '1982_2013', sexes_long_2, ages, 'mort_against_climate.csv')

# write to csv
complete.to_csv(os.path.join(str(TEMP_TEST_B), str('1982_2013'), 'mort_against_climate_complete.csv'))