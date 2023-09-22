from sys import argv, exit

from docxtpl import DocxTemplate
from jinja2 import exceptions as je
from json import JSONDecodeError, load

import jinja2


HELP_MESSAGE = (
    "Jinja2 template processor for DOCX files.\n"
    "Usage: make_doc source.json template.docx output.docx"
)
    
TEMPLATE_NAME_ERROR = "Заданы одинаковые имена для шаблона и файла результата"
JSON_ERROR = "Ошибка загрузки JSON: {message}"
SYNTAX_ERROR = (
    "Синтаксическая ошибка в шаблоне: {message}\n"
    "Область ошибки: {context}"
)
UNDEFINED_ERROR = "Ошибка определения в шаблоне: {message}"
TEMPLATE_ERROR = "Ошибка обработки шаблона: {message}"
GENERAL_ERROR = "Ошибка: {message}"
               

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
    print(HELP_MESSAGE)
    exit(1)

json_file = argv[1]
template = argv[2]
out_file = argv[3]

try:
    if (template == out_file):
        raise ValueError(TEMPLATE_NAME_ERROR)

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
    print(JSON_ERROR.format(message=error))
except je.UndefinedError as error:
    print(SYNTAX_ERROR.format(message=error.message))
except je.TemplateError as error:
    if hasattr(error, "docx_context") and hasattr(error, "lineno"):
        line = [line for line in error.docx_context][3 + min(error.lineno - 4, 0)]
        print(SYNTAX_ERROR.format(message=error.message, context=line))
    else:
        print(TEMPLATE_ERROR(message=error))
except Exception as error:
    print(GENERAL_ERROR.format(message=error))

exit(1)
