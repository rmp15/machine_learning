from multi_var_regression.data.categorical import ages, sexes_long_2
from multi_var_regression.data.file_paths import TEMP_TEST, TEMP_TEST_B
from multi_var_regression.functions.data_manip.data_tools import data_append

test = data_append(TEMP_TEST_B, '1982_2013', ages, sexes_long_2, ages, )