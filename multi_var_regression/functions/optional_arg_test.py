def opt_fun(x1, x2, *positional_parameters, **keyword_parameters):
    if 'optional' in keyword_parameters:
        print('optional parameter found, it is ', keyword_parameters['optional'])
    else:
        print('no optional parameter, sorry')