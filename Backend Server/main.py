import pymysql
import http
from app import app
from db_config import bcrypt
from db_config import mysql
from flask import jsonify
from flask import flash, request

# pw_hash = bcrypt.generate_password_hash("hunter2").decode("utf-8")
# print(bcrypt.check_password_hash(pw_hash, 'hunter2'))
# print(bcrypt.check_password_hash(pw_hash, 'false'))
# print(pw_hash)


@app.route("/", methods=["GET"])
def index():
    return "Welcome to Lights and Lock's Server!"


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    response = jsonify(message)
    response.status_code = 404
    return response


if __name__ == "__main__":
    app.run(debug=True)
