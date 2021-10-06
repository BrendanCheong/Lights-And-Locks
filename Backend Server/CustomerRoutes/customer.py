from app import app
from db_config import *
from flask import jsonify, request


@app.route("/api/Customer/get/purchases", methods=["POST"])
def view_purchases():
    # find customer's pruchases based on their unique customer ID
    conn = mysql.connection
    cursor = conn.cursor()
    try:
        json = request.json
        print(json)
        customer_id = json["Customer ID"]
        sql = f"""-- sql
        SELECT `Purchase`.`Item ID`, 
		`Price`, 
		`Purchase Date`, 
		DATE_ADD(`Purchase Date`,INTERVAL `Warranty` MONTH) AS 
        `Warranty End`, 
        `Warranty`, 
        `Color`, 
        `Factory`,
        `Category`,
        `Model`, 
        `Power Supply`
        FROM `Purchase` 
        INNER JOIN (SELECT `Item ID`,
				    `Color`, 
                    `Category`, 
                    `Factory`, 
                    `Model`, 
                    `Power Supply`,
                    `Warranty`, 
                    `Price`
			FROM `Item`
			INNER JOIN `Product`
			ON `Item`.`Product ID` = `Product`.`Product ID`)
            AS `Product & Items`
        ON `Purchase`.`Item ID` = `Product & Items`.`Item ID`
        WHERE `Customer ID` = "{customer_id}";
        """
        cursor.execute(sql)
        conn.commit()
        rows = cursor.fetchall()
        resp = jsonify(success=rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(str(e))
        return not_found("Invalid Customer Selected")
    finally:
        cursor.close()


@ app.errorhandler(404)
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
