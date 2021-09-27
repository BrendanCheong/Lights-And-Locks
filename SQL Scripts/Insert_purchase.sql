USE `OSHES`;

INSERT INTO `Purchase` (`Item ID`, `Purchase Date`, `Customer ID`)
VALUES("1093", curdate(), "Zuko");

SELECT * FROM `Purchase`;

SELECT `Item ID`, `Purchase Date` FROM `Purchase`
WHERE `Customer ID` = "Zuko";

SELECT `Item ID` FROM `Item` 
INNER JOIN `Purchase`
ON `Item`.`Item ID` = `Purchase`.`Item ID`
WHERE `Customer ID` =  "Zuko";