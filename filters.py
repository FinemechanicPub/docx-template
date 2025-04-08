"""Дополнительные фильтры для Jinja2"""


def s(value):
    if value is None:
        return ""
    else:
        return int(round(value, 0))


def zs(value):
    if not value:
        return ""
    else:
        return int(round(value, 0))


def d(value):
    if value is None:
        return "-"
    else:
        return int(round(value, 0))


def zd(value):
    if not value:
        return "-"
    else:
        return int(round(value, 0))


def f(value, if_none, if_nan, if_big, if_small):
    if value is None:
        return if_none
    if value != value:
        return if_nan
    if value == float("inf"):
        return if_big
    if value == float("-inf"):
        return if_small
    return int(round(value, 0))
