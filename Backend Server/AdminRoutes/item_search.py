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
    try:
        resp = request.json

        def is_int_try(val: str) -> bool:
            try:
                int(val)
                return True
            except ValueError:
                return False

        resp = request.json

        # Use Mongodb to get all the information like Item ID to buy and category/model name etc
        items = mongo["items"]
        pipeline = [
            {
                "$lookup": {
                    "from": "products",
                    "localField": "Category",
                    "foreignField": "Category",
                    "as": "product_doc"
                }
            },
            {
                "$unwind": "$product_doc"
            },
            {
                "$redact": {
                    "$cond": [
                        {"$eq": ["$Model", "$product_doc.Model"]},
                        "$$KEEP",
                        "$$PRUNE"
                    ]
                }
            },
            {
                "$project": {
                    "Category": 1,
                    "Model": 1,
                    "ItemID": "$ItemID",
                    "Color": "$Color",
                    "Factory": "$Factory",
                    "Power Supply": "$PowerSupply",
                    "Purchase Status": "$PurchaseStatus",
                    "Production Year": "$ProductionYear",
                    "ProductID": "$product_doc.ProductID",
                    "Cost": "$product_doc.Cost ($)",
                    "Price": "$product_doc.Price ($)",
                    "Warranty": "$product_doc.Warranty (months)"
                }
            }
        ]
        and_array = [{"Purchase Status": "Unsold"}]
        sold_array = [{"Purchase Status": "Sold"}]
        for k, v in resp.items():
            if (v != "All" and is_int_try(v)):
                and_array.append({k: int(v)})
                sold_array.append({k: int(v)})
            elif (v != "All"):
                and_array.append({k: v})
                sold_array.append({k: v})
        match1 = {
            "$match": {
                "$and": and_array
            }
        }
        match2 = {
            "$match": {
                "$and": sold_array
            }
        }
        pipeline.append(match1)
        result = list(items.aggregate(pipeline))
        pipeline = pipeline[:-1] + [match2]  # calculate total sold
        sold_items_amount = len(list(items.aggregate(pipeline)))
        output = list()
        if (len(result) == 0):
            output = [
                None,
                None,
                None,
                None,
                None,
                0,
                None
            ]
        else:
            output = [
                result[0]["Category"],
                result[0]["Price"],
                result[0]["Warranty"],
                result[0]["Model"],
                result[0]["Cost"],
                len(result),
                sold_items_amount
            ]
        print(output)

        resp = jsonify(success=output)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(str(e))
        return invalid(str(e))


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
