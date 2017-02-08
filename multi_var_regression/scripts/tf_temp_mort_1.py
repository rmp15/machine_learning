from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf
import pandas as pd

from multi_var_regression.data.file_paths import TEMP_MORT

# details of data set
COLUMNS = ['sex', 'age', 'year', 'month', 'fips', 'deaths', 'iso3', 'pop', 'pop.adj', 'rate',
           'rate.adj', 'rate.adj.old', 'leap', 'deaths.adj', 'variable', 'month.short', 'state.name']
FEATURES = ['year', 'month', 'fips']
LABEL = 'variable'

# Load data sets
training_set = pd.read_csv(TEMP_MORT, skipinitialspace=True,
                           skiprows=1, names=COLUMNS)
test_set = pd.read_csv(TEMP_MORT, skipinitialspace=True,
                       names=COLUMNS, skiprows=(training_set.shape[0] - 1000 + 1))

# create feature columns formally, confirming they are all real-valued
feature_cols = [tf.contrib.layers.real_valued_column(k)
                for k in FEATURES]

# instantiate a DNNRegressor for the neural network regression model.
regressor = tf.contrib.learn.DNNRegressor(
    feature_columns=feature_cols, hidden_units=[10, 10])

# create function to process data set
def input_fn(data_set):
  feature_cols = {k: tf.constant(data_set[k].values
                  for k in FEATURES}
  labels = tf.constant(data_set[LABEL].values)
  return feature_cols, labels
labels = input_fn(training_set)

print(labels)


# train the neural network regressor
regressor.fit(input_fn=lambda: input_fn(training_set), steps=5000)
