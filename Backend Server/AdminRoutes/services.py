from app import app
from db_config import *  # NOTE: Replace this with local version if you want to
from flask import jsonify, flash, request


# find services to approve
@app.route("/api/Admin/view/approving_services", methods=['GET'])
def view_all_services_for_approval():
    conn = mysql.connection
    cursor = conn.cursor()
    try:
        sql = f"""-- sql
        SELECT r1.`Request ID`, s1.`Service ID`, r1.`Customer ID`, r1.`Admin ID`, r1.`Item ID`, r1.`Request Date`
        FROM OSHES.Request r1
        INNER JOIN OSHES.Item ON r1.`Item ID` = OSHES.Item.`Item ID`
        INNER JOIN OSHES.Service s1 ON r1.`Request ID` = s1.`Request ID`
        WHERE s1.`Service Status` = "Waiting for approval";
        """
        cursor.execute(sql)
        conn.commit()
        rows = cursor.fetchall()
        resp = jsonify(success=rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(str(e))
        return invalid(str(e))
    finally:
        cursor.close()


# find services to complete
@app.route("/api/Admin/view/all_services", methods=["GET"])
def all_services():
    conn = mysql.connection
    cursor = conn.cursor()
    try:
        sql = f"""-- sql
        SELECT `Admin ID`, `Request ID`, `Service ID`, `Service Status`
        FROM `Service`
        WHERE `Service Status` = "Completed" OR `Service Status` = "In Progress";
        """
        cursor.execute(sql)
        conn.commit()
        rows = cursor.fetchall()
        resp = jsonify(success=rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(str(e))
        return invalid(str(e))
    finally:
        cursor.close()


# approve said service and request
@app.route("/api/Admin/approve/services", methods=["PATCH"])
def approve_services():
    conn = mysql.connection
    cursor = conn.cursor()
    try:
        resp = request.json
        admin_id = resp["Admin ID"]
        request_id = resp["Request ID"]
        service_id = resp["Service ID"]
        sql1 = f"""-- sql
        UPDATE `Request`
        SET `Request Status` = "Approved",
            `Admin ID` = "{admin_id}"
        WHERE `Request ID` = {request_id}; 
        """
        sql2 = f"""-- sql
        UPDATE `Service`
        SET `Service Status` = "In Progress",
            `Admin ID` = "{admin_id}"
        WHERE `Service ID` = {service_id};
        """
        cursor.execute(sql1)
        cursor.execute(sql2)
        conn.commit()
        resp = jsonify(success="Successfully approved Service and Request")
        resp.status_code = 200
        return resp
    except Exception as e:
        print(str(e))
        return not_found("Service and Request Not Found")
    finally:
        cursor.close()


# complete said service and request
@app.route("/api/Admin/complete/services", methods=["PATCH"])
def complete_service():
    conn = mysql.connection
    cursor = conn.cursor()
    try:
        resp = request.json
        request_id = resp["Request ID"]
        service_id = resp["Service ID"]
        sql1 = f"""-- sql
        UPDATE `Request` 
        SET `Request Status` = "Completed"
        WHERE `Request ID` = {request_id}
            AND `Request Status` = "Approved";
        """
        sql2 = f"""-- sql
        UPDATE `Service`
        SET `Service Status` = "Completed"
        WHERE `Service ID` = {service_id}
            AND `Service Status` = "In Progress";
        """
        cursor.execute(sql1)
        cursor.execute(sql2)
        conn.commit()
        resp = jsonify(success="Successfully Completed Service and Request")
        resp.status_code = 200
        return resp
    except Exception as e:
        print(str(e))
        return not_found("Service and Request ID Not Found")
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
