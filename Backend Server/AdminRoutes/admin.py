from app import app
from db_config import *  # NOTE: Replace this with local version if you want to
from flask import jsonify, flash, request


@app.route('/api/Admin/add', methods=['POST'])
def admin():
    conn = mysql.connection
    cursor = conn.cursor()
    try:
        json = request.json
        admin_id = json["Admin ID"]
        password = json["Password"]
        name = json["Name"]
        phone_number = json["Phone Number"]
        gender = json["Gender"]

        # validate admin id and name and password is valid
        if admin_id and password and name:
            _hashed_password = bcrypt.generate_password_hash(
                password).decode("utf-8")
            sql = f"""-- sql
            INSERT INTO `Administrator` (`Admin ID`, `Password`, `Name`, `Gender`, `PhoneNumber`)
            VALUES("{admin_id}", "{_hashed_password}", "{name}", "{gender}", "{phone_number}");
            """
            cursor.execute(sql)
            conn.commit()
            resp = jsonify(success="Admin Added Successfully!")
            resp.status_code = 200
            return resp
        else:
            resp = jsonify(message="Admin Details Entered Wrongly")
            resp.status_code = 404
            return resp
    except Exception as e:
        print(str(e))
        resp = jsonify(error=str(e))
        resp.status_code = 500
        return resp
    finally:
        cursor.close()


@app.route('/api/Admin/login', methods=["POST"])
def admin_login():
    conn = mysql.connection
    cursor = conn.cursor()
    try:
        json = request.json
        admin_id = json["Admin ID"]
        password = json["Password"]
        if admin_id and password:
            sql = f"""-- sql
            SELECT `Admin ID`, `Name`, `Password`
            FROM `OSHES`.`Administrator`
            WHERE `Admin ID` = "{admin_id}";
            """
            cursor.execute(sql)
            conn.commit()
            rows = cursor.fetchone()
            if (bcrypt.check_password_hash(rows[-1], password)):
                return_load = {
                    "Admin ID": rows[0],
                    "Name": rows[1],
                }
                resp = jsonify(success=return_load)
                resp.status_code = 200
                return resp
            else:
                resp = jsonify(error="Wrong Password!")
                resp.status_code = 500
                return resp
        else:
            resp = jsonify(message="Invalid Admin Details!")
            resp.status_code = 404
            return resp
    except Exception as e:
        resp = jsonify(error=str(e))
        resp.status_code = 500
        return resp
    finally:
        cursor.close()
