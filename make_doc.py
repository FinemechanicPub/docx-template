from inspect import getmembers, isfunction
from sys import argv, exit

from docxtpl import DocxTemplate
from jinja2 import Environment, exceptions as je
from json import JSONDecodeError, load

import filters

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


def process_template():
    if len(argv) < 4:
        return(HELP_MESSAGE)
    json_file, template, out_file = argv[1:4]

    try:
        if (template == out_file):
            raise ValueError(TEMPLATE_NAME_ERROR)

        environment = Environment()

        for name, fun in getmembers(filters, isfunction):
            environment.filters[name] = fun

        doc = DocxTemplate(template)

        with open(json_file, "r", encoding="utf8") as file:
            json_data = load(file)
        doc.render(context=json_data, jinja_env=environment)
        doc.save(out_file)
        return

    except JSONDecodeError as error:
        return JSON_ERROR.format(message=error)
    except je.UndefinedError as error:
        return UNDEFINED_ERROR.format(message=error.message)
    except je.TemplateError as error:
        if hasattr(error, "docx_context") and hasattr(error, "lineno"):
            lines = [line for line in error.docx_context]
            index = 3 + min(error.lineno - 4, 0)
            return SYNTAX_ERROR.format(
                message=error.message,
                context=lines[index] if abs(index) < len(lines) else ""
            )
        else:
            return TEMPLATE_ERROR.format(message=error)
    except Exception as error:
        return GENERAL_ERROR.format(message=error)


if __name__ == "__main__":
    message = process_template()
    if (message):
        print(message)
        exit(1)
    exit(0)
