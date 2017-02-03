import pandas as pd

# multiplies a rate by a chosen number
def rate_multiply(data, rate_col, multiply_factor):

    # create death rate per multiplicative factor
    name = 'rate_' + str(multiply_factor)
    data[name] = data[rate_col] * multiply_factor


# creates a unique numbered key from two columns in a data frame
# NEED TO FIX
def compound_key(data, col1, col2):

    # compound cell values
    data[col1 + '_' + col2] = str(data[col1]) + str(data[col2])
    data[col1 + '_' + col2] = pd.factorize(data[col1 + '_' + col2])[0] + 1


# creates unique names from a column in a data frame
# NEED TO FIX
def unique_names(data, col):
    names = data.col.unique()
    names = names.tolist()

    print(state_names)

    print(type(state_names))