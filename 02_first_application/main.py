from flask import Flask
from flask_restx import Api

# Create flask application
app = Flask(__name__)

# Create api as flask extension
api = Api(app)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8080)
