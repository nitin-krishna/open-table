__author__ = '@nitin-krishna'

import pandas as pd


def format_date(date):
    return pd.to_datetime(date).date()


def format_time(time):  # TODO: allow for flexible time formats
    return time
