USE OSHES;

CREATE TABLE `Test` (
	`testing id` VARCHAR(50) NOT NULL,
    `testing number` INT NOT NULL,
    Primary Key(`testing id`)
);

INSERT INTO `Test` (`testing id`, `testing number`) VALUES
("wassup", 1),
("hello", 2),
("world", 3)

SELECT * FROM `Test`;