#Based on:
#https://medium.com/@ilblackdragon/tensorflow-tutorial-part-4-958c29c717a0#.g539govuk

# NEED TO FIX THIS FOR CONTINUOUS OUTPUT
def regr(DATA,CONTINUOUS_COLUMNS, CATEGORICAL_COLUMNS, LABEL):

    import random

    import pandas as pd
    import tensorflow as tf
    from sklearn.cross_validation import train_test_split
    from sklearn.metrics import accuracy_score
    from sklearn.preprocessing import LabelEncoder
    from tensorflow.contrib import layers
    from tensorflow.contrib import learn

    # load data
    train = pd.read_csv(DATA)
    y = train.pop(LABEL)

    # Drop all unique columns. List all variables for future reference.
    CONTINUOUS_COLUMNS = CONTINUOUS_COLUMNS
    CATEGORICAL_COLUMNS = CATEGORICAL_COLUMNS
    X = train[CATEGORICAL_COLUMNS + CONTINUOUS_COLUMNS].fillna(0)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


    # Pandas input function.
    def pandas_input_fn(x, y=None, batch_size=128, num_epochs=None):
        def input_fn():
            if y is not None:
                x['target'] = y
            queue = tf.contrib.learn.dataframe.queues.feeding_functions.enqueue_data(
                x, 1000, shuffle=num_epochs is None, num_epochs=num_epochs)
            if num_epochs is None:
                features = queue.dequeue_many(batch_size)
            else:
                features = queue.dequeue_up_to(batch_size)
            features = dict(zip(['index'] + list(x.columns), features))
            if y is not None:
                target = features.pop('target')
                return features, target
            return features

        return input_fn


    # Process categorical variables into ids.
    X_train = X_train.copy()
    X_test = X_test.copy()
    categorical_var_encoders = {}

    for var in CATEGORICAL_COLUMNS:
        le = LabelEncoder().fit(X_train[var])
        X_train[var + '_ids'] = le.transform(X_train[var])
        X_test[var + '_ids'] = le.transform(X_test[var])
        X_train.pop(var)
        X_test.pop(var)
        categorical_var_encoders[var] = le

    CATEGORICAL_EMBED_SIZE = 10  # Note, you can customize this per variable.


    # 3 layer neural network with hyperbolic tangent activation.
    def dnn_tanh(features, target):
        target = tf.one_hot(target, 2, 1.0, 0.0)
        # Organize continues features.
        final_features = [tf.expand_dims(tf.cast(features[var], tf.float32), 1) for var in CONTINUOUS_COLUMNS]
        # Embed categorical variables into distributed representation.
        for var in CATEGORICAL_COLUMNS:
            feature = learn.ops.categorical_variable(
                features[var + '_ids'], len(categorical_var_encoders[var].classes_),
                embedding_size=CATEGORICAL_EMBED_SIZE, name=var)
            final_features.append(feature)
        # Concatenate all features into one vector.
        features = tf.concat(1, final_features)
        # Deep Neural Network
        logits = layers.stack(features, layers.fully_connected, [10, 20, 10],
                              activation_fn=tf.tanh)
        prediction, loss = learn.models.logistic_regression(logits, target)
        train_op = layers.optimize_loss(loss,
                                        tf.contrib.framework.get_global_step(), optimizer='SGD', learning_rate=0.05)
        return tf.argmax(prediction, dimension=1), loss, train_op


    random.seed(42)
    classifier = learn.Estimator(model_fn=dnn_tanh)

    # Note: not training this almost at all.
    classifier.fit(input_fn=pandas_input_fn(X_train, y_train), steps=1000)
    preds = list(classifier.predict(input_fn=pandas_input_fn(X_test, num_epochs=1), as_iterable=True))

    result = accuracy_score(y_test, preds)
    print(result)

    return result
