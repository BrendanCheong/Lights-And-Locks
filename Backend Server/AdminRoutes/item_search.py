from app import app
from db_config import *
from flask import jsonify, request


@app.route("/api/Admin/view/all_items", methods=["POST"])  # item search
def view_all_items():
    conn = mysql.connection
    cursor = conn.cursor()
    try:
        resp: dict = request.json
        item_id: str = resp["Item ID"]
        ITEM_RESPONSE: str = resp["ITEM RESPONSE"]
        statement1 = (
            "SELECT p1.`Product ID`, r1.`Item ID`, Item.`Production Year`, Item.`Power Supply`, Item.`Color`, Item.`Factory`, Item.`Purchase Status`, p1.`Model`, p1.`Category`, p1.`Warranty`,p1.`Price`, p1.`Cost` ",
            "FROM OSHES.Request r1 ",
            "INNER JOIN OSHES.Item ON r1.`Item ID` = OSHES.Item.`Item ID` ",
            "INNER JOIN OSHES.Service s1 ON r1.`Request ID` = s1.`Request ID` ",
            "INNER JOIN OSHES.Product p1 ON p1.`Product ID` = OSHES.Item.`Product ID` "
            """WHERE (s1.`Service Status` = "Waiting for approval" OR s1.`Service Status`= "In Progress") """,
            f"""AND r1.`Item ID` = "{item_id}" """ if item_id else "",
            """ORDER BY `Item ID`;"""
        )
        statement2 = (
            "SELECT * FROM `Item` ",
            "INNER JOIN `Product` USING (`Product ID`) ",
            """WHERE (`Purchase Status` = "Sold" OR `Purchase Status` = "Unsold") """,
            f"""AND `Item ID` = "{item_id}" """ if item_id else "",
            "ORDER BY `Item ID`;"
        )
        sql = ""
        if (ITEM_RESPONSE == "Yes"):
            for text in statement1:
                sql += text
            cursor.execute(sql)
            conn.commit()
            rows = cursor.fetchall()
            resp = jsonify(success=rows)
            resp.status_code = 200
            return resp
        else:
            for text in statement2:
                sql += text
            cursor.execute(sql)
            conn.commit()
            rows = cursor.fetchall()
            resp = jsonify(success=rows)
            resp.status_code = 200
            return resp
    except Exception as e:
        print(str(e))
        return invalid("Could Not Find that Item")
    finally:
        cursor.close()


@app.route("/api/Admin/search/products", methods=["POST"])  # product search
def view_all_products():
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
        statement2 = (
            "(SELECT COUNT(*) AS `Sold Items` ",
            "FROM Product LEFT JOIN Item USING (`Product ID`) ",
            """WHERE `Purchase Status` = "Sold" """,
            f"""AND Model = "{model}" """ if model != "All" else "",
            f"""AND Price = {price} """ if price != "All" else "",
            f"""AND color = "{color}" """ if color != "All" else "",
            f"""AND factory = "{factory}" """ if factory != "All" else "",
            f"""AND `Production Year` = "{production_year}" """ if production_year != "All" else "",
            f"""AND `Power Supply` = "{power_supply}" """ if power_supply != "All" else "",
            f"""AND Warranty = {warranty} """ if warranty != "All" else "",
            f"""AND Category = "{category}" """ if category != "All" else "",
            "ORDER BY `Product ID`, `Item ID`) AS `Sold Items` "
        )
        sql2 = ""
        for text in statement2:
            sql2 += text
        statement1 = (
            "SELECT `Category`, `Price`, `Warranty`, `Model`, `Cost`, COUNT(*) AS `Inventory Level`, ",
            f"""{sql2}""",
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
        for text in statement1:
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
