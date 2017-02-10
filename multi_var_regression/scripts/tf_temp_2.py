# this script
# classifies a month as winter or non-winter
# attempts to use tf to predict from death rates

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import pandas as pd
import tensorflow as tf

from multi_var_regression.data.file_paths import TEMP_MORT

COLUMNS = ['sex', 'age', 'year', 'month', 'fips', 'rate.adj', 'temperature', 'season']
COLUMN_CLASSES = [[''], [''], [1], [''], [''], [1.0], [1.0], ['']]
CONTINUOUS_COLUMNS = ['sex', 'age', 'year', 'fips', 'rate.adj', 'temperature']
CATEGORICAL_COLUMNS = ['month']
LABEL = 'season'

# load data
training_set = pd.read_csv(TEMP_MORT, skipinitialspace=True,
                           skiprows=1, names=COLUMNS)


def my_input_fn():
    examples = tf.contrib.learn.graph_io.read_batch_examples(TEMP_MORT, 32, tf.TextLineReader)
    header = COLUMNS
    record_defaults = COLUMN_CLASSES
    cols = tf.decode_csv(examples, record_defaults=record_defaults)
    features = zip(header, cols)
    target = features.pop('season')
    return features, target

