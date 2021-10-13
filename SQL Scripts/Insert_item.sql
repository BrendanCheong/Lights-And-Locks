USE `OSHES`;

INSERT INTO `Item` (`Item ID`, `Production Year`, `Power Supply`, `Color`, `Factory`, `Purchase Status`, `Product ID`)
VALUES("1001", 2014, "Battery", "White", "Malaysia", "Sold",
	(SELECT `Product ID` FROM `Product`
	WHERE `Model` = "Light1"
	AND `Category` = "Lights"));

SELECT * FROM `Item`;

UPDATE `Item`
SET `Purchase Status` = "Sold"
WHERE `Item ID` = "1096";

-- finds all items for item table for customers, no count function though
SELECT `Item ID`,`Color`, `Category`, `Factory`, `Model`, `Power Supply`,`Warranty`, `Price`
FROM `Item`
INNER JOIN `Product`
ON `Item`.`Product ID` = `Product`.`Product ID`;

-- find items based on selection criteria, with ALL criterias
-- make criterias modular
SELECT *, COUNT(*) AS `Inventory Level`, `Item ID`
FROM Product LEFT JOIN Item USING (`Product ID`)
WHERE Category = "Lock"
-- 	   AND Model = "Light1"
--     AND Price = "50"
     AND Color = "Green"
--     AND Factory = "Malaysia"
--     AND `Production Year` = "2015"
--     AND `Power Supply` = "USB"
--     AND Warranty = 10
     AND `Purchase Status` = "Unsold"
ORDER BY `Product ID`, `Item ID`;

-- find items as above, make modular, but also return cost and number of Sold items
SELECT `Category`, `Price`, `Warranty`, `Model`, `Cost`, COUNT(*) AS `Inventory Level`, (SELECT COUNT(*) AS `Sold Items` 
												FROM Product LEFT JOIN Item USING (`Product ID`)
												WHERE Category = "Lights"
													AND `Purchase Status` = "Sold" -- idea?
											    -- AND Model = "Light1"
												-- AND Price = "50"
												-- AND Color = "Green"
												-- AND Factory = "Malaysia"
												-- AND `Production Year` = "2015"
												--  AND `Power Supply` = "USB"
												--  AND Warranty = 10
													ORDER BY `Product ID`, `Item ID`) AS `Sold Items`
FROM Product LEFT JOIN Item USING (`Product ID`)
WHERE Category = "Lights"
-- AND Model = "Light1"
-- AND Price = "50"
-- AND Color = "Green"
-- AND Factory = "Malaysia"
-- AND `Production Year` = "2015"
--  AND `Power Supply` = "USB"
--  AND Warranty = 10
    AND `Purchase Status` = "Unsold"
ORDER BY `Product ID`, `Item ID`;

-- find the number of items sold by category and model
SELECT p1.Category, p1.Model, COUNT(`Item ID`) AS "Number of Sold Item"
FROM OSHES.Item
LEFT JOIN OSHES.Product p1 ON OSHES.Item.`Product ID` = p1.`Product ID`
WHERE OSHES.Item.`Purchase Status` = "Sold"
GROUP BY p1.Category, p1.Model
ORDER BY 1;

-- find the number of sold and unsold items by Product id
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

-- find all items under service
SELECT p1.`Product ID`, r1.`Item ID`, Item.`Production Year`, Item.`Power Supply`, Item.`Color`, Item.`Factory`, Item.`Purchase Status`, p1.`Model`, p1.`Category`, p1.`Warranty`,p1.`Price`, p1.`Cost`
FROM OSHES.Request r1
INNER JOIN OSHES.Item ON r1.`Item ID` = OSHES.Item.`Item ID`
INNER JOIN OSHES.Service s1 ON r1.`Request ID` = s1.`Request ID`
INNER JOIN OSHES.Product p1 ON p1.`Product ID` = OSHES.Item.`Product ID`
WHERE (s1.`Service Status` = "Waiting for approval" OR s1.`Service Status`= "In Progress")
-- AND r1.`Item ID` = "1003"
ORDER BY `Item ID`;

-- find a specific item by id, return category and model also
SELECT *
FROM `Item`
INNER JOIN `Product` USING (`Product ID`)
WHERE (`Purchase Status` = "Sold" OR `Purchase Status` = "Unsold")
-- AND `Item ID` = "1096" 
ORDER BY `Item ID`;
