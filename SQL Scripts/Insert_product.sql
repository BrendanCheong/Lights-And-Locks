USE `OSHES`;

INSERT INTO `Product` (`Product ID`, `Model`, `Category`, `Warranty`, `Price`, `Cost`)
VALUES(1, "Light1", "Lights", 10, 50, 20);

SELECT * FROM `Product` WHERE `Product ID` = 1;
SELECT * FROM `Product`;

DELETE FROM `Product` WHERE `Product ID` = 1;