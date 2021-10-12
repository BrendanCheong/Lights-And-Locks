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


@app.route("/api/Customer/search/products", methods=["POST"])
def search_product_customer():
    # Search for a product based on a number of queries selected from the advanced search
    # note that Category is FIXED while all other fields are ambiguous
    # returns the inventory level for said item
    conn = mysql.connection
    cursor = conn.cursor()
    try:
        resp = request.json
        category = resp["Category"]
        model = resp["Model"]
        price = resp["Price"]
        color = resp["Color"]
        factory = resp["Factory"]
        production_year = resp["Production Year"]
        power_supply = resp["Power Supply"]
        warranty = resp["Warranty"]
        statement = (
            "SELECT `Category`, `Model`, `Warranty`, `Price`, COUNT(*) AS `Inventory Level`, `Item ID` ",
            "FROM Product LEFT JOIN Item USING (`Product ID`) ",
            """WHERE `Purchase Status` = "Unsold" """,
            f"""AND Model = "{model}" """ if model != "All" else "",
            f"""AND Price = {price} """ if price != "All" else "",
            f"""AND color = "{color}" """ if color != "All" else "",
            f"""AND factory = "{factory}" """ if factory != "All" else "",
            f"""AND `Production Year` = "{production_year}" """ if production_year != "All" else "",
            f"""AND `Power Supply` = "{power_supply}" """ if power_supply != "All" else "",
            f"""AND Warranty = {warranty} """ if warranty != "All" else "",
            f"""AND Category = "{category}" """ if category != "All" else "",
            "ORDER BY `Product ID`, `Item ID`;"
        )
        sql = ""
        for text in statement:
            sql += text
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


@app.route("/api/Customer/add/purchases", methods=["POST"])
def add_purchase():
    # add to the purchase table based on item Id and Customer Id
    # then update the item status to Sold
    conn = mysql.connection
    cursor = conn.cursor()
    try:
        resp = request.json
        customer_id = resp["Customer ID"]
        item_id = resp["Item ID"]
        sql1 = f"""-- sql
        INSERT INTO `Purchase` (`Item ID`, `Purchase Date`, `Customer ID`)
        VALUES("{item_id}", curdate(), "{customer_id}");
        """
        sql2 = f"""-- sql
        UPDATE `Item`
        SET `Purchase Status` = "Sold"
        WHERE `Item ID` = "{item_id}";
        """
        cursor.execute(sql1)
        cursor.execute(sql2)
        conn.commit()
        resp = jsonify(success="Successfully Purchased Item!")
        resp.status_code = 200
        return resp
    except Exception as e:
        print(str(e))
        return invalid("Item Already Purchased! >:(")
    finally:
        cursor.close()


@app.errorhandler(404)
def not_found(error):
    print
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
