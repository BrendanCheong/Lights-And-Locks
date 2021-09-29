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
