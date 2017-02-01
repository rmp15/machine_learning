from linear.regression import run_csv_linear_regression

FILES_DIR = '/Users/rmiparks/morality'

ALL_AGES = [0, 5, 15, 25, 35]

def run_regression_on_all_ages():
    for a in ALL_AGES:
        run_age_regression(a)

def run_age_regression(age):
    # E.g. /Users/rmiparks/mortality/0.csv
    file_name = '%s/%d.csv' % (FILES_DIR, age)

    run_csv_linear_regression(file_name)
