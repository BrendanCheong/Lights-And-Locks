-- find services that need to be approved, which are request that automatically create services in the service table
-- when updating a service, I also need to update the request table!
SELECT r1.`Request ID`, r1.`Customer ID`, r1.`Admin ID`, r1.`Item ID`, r1.`Request Date`, s1.`Service ID`
FROM OSHES.Request r1
INNER JOIN OSHES.Item ON r1.`Item ID` = OSHES.Item.`Item ID`
INNER JOIN OSHES.Service s1 ON r1.`Request ID` = s1.`Request ID`
WHERE s1.`Service Status` = "Waiting for approval";

-- insert service
INSERT INTO `Service` (`Service Status`, `Admin ID`, `Request ID`)
VALUES("Waiting for approval", "admin", 1);

SELECT * FROM `Service`;