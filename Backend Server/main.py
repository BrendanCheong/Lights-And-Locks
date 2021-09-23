import pymysql
import http
import os
from pymongo import MongoClient
from app import app
from flask import jsonify, flash, request
from app import app
# NOTE:change this to db_local_config (if needed) for those who cannot connect to our AWS RDS and call the Initalise database GET route
from db_config import *
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt

# pw_hash = bcrypt.generate_password_hash("hunter2").decode("utf-8")
# print(bcrypt.check_password_hash(pw_hash, 'hunter2'))
# print(bcrypt.check_password_hash(pw_hash, 'false'))
# print(pw_hash)


@app.route("/", methods=["GET"])
def index():
    return jsonify(Welcome="Welcome to Lights and Lock's Server!")


@app.route('/api/Customer/add', methods=['POST'])
def add_user():
    conn = mysql.connection  # start off by creating a connection
    cursor = conn.cursor()  # then create a cursor to interact with the database
    try:
        _json = request.json
        _name = str(_json['Name'])
        _email = str(_json['Email'])
        _password = str(_json['Password'])
        _customer_id = str(_json["Customer ID"])
        _gender = str(_json["Gender"])
        _phone_number = str(_json["PhoneNumber"])
        _address = str(_json["Address"])
        # validate the received values
        if _name and _email and _password and request.method == 'POST':
            # do not save password as a plain text
            _hashed_password = bcrypt.generate_password_hash(
                _password).decode("utf-8")
            # form the raw sql statement with f strings, USE THIS EXACT FORMAT, any random indents can cause an error
            sql = f"""-- sql
                INSERT INTO `Customer` (`Customer ID`, `Password`, `Name`, `Gender`, `PhoneNumber`, `Address`, `Email`)
                VALUES ("{_customer_id}", "{_hashed_password}", "{_name}",
                        "{_gender}", "{_phone_number}", "{_address}", "{_email}");
                """
            cursor.execute(sql)  # execute formed sql
            conn.commit()  # if can execute, push changes to database
            resp = jsonify(success='User added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("Missing User Details")
    except Exception as e:
        print(str(e))
        resp = jsonify(error=str(e))
        resp.status_code = 500
        return resp
    finally:
        cursor.close()  # always have a finally block to close the database connection


@app.route('/api/Initialise', methods=["GET"])
def initialise_db():
    conn = mysql.connection
    cursor = conn.cursor()
    cur_path = os.path.dirname(__file__)[:-14]
    new_path = cur_path + 'SQL Scripts\\Initialise_OSHES_database.sql'
    try:
        with open(new_path) as f:
            cursor.execute(f.read())

        # testing out mongoDB connection
        collection = mongo["products"]
        for doc in collection.find({}):
            print(doc)
        resp = jsonify(success='Database Initialised!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(str(e))
        resp = jsonify(error=str(e))
        resp.status_code = 500
    finally:
        cursor.close()


@ app.errorhandler(404)
def not_found(error=None):
    """[summary]

    Args:
        error ([type], optional): [specifies error type to be sent]. Defaults to None.

    Returns:
        [Dict(str)]: [sends back 404 data not found error message should I choose to use it]
    """
    message = {
        'status': 404,
        'message': 'Not Found: ' + error,
        'error location': request.url
    }
    response = jsonify(message)
    response.status_code = 404
    return response


if __name__ == "__main__":
    app.run(debug=True)
