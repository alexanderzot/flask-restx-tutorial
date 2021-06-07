# Flask-RESTX tutorial

**Оглавление:**

1. Установка Flask-RESTX в виртуальную среду
2. [Первое приложение](../02_first_application/README.md)
3. [Создание и добавление ресурсов](../03_creating_resources/README.md)
4. [Парсинг данных запроса](../04_request_parsing/README.md)
5. [Маршалинг и форматирование выходных данных](../05_marshalling/README.md)
6. [Объектно-реляционное отображение (ORM)](../06_orm/README.md)

---

## 1. Установка Flask-RESTX в виртуальную среду

[Flask-RESTX](https://flask-restx.readthedocs.io/en/latest/quickstart.html#migrate-from-flask-restplus) — это расширение Flask для создания REST API, является форком другого расширения [Flask-RESTPlus](https://flask-restplus.readthedocs.io/en/stable/), которое не обновляется с 2019 года.

1. Создание новой виртуальной среды для Python 3:
```bash
python3 -m venv flask_restx_tutorial
``` 

Подробнее про виртуальные среды можно прочитать [тут](https://python-scripts.com/virtualenv).

2. Запуск виртуальной среды:
```bash
source flask_restx_tutorial/bin/activate
```

После запуска виртуальной среды — введенные команды в текущей командной оболочке (терминале) будут в первую очередь выполняться в этой среде. Если команда в среде не найдена, то запустится команда из операционной системы, как в случае, когда выполняется команда в терминале без запущенной виртуальной среды. В связи с этим команды python и pip будут запускаться из изолированной от остальной системы среды, поэтому управление пакетами с помощью [пакетного менеджера pip](https://pip.pypa.io/en/stable/quickstart/) будет происходить только для активной виртуальной среды.  

3. Обновление пакетного менеджера Python:
```bash
python -m pip install --upgrade pip
```

4. Установка Flask-RESTX:
```bash
pip install flask-restx
```

Необходимые зависимости для работы пакета устанавливаются автоматически.

5. Запуск скрипта, например `main.py`, происходит следующим образом:
```bash
python main.py
```
