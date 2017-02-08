from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import itertools

import pandas as pd
import tensorflow as tf

from multi_var_regression.data.file_paths import TEMP_MORT

# details of data set
COLUMNS = ['sex', 'age', 'year', 'month', 'fips', 'deaths', 'iso3', 'pop', 'pop.adj', 'rate',
           'rate.adj', 'rate.adj.old', 'leap', 'deaths.adj', 'variable', 'month.short', 'state.name']
FEATURES = ['year', 'month', 'variable']
LABEL = 'rate.adj'

CONTINUOUS_COLUMNS = ['deaths', 'pop', 'pop.adj', 'rate', 'rate.adj', 'rate.adj.old', 'deaths.adj', 'variable']
CATEGORICAL_COLUMNS = ['sex', 'age', 'year', 'month', 'fips', 'iso3', 'leap', 'month.short', 'state.name']

# define details
sexes = ["1", "2"]
ages = ["0", "5", "15", "25", "35", "45", "55", "65", "75", "85"]

# define categorical variables in tf
sex = tf.contrib.layers.sparse_column_with_keys(column_name="sex", keys=sexes)
age = tf.contrib.layers.sparse_column_with_keys(column_name="age", keys=ages)
year = tf.contrib.layers.sparse_column_with_keys(column_name="age", keys=ages)
month =
iso3 =
leap =



# Load data sets
training_set = pd.read_csv(TEMP_MORT, skipinitialspace=True,
                           skiprows=1, names=COLUMNS)
test_set = pd.read_csv(TEMP_MORT, skipinitialspace=True,
                       names=COLUMNS, skiprows=(training_set.shape[0] - 1000 + 1))
prediction_set = pd.read_csv(TEMP_MORT, skipinitialspace=True,
                       names=COLUMNS, skiprows=(training_set.shape[0] - 10 + 1))

# create function to process data set
def input_fn(df):

    # Creates a dictionary mapping from each continuous feature column name (k) to
    # the values of that column stored in a constant Tensor.
    continuous_cols = {k: tf.constant(df[k].values)
                         for k in CONTINUOUS_COLUMNS}
    # Creates a dictionary mapping from each categorical feature column name (k)
    # to the values of that column stored in a tf.SparseTensor.
    categorical_cols = {k: tf.SparseTensor(
        indices=[[i, 0] for i in range(df[k].size)],
        values=df[k].values,
        shape=[df[k].size, 1])
                          for k in CATEGORICAL_COLUMNS}
    # Merges the two dictionaries into one.
    feature_cols = dict(continuous_cols.items() + categorical_cols.items())
    # Converts the label column into a constant Tensor.
    label = tf.constant(df[LABEL_COLUMN].values)
    # Returns the feature columns and the label.
    return feature_cols, label



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
