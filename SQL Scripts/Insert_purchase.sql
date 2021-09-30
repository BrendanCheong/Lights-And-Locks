USE `OSHES`;

INSERT INTO `Purchase` (`Item ID`, `Purchase Date`, `Customer ID`)
VALUES("1094", curdate(), "Zuko");

SELECT * FROM `Purchase`;

SELECT `Item ID`, `Purchase Date` FROM `Purchase`
WHERE `Customer ID` = "Zuko";

SELECT  `Purchase Date`, 
		`Color`, 
        `Category`, 
        `Factory`, 
        `Model`, 
        `Power Supply`,
        `Warranty`, 
        DATE_ADD(`Purchase Date`,INTERVAL `Warranty` MONTH) AS 
        `Warranty End`, 
        `Price`
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
WHERE `Customer ID` = "Zuko";