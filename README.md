# pytest_ui_api_template

## Шаблон для автоматизации тестирования на python

### Шаги
1. Склонировать проект 'git clone https://github.com/имя_пользователя/
   pytest_ui_api_template.git'
2. Установить зависимости 'pip freeze > requirements.txt'
3. Запустить тесты 'python -m pytest'
4. Сгенерировать отчет 'allure generate allure-files -o allure-report'
5. Открыть отчет 'allure open allure-report'

### Стек:
- pytest
- selenium
- webdriver manager
- requests
- _sqlalchemy_
- allure
- configparser
- json

### Структура:
- ./test - тесты

- ./pages - описание страниц
- ./api - хелперы для работы с API
- ./db - хелперы для работы с БД (?)
- ./configuration - провайдер настроек
- ./testdata - провайдер тестовых данных
- pytest.ini - конфигурация для запуска тестов
- test_config.ini - настройки для тестов
- test_data.json - данные для тестов
- requirements.txt - список зависимостей (библиотеки)

### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore)
- [Про configparser](https://docs.python.org/3/library/configparser.html#configparser-objects)
- [pip freeze](https://pip.pypa.io/en/stable/cli/pip_freeze/)
