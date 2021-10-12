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

        # check if there's a Canceled or Completed Request, where if there is, we must delete that request and make a new one
        # if there isn't, its probably the first time they are making a request, so try to make a request and service
        sql1 = f"""-- sql
        SELECT * 
        FROM `Request`
        WHERE (`Request Status` = "Canceled" OR `Request Status` = "Completed")
        AND `Item ID` = "{item_id}";
        """
        cursor.execute(sql1)
        conn.commit()
        rows = cursor.fetchall()
        print(rows)
        if (len(rows) > 0):
            # delete the pre-existing request
            sql2 = "SET FOREIGN_KEY_CHECKS=0;"
            sql3 = f"""DELETE FROM `Request` WHERE `Item ID` = "{item_id}";"""
            sql4 = "SET FOREIGN_KEY_CHECKS=1;"
            cursor.execute(sql2)
            cursor.execute(sql3)
            cursor.execute(sql4)
            conn.commit()
            # now try to make a brand new request that also adds in a service
            try:
                sql5 = f"""-- sql
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
                cursor.execute(sql5)
                conn.commit()
                # try to make a new service
                try:
                    sql6 = f"""-- sql
                    INSERT INTO `Service` (`Service Status`, `Admin ID`, `Request ID`) 
                    VALUES (
                        (CASE WHEN curdate() <= '{warranty_end_date}' THEN "Waiting for approval" END),
                        (CASE WHEN curdate() <= '{warranty_end_date}' THEN NULL END),
                        (CASE WHEN curdate() <= '{warranty_end_date}' THEN (SELECT `Request ID` FROM `Request` WHERE `Item ID` = "{item_id}" AND `Customer ID` = "{customer_id}") END)
                    );
                    """
                    cursor.execute(sql6)
                    conn.commit()
                    resp = jsonify(
                        success="Request for Service Created Successfully")
                    resp.status_code = 200
                    return resp
                except Exception as e:  # catch scenario where the request needs to be paid and thus we can't make a new service
                    print(str(e))
                    resp = jsonify(
                        success="Request is Submitted and Waiting for Payment")
                    resp.status_code = 200
                    return resp
            except Exception as e:
                print(str(e))
                return invalid("That Item has already been requested!")
        else:  # if no existing request, this is probably the first time you are making that request
            try:
                sql7 = f"""-- sql
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
                cursor.execute(sql7)
                conn.commit()
                # try to make a new service
                try:
                    sql8 = f"""-- sql
                    INSERT INTO `Service` (`Service Status`, `Admin ID`, `Request ID`) 
                    VALUES (
                        (CASE WHEN curdate() <= '{warranty_end_date}' THEN "Waiting for approval" END),
                        (CASE WHEN curdate() <= '{warranty_end_date}' THEN NULL END),
                        (CASE WHEN curdate() <= '{warranty_end_date}' THEN (SELECT `Request ID` FROM `Request` WHERE `Item ID` = "{item_id}" AND `Customer ID` = "{customer_id}") END)
                    );
                    """
                    cursor.execute(sql8)
                    conn.commit()
                    resp = jsonify(
                        success="Request for Service Created Successfully")
                    resp.status_code = 200
                    return resp
                except Exception as e:  # catch scenario where the request needs to be paid and thus we can't make a new service
                    print(str(e))
                    resp = jsonify(
                        success="Request is Submitted and Waiting for Payment")
                    resp.status_code = 200
                    return resp
            except Exception as e:
                print(str(e))
                return invalid("That Item has already been requested!")
    except Exception as e:
        print(str(e))
        return invalid("Something went wrong: " + str(e))
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
    # upon successful payment of service fee, create a new service in service table to be approved by admin
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
        INSERT INTO `Service` (`Service Status`, `Admin ID`, `Request ID`)
        VALUES ("Waiting for approval", NULL, (SELECT `Request ID` FROM `Request` WHERE `Item ID` = "{item_id}" AND `Customer ID` = "{customer_id}"));
        """
        sql3 = f"""-- sql
        SELECT (`Cost` / 20) + 40 AS `Service Fee`
        FROM `Product`
        INNER JOIN `Item`
        ON `Item`.`Product ID` = `Product`.`Product ID`
        WHERE `Item ID` = "{item_id}";
        """
        cursor.execute(sql1)
        cursor.execute(sql2)
        cursor.execute(sql3)
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
    # assume that this is ALWAYS Status = "Canceled"
    # upon canceling, cancel any possible SERVICES from the service table
    # This means that canceling a request stops the admin from servicing said item!
    # this is because there is nothing to service when you cancel a request
    conn = mysql.connection
    cursor = conn.cursor()
    try:
        resp = request.json
        request_status = resp["Request Status"]
        customer_id = resp["Customer ID"]
        item_id = resp["Item ID"]
        sql1 = f"""-- sql
        UPDATE `Request`
        SET `Request Status` = "{request_status}"
        WHERE `Customer ID` = "{customer_id}" AND `Item ID` = "{item_id}";
        """
        sql2 = f"""-- sql
        DELETE FROM `Service` 
        WHERE
            `Service ID` = (SELECT 
                *
            FROM
                (SELECT 
                    `Service ID`
                FROM
                    `Service`
                INNER JOIN `Request` USING (`Request ID`)
                
                WHERE
                    `Customer ID` = '{customer_id}'
                    AND `Item ID` = '{item_id}') AS `Selected ID`);
        """
        cursor.execute(sql1)
        cursor.execute(sql2)
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
