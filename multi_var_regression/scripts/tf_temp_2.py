# this script
# classifies a month as winter or non-winter
# attempts to use tf to predict from death rates

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tempfile

import pandas as pd
import tensorflow as tf

from multi_var_regression.data.categorical import *
from multi_var_regression.data.file_paths import *
from multi_var_regression.data.tf_input import input_fn

COLUMNS = ['sex', 'age', 'year', 'month', 'fips', 'rate.adj', 'temperature', 'season']
CONTINUOUS_COLUMNS = ['year', 'rate.adj', 'temperature']
CATEGORICAL_COLUMNS = ['sex', 'age', 'month', 'fips']
LABEL = 'season'

# Load data sets
training_set = pd.read_csv(TEMP_MORT, skipinitialspace=True,
                           skiprows=1, names=COLUMNS)
test_set = pd.read_csv(TEMP_MORT, skipinitialspace=True,
                       names=COLUMNS, skiprows=(training_set.shape[0] - 1000 + 1))

# define continuous columns in tf
year = tf.contrib.layers.real_valued_column("year")
rate_adj = tf.contrib.layers.real_valued_column("rate.adj")
temperature = tf.contrib.layers.real_valued_column("temperature")

# define categorical variables in tf
sex = tf.contrib.layers.sparse_column_with_keys(column_name="sex", keys=sexes)
age = tf.contrib.layers.sparse_column_with_keys(column_name="age", keys=ages)
month = tf.contrib.layers.sparse_column_with_keys(column_name="month", keys=months_short)
fips = tf.contrib.layers.sparse_column_with_keys(column_name="fips", keys=fips)

# make temporary file location
model_dir = tempfile.mkdtemp()

# defining the logistic regression model
m = tf.contrib.learn.LinearClassifier(feature_columns=[year, rate_adj, temperature, sex, age, month, fips], model_dir=model_dir)

#def train_input_fn():
#    return input_fn(training_set, CONTINUOUS_COLUMNS, CATEGORICAL_COLUMNS, LABEL)

def train_input_fn():
    return input_fn(training_set, ['year'], ['month'], LABEL)

#def eval_input_fn():
#    return input_fn(test_set, CONTINUOUS_COLUMNS, CATEGORICAL_COLUMNS, LABEL)

# train and evaluate model
m.fit(input_fn=train_input_fn, steps=200)
