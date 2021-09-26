USE `OSHES`;

INSERT INTO `Customer` (`Customer ID`, `Password`, `Name`, `Gender`, `PhoneNumber`, `Address`, `Email`)
VALUES ("f50ec0b7-f960-400d-91f0-c42a6d44e3d0",
"$2b$12$X1OqzBS2q4g4ZLefVZuAgepWHT4PJ64pPU3YiwLBEBi1QgaTd.zWG",
"Brendan Cheong Ern Jie",
"Male",
"94569855",
"Telok Chapel Lodgings",
"testgmail@gmail.com");

SELECT * FROM `OSHES`.`Customer`;
SELECT * FROM `OSHES`.`Administrator`;

SELECT `Customer ID`, `Email`,`Name`, `Password` 
FROM `OSHES`.`Customer`
WHERE `Email` = "brendancej82@gmail.com";

DELETE FROM `OSHES`.`Customer`;