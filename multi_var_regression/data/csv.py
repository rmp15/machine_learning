import pandas as pd


def read_csv(file_path):
    data = pd.read_csv(file_path)

    return data


def read_two_col_csv(file_path):
    raw = read_csv(file_path)

    x = raw[:,0]
    y = raw[:,1]

    return x, y


def extract_train_test(data, n_tests):
    data = pd.DataFrame(data)
    train = data[:n_tests]
    test = data[-n_tests:]

    return train, test


def _reshape(col_data):
    return col_data.reshape((col_data.shape[0], 1))
