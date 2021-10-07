USE `OSHES`;

INSERT INTO `Item` (`Item ID`, `Production Year`, `Power Supply`, `Color`, `Factory`, `Purchase Status`, `Product ID`)
VALUES("1001", 2014, "Battery", "White", "Malaysia", "Sold",
	(SELECT `Product ID` FROM `Product`
	WHERE `Model` = "Light1"
	AND `Category` = "Lights"));

SELECT * FROM `Item`;

SELECT `Item ID` FROM `Item`
WHERE `Purchase Status` = "Unsold"
	AND `Product ID` = 1
ORDER BY `Item ID` ASC
LIMIT 1;

-- finds all items for item table for customers, no count function though
SELECT `Item ID`,`Color`, `Category`, `Factory`, `Model`, `Power Supply`,`Warranty`, `Price`
FROM `Item`
INNER JOIN `Product`
ON `Item`.`Product ID` = `Product`.`Product ID`;

-- find items based on selection criteria, with ALL criterias
-- make criterias modular
SELECT `Category`, `Model`, `Warranty`, `Price`, COUNT(*) AS `Inventory Level`, `Item ID`
FROM Product LEFT JOIN Item USING (`Product ID`)
WHERE Category = "Lights"
-- 	AND Model = "Light1"
--     AND Price = "50"
--     AND Color = "Green"
--     AND Factory = "Malaysia"
--     AND `Production Year` = "2015"
--     AND `Power Supply` = "USB"
--     AND Warranty = 10
    AND `Purchase Status` = "Unsold"
ORDER BY `Product ID`, `Item ID`;