# Шаблонизатор для документов в формате DOCX

Представляет собой небольшую надстройку над проектом [python-docx-template](https://github.com/elapouya/python-docx-template). Проект предназначен для сборки в исполняемый файл с помощью [PyInstaller](https://pyinstaller.org/en/stable/).

Функционально надстройка добавляет несколько фильтров для Jinja2 и сигнализирует об ошибках кодами завершения программы.

## Сборка проекта

Создание окружения
```bash
python -m venv venv
```

Установка зависимостей
```bash
pip install -r requirements.txt
```

Сборка
```bash
pyinstaller make_doc.spec
```

В случае успешного завершения сборки готовый файл будет помещен в директорию `dist`.

## Использование

Шаблонизатор заополняет шаблон данными из `json`-файла и сохраняет готовый документ под заданным именем. Три указанных файла пердаются в качестве параметров командной строки:
```shell
make_doc source.json template.docx output.docx
```