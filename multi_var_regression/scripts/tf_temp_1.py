from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf
import pandas as pd
import itertools

from multi_var_regression.data.file_paths import TEMP_MORT

# details of data set
COLUMNS = ['sex', 'age', 'year', 'month', 'fips', 'deaths', 'iso3', 'pop', 'pop.adj', 'rate',
           'rate.adj', 'rate.adj.old', 'leap', 'deaths.adj', 'variable', 'month.short', 'state.name']
FEATURES = ['year', 'month', 'variable']
LABEL = 'rate.adj'

# Load data sets
training_set = pd.read_csv(TEMP_MORT, skipinitialspace=True,
                           skiprows=1, names=COLUMNS)
test_set = pd.read_csv(TEMP_MORT, skipinitialspace=True,
                       names=COLUMNS, skiprows=(training_set.shape[0] - 1000 + 1))
prediction_set = pd.read_csv(TEMP_MORT, skipinitialspace=True,
                       names=COLUMNS, skiprows=(training_set.shape[0] - 10 + 1))

# create feature columns formally, confirming they are all real-valued
feature_cols = [tf.contrib.layers.real_valued_column(k)
                for k in FEATURES]

# instantiate a DNNRegressor for the neural network regression model.
regressor = tf.contrib.learn.DNNRegressor(
    feature_columns=feature_cols, hidden_units=[10, 10])


# create function to process data set
def input_fn(data_set):
    feature_cols = {k: tf.constant(data_set[k].values)
                  for k in FEATURES}
    labels = tf.constant(data_set[LABEL].values)
    return feature_cols, labels

# train the neural network regressor
regressor.fit(input_fn=lambda: input_fn(training_set), steps=5000)

# evaluate the model fit
ev = regressor.evaluate(input_fn=lambda: input_fn(test_set), steps=1)
loss_score = ev["loss"]
print("Loss: {0:f}".format(loss_score))

# make predictions using the model
y = regressor.predict(input_fn=lambda: input_fn(prediction_set))
# .predict() returns an iterator; convert to a list and print predictions
predictions = list(itertools.islice(y, 10))
print("Predictions: {}".format(str(predictions)))

print(prediction_set.head())
