import os
from flask import jsonify, flash, request
from app import app
# NOTE:change this to db_local_config (if needed) for those who cannot connect to our AWS RDS and call the Initalise database GET route
from db_config import *

# pw_hash = bcrypt.generate_password_hash("hunter2").decode("utf-8")
# zombie = bcrypt.generate_password_hash("hunter2").decode("utf-8")
# print(pw_hash)
# print(zombie)
# print(bcrypt.check_password_hash(pw_hash, 'hunter2'))
# print(bcrypt.check_password_hash(pw_hash, 'false'))
# print(pw_hash)


@app.route("/", methods=["GET"])
def index():
    return jsonify(Welcome="Welcome to Lights and Lock's Server!")


"""
Add Customer Routes Here
"""


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
        return invalid(str(e))
    finally:
        cursor.close()  # always have a finally block to close the database connection


@app.route("/api/Customer/login", methods=["POST"])
def login_user():
    conn = mysql.connection  # start off by creating a connection
    cursor = conn.cursor()  # then create a cursor to interact with the database
    try:
        _json = request.json
        _customer_id = _json["Customer ID"]
        _password = _json["Password"]
        if _customer_id and _password:
            sql = f"""-- sql
            SELECT `Customer ID`, `Email`,`Name`, `Password` 
            FROM `OSHES`.`Customer`
            WHERE `Customer ID` = "{_customer_id}";
            """
            cursor.execute(sql)
            rows = cursor.fetchone()
            if (bcrypt.check_password_hash(rows[-1], _password)):
                return_load = {
                    "Customer ID": rows[0],
                    "Email": rows[1],
                    "Name": rows[2]
                }
                resp = jsonify(success=return_load)
                resp.status_code = 200
                return resp
            else:
                return invalid("Wrong Password Entered!")
        else:
            return not_found("Missing User Details")
    except Exception as e:
        print(str(e))
        return invalid("Customer Not Found")
    finally:
        cursor.close()


@app.route('/api/Initialise', methods=["GET"])
def initialise_db():
    conn = mysql.connection
    cursor = conn.cursor()
    cur_path = os.path.dirname(__file__)[:-14]
    new_path = cur_path + 'SQL Scripts\\init.sql'
    print(new_path)
    # creates a path to the folder containing the initialise database script
    # then read and execute the sql file with cursor
    try:
        with open(new_path) as f:
            cursor.execute(f.read())

        # Add MongoDB's Products and Items According to MySQL schema
        # takes like 20 seconds to execute all lol
        collection = mongo["products"]
        for doc in collection.find({}):
            sql = f"""-- sql
            INSERT INTO `Product` (`Product ID`, `Model`, `Category`, `Warranty`, `Price`, `Cost`)
            VALUES({doc["ProductID"]}, "{doc["Model"]}", "{doc["Category"]}", {doc["Warranty (months)"]}, {doc["Price ($)"]}, {doc["Cost ($)"]});
            """
            cursor.execute(sql)
            conn.commit()
        collection = mongo["items"]

        # For each document in the collection selected, iterate through all of them
        # then insert into the MySQL database
        for doc in collection.find({}):
            sql = f"""-- sql
            INSERT INTO `Item` (`Item ID`, `Production Year`, `Power Supply`, `Color`, `Factory`, `Purchase Status`, `Product ID`)
            VALUES("{doc["ItemID"]}", {int(doc["ProductionYear"])}, "{doc["PowerSupply"]}", "{doc["Color"]}", "{doc["Factory"]}", "{doc["PurchaseStatus"]}", 
                (SELECT `Product ID` FROM `Product`
                WHERE `Model` = "{doc["Model"]}"
                AND `Category` = "{doc["Category"]}"));
            """
            cursor.execute(sql)
            conn.commit()
        resp = jsonify(success='Database Initialised!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(str(e))
        return invalid(str(e))
    finally:
        cursor.close()


@ app.errorhandler(404)
def not_found(error):
    """[summary]

    Args:
        error ([type], optional): [specifies error type to be sent]. Defaults to None.

    Returns:
        [Dict(str)]: [sends back 404 data not found error message should I choose to use it]
    """
    message = {
        'status': 404,
        'error': 'Not Found: ' + error,
        'error location': request.url
    }
    response = jsonify(message)
    response.status_code = 404
    return response


@app.errorhandler(500)
def invalid(error):
    message = {
        'status': 500,
        'error': error,
        'error location': request.url
    }
    response = jsonify(message)
    response.status_code = 500
    return response


if __name__ == "__main__":
    import AdminRoutes.admin
    import AdminRoutes.admin_frontpage
    import AdminRoutes.item_search
    import AdminRoutes.services
    import CustomerRoutes.customer
    import CustomerRoutes.requests
    app.run(debug=True)
