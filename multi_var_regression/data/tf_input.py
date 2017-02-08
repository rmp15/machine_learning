import tensorflow as tf


# create function to process data set
def input_fn(df, CONTINUOUS_COLUMNS, CATEGORICAL_COLUMNS, LABEL):

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
    d = dict(continuous_cols.items())
    d.update(categorical_cols.items())
    feature_cols = d
    # Converts the label column into a constant Tensor.
    label = tf.constant(df[LABEL].values)
    # Returns the feature columns and the label.
    return feature_cols, label
