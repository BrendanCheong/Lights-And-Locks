USE `OSHES`;

INSERT INTO `Customer` (`Customer ID`, `Password`, `Name`, `Gender`, `PhoneNumber`, `Address`, `Email`)
VALUES ("Zuko",
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

-- view customers with Unpaid Fees
-- remember to auto cancel customers with unpaid service fees before running this
SELECT c1.`Customer ID`, c1.`Name`, c1.`Gender`, c1.`PhoneNumber`, c1.`Email`, c1.`Address`
FROM OSHES.Customer c1 
INNER JOIN OSHES.Request r1 ON c1.`Customer ID` = r1.`Customer ID`
WHERE r1.`Request Status` = "Submitted and Waiting for payment"
ORDER BY c1.`Customer ID`; -- order by Customer ID


DELETE FROM `OSHES`.`Customer`;