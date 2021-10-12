USE `OSHES`;
-- when canceling "Canceled" a request, customer can go into purchases and request the same item ID again
-- this means that the db must delete that request with the unique item ID
-- then add a new request based on that same item ID
-- this also occurs for when the request is "Completed", delete the request with the unique ID
-- and then make the request again from the purchases screen
# if this returns nothing, then you have to make a brand new request without deleting
# if you can't make a brand new request, throw error saying that the request already exists!
SELECT * 
FROM `Request`
WHERE (`Request Status` = "Canceled" OR `Request Status` = "Completed")
AND `Item ID` = "1003";
# else delete the pre existing request
SET FOREIGN_KEY_CHECKS=0;
DELETE FROM `Request` WHERE `Item ID` = "1003";
SET FOREIGN_KEY_CHECKS=1;
# then continue in making a new request

###########################
-- insert Request that is not under warranty and will be auto canceled after 10 days
-- when the case is "Submitted", create a new Service using the new Request ID
-- if not, don't create a new service
INSERT INTO `Request` (`Request Date`, `Request Status`, `Customer ID`, `Admin ID`, `Item ID`)
VALUES (DATE("2015-12-17"), 
CASE WHEN '2015-12-17' <= DATE_ADD((SELECT `Purchase Date` FROM `Purchase` WHERE `Item ID` = "1096"), INTERVAL 10 MONTH) -- I need to add the purchase date here based on item ID
THEN "Submitted"
ELSE "Submitted and Waiting for Payment"
END,
"Brendan",
NULL,
"1001"); -- selected item ID

#########################################################
-- insert query that is not under warranty that will get auto canceled
INSERT INTO `Request` (`Request Date`, `Request Status`, `Customer ID`, `Admin ID`, `Item ID`)
VALUES ('2020-12-22', 
"Submitted and Waiting for Payment",
"Zuko",
NULL,
"1002");

-- query not under warranty that won't get auto canceled
INSERT INTO `Request` (`Request Date`, `Request Status`, `Customer ID`, `Admin ID`, `Item ID`)
VALUES ('2022-12-22', 
"Submitted and Waiting for Payment",
"Zuko",
NULL,
"1003");
#########################################################

-- insert query that uses current date, as per normal
-- will be submitted by default, assuming warranty date
-- when the case is "Submitted", create a new Service using the new Request ID
-- if not, don't create a new service
START TRANSACTION;

INSERT INTO `Request` (`Request Date`, `Request Status`, `Customer ID`, `Admin ID`, `Item ID`)
VALUES (curdate(), 
CASE WHEN curdate() <= '2022-12-15' -- I compare request date to warranty date
THEN "Submitted"
ELSE "Submitted and Waiting for Payment"
END,
"Brendan",
NULL,
"1098");


INSERT INTO `Service` (`Service Status`, `Admin ID`, `Request ID`) -- handle error thrown here with another try catch block
VALUES (
	(CASE WHEN curdate() <= '2022-12-15' THEN "Waiting for approval" END),
    (CASE WHEN curdate() <= '2022-12-15' THEN NULL END),
    (CASE WHEN curdate() <= '2022-12-15' THEN (SELECT `Request ID` FROM `Request` WHERE `Item ID` = "1098" AND `Customer ID` = "Brendan") END)
);

COMMIT;

-- find my Requests according to Customer ID
SELECT `Item ID`, `Admin ID`, `Request Date`, `Request Status`,`Service Fee`, `Payment Date`
FROM `Request`
WHERE `Customer ID` = "Brendan";

-- update the request status based on customer id and status chosen
-- for canceling requests!
-- you can't cancel if its Approved, Canceled already or Completed
-- once canceled, remove the service in service table regardless of service status
START TRANSACTION;

UPDATE `Request` 
SET 
    `Request Status` = 'Canceled'
WHERE
    `Customer ID` = 'Zuko' -- var
        AND `Item ID` = '1003'; -- var

DELETE FROM `Service` 
WHERE
    `Service ID` = (SELECT 
        *
    FROM
        (SELECT 
            `Service ID`
        FROM
            `Service`
        INNER JOIN `Request` USING (`Request ID`)
        
        WHERE
            `Customer ID` = 'Zuko' -- var
            AND `Item ID` = '1003') AS `Selected ID`); -- var

COMMIT;

-- PAYMENT of SERVICE FEE: update the payment date and service fee and status to "In Progress" upon paying
-- upon paying for the request/service fee, create a new Service in service table
-- that says "Waiting for Approval" using the Request ID
-- need to check if status is not canceled (client side)
START TRANSACTION;

UPDATE `Request`
SET `Request Status` = "In Progress",
	`Payment Date` = curdate(), -- assume current date
	`Service Fee` = ((SELECT `Cost`
						FROM `Product`
						INNER JOIN `Item`
						ON `Item`.`Product ID` = `Product`.`Product ID`
						WHERE `Item ID` = "1096") / 20) + 40
WHERE `Customer ID` = "Zuko" AND `Item ID` = "1003" AND `Request Status` = "Submitted and Waiting for Payment";

INSERT INTO `Service` (`Service Status`, `Admin ID`, `Request ID`)
VALUES ("Waiting for approval", NULL, (SELECT `Request ID` FROM `Request` WHERE `Item ID` = "1003" AND `Customer ID` = "Zuko"));

SELECT (`Cost` / 20) + 40 AS `Service Fee`
FROM `Product`
INNER JOIN `Item`
ON `Item`.`Product ID` = `Product`.`Product ID`
WHERE `Item ID` = "1003";

COMMIT;


-- auto cancel after 10 days if not paid in time
UPDATE `Request` SET `Request Status` =
CASE WHEN `Request Status` = "Submitted and Waiting for Payment" AND curdate() > DATE_ADD(`Request Date`, INTERVAL 10 DAY)
THEN "Canceled"
ELSE `Request Status`
END;

-- auto update the Request Status to "Canceled" if not paid in 10 days
SELECT * FROM `Request`;
DELETE FROM `OSHES`.`Request`;