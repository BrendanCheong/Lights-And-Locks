from app import app
from db_config import *
from flask import jsonify, request


@app.route("/api/Admin/view/items_sold_unsold", methods=["GET"])
def sold_unsold_items():
    conn = mysql.connection
    cursor = conn.cursor()
    try:
        sql = f"""-- sql
        SELECT `Sold`.`Product ID` AS `IID`, `Sold Items`, `Unsold Items`
        FROM (SELECT `Product ID`, COUNT(*) AS `Sold Items` 
                FROM `Item` 
                WHERE `Purchase Status` = "Sold" 
                GROUP BY `Product ID`) AS `Sold`
        INNER JOIN (SELECT `Product ID`, COUNT(*) AS `Unsold Items` 
                    FROM `Item` 
                    WHERE `Purchase Status` = "Unsold" 
                    GROUP BY `Product ID`) AS `Unsold`
        ON `Sold`.`Product ID` = `Unsold`.`Product ID`;
        """
        cursor.execute(sql)
        conn.commit()
        rows = cursor.fetchall()
        resp = jsonify(success=rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(str(e))
        return invalid("Something went wrong when finding Items")
    finally:
        cursor.close()


@app.route("/api/Admin/view/items_sold_cat_model", methods=["GET"])
def sold_items_cat_model():
    conn = mysql.connection
    cursor = conn.cursor()
    try:
        sql = f"""-- sql
        SELECT p1.Category, p1.Model, COUNT(`Item ID`) AS "Number of Sold Item"
        FROM OSHES.Item
        LEFT JOIN OSHES.Product p1 ON OSHES.Item.`Product ID` = p1.`Product ID`
        WHERE OSHES.Item.`Purchase Status` = "Sold"
        GROUP BY p1.Category, p1.Model
        ORDER BY 1;
        """
        cursor.execute(sql)
        conn.commit()
        rows = cursor.fetchall()
        resp = jsonify(success=rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(str(e))
        return invalid("Something went wrong when finding Items")
    finally:
        cursor.close()


@app.route("/api/Admin/view/customers_unpaid", methods=["GET"])
def unpaid_customers():
    # insert auto canceler after 10 days
    # then view all customers with unpaid service fees
    conn = mysql.connection
    cursor = conn.cursor()
    try:
        sql1 = f"""-- sql
        UPDATE `Request` SET `Request Status` =
        CASE WHEN `Request Status` = "Submitted and Waiting for Payment" AND curdate() > DATE_ADD(`Request Date`, INTERVAL 10 DAY)
        THEN "Canceled"
        ELSE `Request Status`
        END;
        """
        sql2 = f"""-- sql
        SELECT c1.`Customer ID`, c1.`Name`, c1.`Gender`, c1.`PhoneNumber`, c1.`Email`, c1.`Address`
        FROM OSHES.Customer c1 
        INNER JOIN OSHES.Request r1 ON c1.`Customer ID` = r1.`Customer ID`
        WHERE r1.`Request Status` = "Submitted and Waiting for payment"
        ORDER BY c1.`Customer ID`;
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
        return invalid("Something went wrong when fetching customers")
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
