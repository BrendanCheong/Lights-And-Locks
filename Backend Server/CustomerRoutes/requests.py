from app import app
from db_config import *
from flask import jsonify, request
import simplejson as json


@app.route("/api/Customer/add/request", methods=["POST"])
def add_request():
    # add a new request based on customer, item id and calculates request status
    # NOTE: Before adding a new request, check if there is already an existing request that is either "Canceled" or "Completed"
    # If so, delete that request using item ID, THEN add a new request
    # BUT if its your first time, just add the request
    conn = mysql.connection
    cursor = conn.cursor()
    try:
        resp = request.json
        warranty_end_date = resp["Warranty End"]
        customer_id = resp["Customer ID"]
        item_id = resp["Item ID"]
        sql = f"""-- sql
        INSERT INTO `Request` (`Request Date`, `Request Status`, `Customer ID`, `Admin ID`, `Item ID`)
        VALUES (curdate(), 
        CASE WHEN curdate() <= '{warranty_end_date}' -- I compare request date to warranty date
        THEN "Submitted"
        ELSE "Submitted and Waiting for Payment"
        END,
        "{customer_id}",
        NULL,
        "{item_id}");
        """
        cursor.execute(sql)
        conn.commit()
        resp = jsonify(success="Successfully added to Request Table")
        resp.status_code = 200
        return resp
    except Exception as e:
        print(str(e))
        return invalid("That Item has already been requested!")
    finally:
        cursor.close()


@app.route("/api/Customer/get/request", methods=["POST"])
def get_all_request():
    # get all request according to customers ID
    # install an auto canceler for those not paid in 10 days before searching to refesh
    conn = mysql.connection
    cursor = conn.cursor()
    try:
        resp = request.json
        customer_id = resp["Customer ID"]
        sql1 = f"""-- sql
        UPDATE `Request` SET `Request Status` =
        CASE WHEN `Request Status` = "Submitted and Waiting for Payment" AND curdate() > DATE_ADD(`Request Date`, INTERVAL 10 DAY)
        THEN "Canceled"
        ELSE `Request Status`
        END
        """
        sql2 = f"""-- sql
        SELECT `Item ID`, `Admin ID`, `Request Date`, `Request Status`, `Service Fee`, `Payment Date`
        FROM `Request`
        WHERE `Customer ID` = "{customer_id}";
        """
        cursor.execute(sql1)
        cursor.execute(sql2)
        conn.commit()
        rows = cursor.fetchall()
        resp = jsonify(success=rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(str(e))
        return not_found("Customer Not Found")
    finally:
        cursor.close()


@app.route("/api/Customer/update/request/payment", methods=["PATCH"])
def pay_service_fee():
    # pay for the service fee, resulting in status changing to "In Progress"
    # and calculate the service fee as well and set payment date to current date
    # return back the service fee as well, to render on the table
    conn = mysql.connection
    cursor = conn.cursor()
    try:
        resp = request.json
        customer_id = resp["Customer ID"]
        item_id = resp["Item ID"]
        sql1 = f"""-- sql
        UPDATE `Request`
        SET `Request Status` = "In Progress",
            `Payment Date` = curdate(), -- assume current date
            `Service Fee` = ((SELECT `Cost`
                                FROM `Product`
                                INNER JOIN `Item`
                                ON `Item`.`Product ID` = `Product`.`Product ID`
                                WHERE `Item ID` = "{item_id}") / 20) + 40
        WHERE `Customer ID` = "{customer_id}" AND `Item ID` = "{item_id}" AND `Request Status` = "Submitted and Waiting for Payment";
        """
        sql2 = f"""-- sql
        SELECT (`Cost` / 20) + 40 AS `Service Fee`
        FROM `Product`
        INNER JOIN `Item`
        ON `Item`.`Product ID` = `Product`.`Product ID`
        WHERE `Item ID` = "{item_id}";
        """
        cursor.execute(sql1)
        cursor.execute(sql2)
        conn.commit()
        rows = json.dumps(cursor.fetchall())
        processed = str(rows).replace('[', '').replace(']', '')
        resp = jsonify(success=processed)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(str(e))
        return not_found("Item ID or Customer Not Found")
    finally:
        cursor.close()


@app.route("/api/Customer/update/request", methods=["PATCH"])
def change_request_state():
    # updates the request based on customer id and item id to desired status from client side
    conn = mysql.connection
    cursor = conn.cursor()
    try:
        resp = request.json
        request_status = resp["Request Status"]
        customer_id = resp["Customer ID"]
        item_id = resp["Item ID"]
        sql = f"""-- sql
        UPDATE `Request`
        SET `Request Status` = "{request_status}"
        WHERE `Customer ID` = "{customer_id}" AND `Item ID` = "{item_id}";
        """
        cursor.execute(sql)
        conn.commit()
        resp = jsonify(success="Request Status Updated Successfully")
        resp.status_code = 200
        return resp
    except Exception as e:
        print(str(e))
        return invalid("You can't do that request!")
    finally:
        cursor.close()


@app.errorhandler(404)
def not_found(error):
    message = {
        'status': 404,
        'message': 'Not Found: ' + error,
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
