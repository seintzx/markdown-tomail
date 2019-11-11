#!/usr/bin/env python3

import datetime as dt


def get_date():
    past_month = format(dt.date.today().replace(day=1) - dt.timedelta(days=1),
                        '%B')
    past_nmonth = format(dt.date.today().replace(day=1) - dt.timedelta(days=1),
                         '%m')
    curr_month = format(dt.date.today().replace(day=1), '%B')
    curr_nmonth = format(dt.date.today().replace(day=1), '%m')
    curr_year = format(dt.date.today().replace(day=1), '%Y')
    return ([past_month, past_nmonth, curr_month, curr_nmonth, curr_year])
