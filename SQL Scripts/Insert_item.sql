USE `OSHES`;

INSERT INTO `Item` (`Item ID`, `Category`, `Production Year`, `Power Supply`, `Color`, `Factory`, `Purchase Status`, `Model`, `Product ID`)
VALUES("1001", "Lights", 2014, "Battery", "White", "Malaysia", "Sold", "Light1", 
	(SELECT `Product ID` FROM `Product`
	WHERE `Model` = "Light1"
	AND `Category` = "Lights"));

SELECT * FROM `Item`