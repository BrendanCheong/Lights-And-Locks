from pprint import pprint
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
    # note that Purchase Status is FIXED while all other fields are ambiguous
    # returns the inventory level for said item
    try:

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

        for k, v in resp.items():
            if (v != "All" and is_int_try(v)):
                and_array.append({k: int(v)})
            elif (v != "All"):
                and_array.append({k: v})
        match = {
            "$match": {
                "$and": and_array
            }
        }
        pipeline.append(match)
        result = list(items.aggregate(pipeline))
        output = list()
        if (len(result) == 0):
            output = [
                None,
                None,
                None,
                None,
                0,
                0
            ]
        else:
            output = [
                result[0]["Category"],
                result[0]["Model"],
                result[0]["Warranty"],
                result[0]["Price"],
                len(result),
                result[0]["ItemID"]
            ]
        resp = jsonify(success=[output])
        resp.status_code = 200
        return resp
    except Exception as e:
        print(str(e))
        return invalid(str(e))


@app.route("/api/Customer/add/purchases", methods=["POST"])
def add_purchase():
    # add to the purchase table based on item Id and Customer Id
    # then update the item status to Sold
    # also update the mongodb while you're at it
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

        items = mongo["items"]
        items.update_one(
            {"ItemID": item_id},
            {"$set": {"PurchaseStatus": "Sold"}}
        )

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
