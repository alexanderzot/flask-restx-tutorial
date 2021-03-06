# Flask-RESTX tutorial

**Оглавление:**

1. [Установка Flask-RESTX в виртуальную среду](../01_virtual_environment/README.md)
2. Первое приложение
3. [Создание и добавление ресурсов](../03_creating_resources/README.md)
4. [Парсинг данных запроса](../04_request_parsing/README.md)
5. [Маршалинг и форматирование выходных данных](../05_marshalling/README.md)
6. [Объектно-реляционное отображение (ORM)](../06_orm/README.md)

---

## 2. Первое приложение

Исходный код main.py:
```python
from flask import Flask
from flask_restx import Api

app = Flask(__name__)
api = Api(app)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8080)
```

Для создания основы сервера необходимо создать экземпляр класса `Flask`. 
Чтобы подключить расширение Flask-RESTX, необходимо импортировать соответствующий пакет, а затем создать экземпляр класса `Api`, передав ему экземпляр основного класса.

> Аргумент `name` необходим для Flask для определения корневого каталога приложения, чтобы с его помощью находить файлы ресурсов. 

Для запуска сервера, вызывается метод `run` у экземпляра `app`, которому передаем в качестве аргументов параметры запуска. 
Параметр `host` задает адрес на котором запустится сервер, а `port` задает номер порта.
При установке значения `debug` включается режим отладки, который обеспечивается автоматическую перезагрузку кода, что позволяет не перезагружать программу при каждом изменении кода, а также выводит дополнительные сообщения об ошибках. 

При переходе по адресу [http://127.0.0.1:8080/](http://127.0.0.1:8080/) — откроется страница с интерактивной документацией созданной автоматически с помощью [Swagger](https://en.wikipedia.org/wiki/Swagger_(software)), которая пока не содержит никакой полезной информации, так как мы не добавляли ресурсы. 
В будущем на странице будет появляться документация к созданному API по мере добавления новых возможностей.

---

Пример кода к данному параграфу доступен [тут](./main.py).
