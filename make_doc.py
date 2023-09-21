from sys import argv, exit

from docxtpl import DocxTemplate
from jinja2 import exceptions as je
from json import JSONDecodeError, load

import jinja2


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


if len(argv) < 4:
    print("Jinja2 template processor for DOCX files.")
    print("Usage: make_doc source.json template.docx output.docx")
    exit(1)

json_file = argv[1]
template = argv[2]
out_file = argv[3]

try:
    if (template == out_file):
        raise ValueError(
            "заданы одинаковые имена для шаблона и файла результата"
        )

    environment = jinja2.Environment()
    environment.filters['s'] = s
    environment.filters['zs'] = zs
    environment.filters['d'] = d
    environment.filters['zd'] = zd
    doc = DocxTemplate(template)

    with open(json_file, "r", encoding="utf8") as file:
        json_data = load(file)
    doc.render(context=json_data, jinja_env=environment)
    doc.save(out_file)
    exit(0)
except JSONDecodeError as error:
    print(f"Ошибка загрузки JSON: {error}")
except je.TemplateSyntaxError as error:
    print(
        f"Синтаксическая ошибка в шаблоне:"
        f"{error.message}"
    )
except je.UndefinedError as error:
    print(f"Ошибка определения в шаблоне: {error.message}")
except je.TemplateError as error:
    print(f"Ошибка обработки шаблона: {error.message}")
except Exception as error:
    print(f"Ошибка: {error}")

exit(1)
