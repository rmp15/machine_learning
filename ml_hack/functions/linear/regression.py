from sklearn import linear_model

from ml_hack.data.csv import read_two_col_csv, extract_train_test


def run_csv_linear_regression(file_path):
    x, y = read_two_col_csv(file_path)

    # Split up data
    x_train, x_test = extract_train_test(x, 20)
    y_train, y_test = extract_train_test(y, 20)

    # Create linear regression object
    regr = linear_model.Ridge()

    # Train the model using the training sets
    regr.fit(x_train, y_train)

    return regr, x_test, y_test
