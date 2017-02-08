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

COLUMNS = ['sex', 'age', 'year', 'month', 'fips', 'deaths', 'iso3', 'pop', 'pop.adj', 'rate',
           'rate.adj', 'rate.adj.old', 'leap', 'deaths.adj', 'variable', 'month.short', 'state.name', 'season']
FEATURES = ['year', 'month', 'variable']
LABEL = 'season'

CONTINUOUS_COLUMNS = ['deaths', 'pop', 'year', 'pop.adj', 'rate', 'rate.adj', 'rate.adj.old', 'deaths.adj', 'variable']
CATEGORICAL_COLUMNS = ['sex', 'age', 'month', 'fips', 'iso3', 'leap', 'month.short', 'state.name']

# Load data sets
training_set = pd.read_csv(TEMP_MORT, skipinitialspace=True,
                           skiprows=1, names=COLUMNS)
test_set = pd.read_csv(TEMP_MORT, skipinitialspace=True,
                       names=COLUMNS, skiprows=(training_set.shape[0] - 1000 + 1))

# define categorical variables in tf
sex = tf.contrib.layers.sparse_column_with_keys(column_name="sex", keys=sexes)
age = tf.contrib.layers.sparse_column_with_keys(column_name="age", keys=ages)
month = tf.contrib.layers.sparse_column_with_keys(column_name="month", keys=months)
fips = tf.contrib.layers.sparse_column_with_keys(column_name="fips", keys=fips)

# define continuous columns in tf
deaths_adj = tf.contrib.layers.real_valued_column("deaths.adj")
pop_adj = tf.contrib.layers.real_valued_column("pop.adj")
rate_adj = tf.contrib.layers.real_valued_column("rate.adj")
temperature = tf.contrib.layers.real_valued_column("variable")

# make temporary file location
model_dir = tempfile.mkdtemp()

# defining the logistic regression model
m = tf.contrib.learn.LinearClassifier(feature_columns=[sex, age, month, fips, rate_adj, temperature],
                                      model_dir=model_dir)

# train and evaluate model
m.fit(input_fn=input_fn(training_set, CONTINUOUS_COLUMNS, CATEGORICAL_COLUMNS, LABEL), steps=200)
