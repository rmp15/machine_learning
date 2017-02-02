def rate_multiply(data, rate_col, multiply_factor):

    # create death rate per multiplicative factor
    name = 'rate_' + str(multiply_factor)
    data[name] = data[rate_col] * multiply_factor
