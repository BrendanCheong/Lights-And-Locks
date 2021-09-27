USE `OSHES`;

INSERT INTO `Product` (`Product ID`, `Model`, `Category`, `Warranty`, `Price`, `Cost`)
VALUES(1, "Light1", "Lights", 10, 50, 20);

SELECT * FROM `Product` WHERE `Product ID` = 1;
SELECT * FROM `Product`;

-- I can add more Product IDs, but can only have 1 Color attribute
SELECT `Category`, `Model`, `Warranty`, `Price`, (SELECT COUNT(*) FROM `Item` WHERE `Product ID` = 1 OR `Product ID` = 2 AND `Color` = "White" ) AS `Stock`
FROM `Product`
WHERE `Category` = "Lights"         
GROUP BY `Category`;

-- to find all possible Product ID given Model and Categories
SELECT `Product ID` 
FROM `Product`
WHERE `Category` = "Lights" AND  `Model` = "Light1";

DELETE FROM `Product` WHERE `Product ID` = 1;