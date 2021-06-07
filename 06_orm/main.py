from flask import Flask
from flask_restx import Api, Resource, reqparse, Model, fields
from flask_restx.inputs import positive
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

# Init SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlite.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

user_parser = reqparse.RequestParser(bundle_errors=True)
user_parser.add_argument("name",
                         type=str,
                         required=True,
                         nullable=False,
                         location="json",
                         help="User name.")
user_parser.add_argument("age",
                         type=positive,
                         default=18,
                         location="json",
                         help="User age.")
user_parser.add_argument("gender",
                         type=str,
                         choices=("male", "female"),
                         case_sensitive=False,
                         location="json",
                         help="User gender - male or female.")


user_fields = Model(
    "User data",
    {
        "id": fields.Integer(required=True),
        "name": fields.String(required=True),
        "age": fields.Integer(required=True)
    }
)

user_list_fields = Model(
    "User data list",
    {
        "users": fields.List(fields.Nested(user_fields)),
        "url": fields.Url(absolute=True)
    }
)


api.models[user_fields.name] = user_fields
api.models[user_list_fields.name] = user_list_fields


# Create User ORM model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=True)

    # Serialize object to json
    def get_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender
        }

    def __repr__(self):
        return "User with name {} is {}-years {}!".format(self.name, self.age, self.gender)


@api.route("/api/users")
class Users(Resource):
    _users = []

    @api.marshal_with(user_list_fields)
    def get(self):
        # Get users from database and save to list in json format
        users_list = [user.get_json() for user in User.query.all()]
        return {"users": users_list}, 200

    @api.expect(user_parser, validate=True)
    def post(self):
        args = user_parser.parse_args(strict=True)

        # Save to database
        user = User(**args)
        db.session.add(user)
        db.session.commit()

        return user.get_json(), 201, {"Location": "/api/users/{}".format(user.id)}


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8080)
