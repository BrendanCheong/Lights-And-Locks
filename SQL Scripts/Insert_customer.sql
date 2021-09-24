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

DELETE FROM `OSHES`.`Customer` WHERE `Customer ID` = "f50ec0b7-f960-400d-91f0-c42a6d44e3d0";