# Flask-RESTX tutorial

**Оглавление:**

1. [Установка Flask-RESTX в виртуальную среду](../01_virtual_environment/README.md)
2. [Первое приложение](../02_first_application/README.md)
3. Создание и добавление ресурсов
4. [Парсинг данных запроса](../04_request_parsing/README.md)
5. [Маршалинг и форматирование выходных данных](../05_marshalling/README.md)
6. [Объектно-реляционное отображение (ORM)](../06_orm/README.md)

---

## 3. Создание и добавление ресурсов

Ресурс — это все элементы REST API, к которым можно получить доступ с помощью URL-адреса. 
Адрес однозначно идентифицирует ресурс, а для указания [действия](http://spring-projects.ru/understanding/rest/) выполняемого над ресурсом используются стандартные [методы HTTP запросов](https://developer.mozilla.org/ru/docs/Web/HTTP/Methods):
* GET — получение ресурса.
* POST — создание ресурса.
* DELETE — удаление ресурса.
* PUT — изменение ресурса с обязательным использованием всех полей.
* PATCH — изменение ресурса с использованием некоторых полей.
* OPTIONS — определение поддерживаемых действий над ресурсом.
* HEAD — проверка факта изменения ресурса без возвращения данных ресурса.

Для создания ресурса требуется объявить новый класс, [наследованный](https://pythonworld.ru/osnovy/dekoratory.html) от класса `Resource`, который доступен во фреймворке:

```python
from flask_restx import Resource

class MyResources(Resource):
    pass
```

> Примечание: оператор `pass` — [оператор-заглушка](https://www.programiz.com/python-programming/pass-statement), равноценен отсутствию операции, используется в местах, где синтаксически требуется указать оператор.

Для добавления возможных действий над ресурсом необходимо определить в классе методы HTTP с соответствующими именами в нижнем регистре:

```python
from flask_restx import Resource

class MyResources(Resource):
    def get(self):
        pass

    def post(self):
        pass
```

> Примечание фреймворк автоматически добавляет метод для обработки запроса OPTIONS, а при добавлении метода get обрабатывается запрос GET и HEAD.

Методы должны возвращать в общем случае кортеж из трех значений: 
1. Тело ответа — json объект в виде словаря (dict).
2. [Код состояния](https://restfulapi.net/http-status-codes/) ответа — целое число.
3. Заголовки ответа — json объект в виде словаря (dict).

> Примечание: фреймворк позволяет использовать другой тип в качестве тела ответа, а также указывать несуществующие в спецификации HTTP коды статуса ответа.

При этом допускается указывать не все значения кортежа, тогда для остальных элементов будут применены значения по-умолчанию:

```python
from flask_restx import Resource

class MyResources(Resource):
    def get(self):
        return {"data": "MyResources - GET"}

    def post(self):
        return {"data": "MyResources - POST"}, 201
```

После объявления ресурса — необходимо назначить ему адрес, это можно сделать следующими способами: 
1. Вызвать метод `add_resource` созданного экземпляра `Api` после объявления класса.
    ```python
    class MyResources(Resource):
        def get(self):
            return {"data": "MyResource - GET"}
   
    api.add_resource(MyResources, "/my_resources")
    ```
2. Использовать готовый [декоратор](https://pythonworld.ru/osnovy/dekoratory.html), который доступен у созданного экземпляра `Api`, перед объявлением класса.
    ```python
    @api.route("/my_resources")
    class MyResources(Resource):
        def get(self):
            return {"data": "MyResources - GET"}
    ```

Результат работы приведенных примеров одинаков и ничем не отличается, созданный ресурс будет доступен по адресу: [http://127.0.0.1:8080/my_resources](http://127.0.0.1:8080/my_resources).
Также в документации Swagger появятся соответствующие записи о добавленных ресурсах. 

Для ресурсов можно указать несколько адресов через запятую, в таком случае ресурс будет доступен по нескольким адресам сразу:
```python
@api.route("/my_resources", "/api/resources")
```
или
```python
api.add_resource(MyResources, "/my_resources", "/api/resources")
```

### Получение идентификатора из адреса ресурса

Если адрес ресурса содержит его идентификатор, то необходимо использовать строку со специальными конструкциями внутри нее, а также добавить необходимые аргументы в методы:

```python
@api.route("/books/<int:book_id>")
class Books(Resource):
    def get(self, book_id):
        return {"id": book_id}
```
Ресурс в данном примере доступен по любому адресу вида: [/books/0](http://127.0.0.1:8080/books/1), [/books/1](http://127.0.0.1:8080/books/2), [/books/9999](http://127.0.0.1:8080/books/9999) и других аналогичных адресов.

При указании адреса ресурса использовалась подстрока вида `<var_type:var_name>`, где `var_type` — определяет тип значения, `var_name` — название переменной в которую Flask передаст полученное обработанное значение. Также в методы обработки запросов данного класса необходимо добавить в качестве аргумента `var_name` не изменяя имени.

> Примечание: указание типа можно опустить, тогда будет использоваться тип `default`, пример правила без указания типа: `"/article/<name_article>"`

Указание типа необходимо для фильтрации значений, которые не подходят под заданный тип. Существуют следующие типы с их дополнительными параметрами: 
* int — целое положительное
   * fixed_digit — количество цифр в числе
   * min — минимальное значение
   * max — максимальное значение
   * signed — разрешить отрицательные значения (True, False)
* string — строка одного сегмента (не содержит косую черту);
   * minlength — минимальная длина строки
   * maxlength — максимальная длина строки
   * length — задать фиксированную длину строки
* float — неотрицательное дробное число в формате с точкой;
   * min — минимальное значение
   * max — максимальное значение
   * signed — разрешить отрицательные значения (True, False)
* uuid — универсальный уникальный идентификатор (UUID);
* path — строка нескольких сегментов (может содержать косую черту);
* any — строка, соответствующая заданному перечислению строк, указанного в параметрах
* default — значение по-умолчанию, соответствует типу string.

> Примеры использования типа с дополнительными параметрами: 
>
> `<string(minlength=3,maxlength=10):name>`
> 
> `<any(about, help):page_name>`
> 
> `<int(signed=True):value>`

В строке ресурса также можно указывать более одного такого правила: `"/year/<int:year_val>/day/<int:day_val>"`.
В этом случае необходимо добавить оба аргумента в методы класса, например: `def get(self, year_val, day_val)` 

**Прерывание обработки текущего запроса**

В случае возникновения 4XX или 5XX ошибок необходимо использовать функцию `abort` для завершения обработки запроса. Первым параметром передается код статуса ответа, в качестве второго передается сообщение об ошибке, также можно добавлять другие именованные параметры, которые будут включены в выходные данные.

```python
from flask_restx import abort

@api.route("/books/<int:book_id>")
class Books(Resource):
    def get(self, book_id):
        if book_id > 10:
            abort(404, "Book not found", my_field="My data")
        return {"id": book_id}
```

> Примечание: список кодов ответов, обрабатываемых функцией `abort()`, доступен по [ссылке](https://werkzeug.palletsprojects.com/en/1.0.x/exceptions/#error-classes).

---

Пример кода к данному параграфу доступен [тут](./main.py).
