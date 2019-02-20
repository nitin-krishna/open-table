__author__ = '@nitin-krishna'

import pandas as pd
import itertools


def format_date(date):
    return pd.to_datetime(date).date()


def format_time(time):  # TODO: allow for flexible time formats
    return pd.to_datetime(time).time()


def repeat(fn, n):
    for _ in itertools.repeat(None, n):
        fn()
