from flask import Flask
from flask_restx import Api, Resource, abort

# Create flask application
app = Flask(__name__)

# Create api as flask extension
api = Api(app)


@api.route("/my_resources", "/api/resources")
class MyResources(Resource):
    def get(self):
        return {"data": "MyResource - GET"}

    def post(self):
        return {"data": "MyResource - POST"}, 201


@api.route("/books/<int:book_id>")
class Books(Resource):
    def get(self, book_id):
        if book_id > 10:
            abort(404, "Book not found", my_field="My data")
        return {"id": book_id}


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8080)
