import tensorflow as tf


# create function to process data set
def input_fn(df, continuous_columns, categorical_columns, label):
    # Creates a dictionary mapping from each continuous feature column name (k) to
    # the values of that column stored in a constant Tensor.
    continuous_cols = {k: tf.constant(df[k].values) for k in continuous_columns}

    # Creates a dictionary mapping from each categorical feature column name (k)
    # to the values of that column stored in a tf.SparseTensor.
    categorical_cols = {k: tf.SparseTensor(
        indices=[[i, 0] for i in range(df[k].size)],
        values=df[k].values,
        shape=[df[k].size, 1])
                        for k in categorical_columns}

    # Merges the two dictionaries into one.
    feature_cols = dict(continuous_cols.items())
    feature_cols.update(categorical_cols.items())
    # Converts the label column into a constant Tensor.
    label = tf.constant(df[label].values)
    # Returns the feature columns and the label.
    return feature_cols, label
