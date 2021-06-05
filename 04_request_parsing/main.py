from flask import Flask
from flask_restx import Api, Resource, reqparse
from flask_restx.inputs import positive

# Create flask application
app = Flask(__name__)

# Create api as flask extension
api = Api(app)

# Create parser for user data
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


@api.route("/api/users")
class Users(Resource):
    # In-memory database
    _users = []

    def get(self):
        return {"users": self._users}, 200

    @api.expect(user_parser, validate=True)
    def post(self):
        args = user_parser.parse_args(strict=True)

        # Create new user
        user_id = len(self._users)
        user = {
            "id": user_id,
            "name": args["name"],
            "age": args["age"],
            "gender": args["gender"]
        }

        # Save user to in-memory database
        self._users.append(user)

        # Return created user data with location in header
        return user, 201, {"Location": "/api/users/{}".format(user_id)}


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8080)
