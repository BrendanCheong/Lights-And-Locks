-- find services that need to be approved, which are request that automatically create services in the service table
-- when updating a service, I also need to update the request table!
SELECT r1.`Request ID`, s1.`Service ID`, r1.`Customer ID`, r1.`Admin ID`, r1.`Item ID`, r1.`Request Date`
FROM OSHES.Request r1
INNER JOIN OSHES.Item ON r1.`Item ID` = OSHES.Item.`Item ID`
INNER JOIN OSHES.Service s1 ON r1.`Request ID` = s1.`Request ID`
WHERE `Service Status` = "Waiting for approval";

-- find all services that needs to be completed and services that are completed
-- I cannot complete an already completed service, on those "In Progress"
SELECT `Admin ID`, `Request ID`, `Service ID`, `Service Status`
FROM `Service`
WHERE `Service Status` = "Completed" OR `Service Status` = "In Progress";

-- when approving a "waiting for approval request", update the request using request id to Approved
-- and update the admin ID of that request to "your_admin_id" as all requests starts off as "NULL"
-- update the admin ID of the Service Table as well from NULL -> admin_id
-- then update the service table to have the service status to be "In Progress"
START TRANSACTION;

UPDATE `Request`
SET `Request Status` = "Approved",
	`Admin ID` = "admin" -- var
WHERE `Request ID` = 7; -- var

UPDATE `Service`
SET `Service Status` = "In Progress",
	`Admin ID` = "admin" -- var
WHERE `Service ID` = 4; -- var

COMMIT;

-- when completing a service, update the request to "Completed" using the request id
-- then update the service table to "Completed" for service status
START TRANSACTION;

UPDATE `Request` 
SET `Request Status` = "Completed"
WHERE `Request ID` = 7 -- var
	AND `Request Status` = "Approved";

UPDATE `Service`
SET `Service Status` = "Completed"
WHERE `Service ID` = 4 -- var
	AND `Service Status` = "In Progress";

COMMIT;


-- insert service
INSERT INTO `Service` (`Service Status`, `Admin ID`, `Request ID`)
VALUES("Waiting for approval", "admin", 1);

SELECT * FROM `Service`;
DELETE FROM `Service`;