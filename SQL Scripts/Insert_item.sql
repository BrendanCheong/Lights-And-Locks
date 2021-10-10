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
WHERE Category = "Lights"
-- 	AND Model = "Light1"
--     AND Price = "50"
--     AND Color = "Green"
--     AND Factory = "Malaysia"
--     AND `Production Year` = "2015"
--     AND `Power Supply` = "USB"
--     AND Warranty = 10
--     AND `Purchase Status` = "Unsold"
ORDER BY `Product ID`, `Item ID`;

-- find items as above, make modular, but also return cost and number of Sold items
SELECT `Cost`, COUNT(*) AS `Inventory Level`, (SELECT COUNT(*) AS `Sold Items` 
												FROM Product LEFT JOIN Item USING (`Product ID`)
												WHERE Category = "Lights"
													AND `Purchase Status` = "Sold" -- idea?
													AND Model = "Light1"
												--  AND Price = "50"
												--  AND Color = "Green"
												--  AND Factory = "Malaysia"
												--  AND `Production Year` = "2015"
												--  AND `Power Supply` = "USB"
												--  AND Warranty = 10
													ORDER BY `Product ID`, `Item ID`) AS `Sold Items`, 
                                                    `Item ID`

FROM Product LEFT JOIN Item USING (`Product ID`)
WHERE Category = "Lights"
	AND Model = "Light1"
--  AND Price = "50"
--  AND Color = "Green"
--  AND Factory = "Malaysia"
--  AND `Production Year` = "2015"
--  AND `Power Supply` = "USB"
--  AND Warranty = 10
    AND `Purchase Status` = "Unsold"
ORDER BY `Product ID`, `Item ID`;

-- find the number of sold by category and amount
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