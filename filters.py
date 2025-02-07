"""Дополнительные фильтры для Jinja2"""

NO_CONVERT = [float("inf"), float("-inf"), float("nan")]

def s(value):
    if value is None:
        return ""
    else:
        return int(round(value, 0)) if value not in NO_CONVERT else value


def zs(value):
    if not value:
        return ""
    else:
        return int(round(value, 0)) if value not in NO_CONVERT else value


def d(value):
    if value is None:
        return "-"
    else:
        return int(round(value, 0)) if value not in NO_CONVERT else value


def zd(value):
    if not value:
        return "-"
    else:
        return int(round(value, 0)) if value not in NO_CONVERT else value
