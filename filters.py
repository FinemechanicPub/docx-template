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
