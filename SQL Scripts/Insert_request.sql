USE `OSHES`;

-- insert Request that isunder warranty
INSERT INTO `Request` (`Request Date`, `Request Status`, `Customer ID`, `Admin ID`, `Item ID`)
VALUES (DATE("2015-12-17"), 
CASE WHEN '2015-12-17' <= DATE_ADD((SELECT `Purchase Date` FROM `Purchase` WHERE `Item ID` = "1096"), INTERVAL 10 MONTH) -- I need to add the purchase date here based on item ID
THEN "Submitted"
ELSE "Submitted and Waiting for Payment"
END,
"Brendan",
NULL,
"1001"); -- selected item ID

INSERT INTO `Request` (`Request Date`, `Request Status`, `Customer ID`, `Admin ID`, `Item ID`)
VALUES (curdate(), 
CASE WHEN curdate() <= '2022-12-15' -- I compare request date to warranty date
THEN "Submitted"
ELSE "Submitted and Waiting for Payment"
END,
"Brendan",
"admin",
"1098");

-- insert an expired warranty with custom request date and warranty date

-- find my Requests according to Customer ID
SELECT `Item ID`, `Admin ID`, `Request Date`, `Request Status`,`Service Fee`, `Payment Date`
FROM `Request`
WHERE `Customer ID` = "Brendan";

-- update the request status based on customer id and 
UPDATE `Request`
SET `Request Status` = "Canceled"
WHERE `Customer ID` = "Something" AND `Item ID` = "Something";

-- update the payment date and service fee and status to "In Progress" upon paying
-- need to check if status is not canceled
START TRANSACTION;
UPDATE `Request`
SET `Request Status` = "In Progress",
	`Payment Date` = curdate(), -- assume current date
	`Service Fee` = ((SELECT `Cost`
						FROM `Product`
						INNER JOIN `Item`
						ON `Item`.`Product ID` = `Product`.`Product ID`
						WHERE `Item ID` = "1096") / 20) + 40
WHERE `Customer ID` = "Brendan" AND `Item ID` = "1096" AND `Request Status` = "Submitted and Waiting for Payment";

SELECT (`Cost` / 20) + 40 AS `Service Fee`
FROM `Product`
INNER JOIN `Item`
ON `Item`.`Product ID` = `Product`.`Product ID`
WHERE `Item ID` = "1096";

COMMIT;
-- calculate service fee
SELECT `Cost`
FROM `Product`
INNER JOIN `Item`
ON `Item`.`Product ID` = `Product`.`Product ID`
WHERE `Item ID` = "1092";

-- auto cancel after 10 days if not paid properly
UPDATE `Request` SET `Request Status` =
CASE WHEN `Request Status` = "Submitted and Waiting for Payment" AND curdate() >= DATE_ADD(`Request Date`, INTERVAL 10 DAY)
THEN "Canceled"
ELSE (SELECT `Request Status` FROM (SELECT * FROM `Request` AS `Peanut`) AS `Wanker` WHERE `Customer ID` = "Brendan")
END
WHERE `Customer ID` = "Brendan";

-- auto update the Request Status to "Canceled" if not paid in 10 days
SELECT * FROM `Request`;
DELETE FROM `OSHES`.`Request` WHERE `Customer ID` = "Brendan";