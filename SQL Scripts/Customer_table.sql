CREATE DATABASE OSHES;

USE OSHES;

CREATE TABLE `Customer`(
  `Customer ID` CHAR(36) NOT NULL UNIQUE,
  `Password` CHAR(60) NOT NULL UNIQUE,
  `Address` VARCHAR(150) NOT NULL,
  `Phone Number` INT NOT NULL,
  `Name` VARCHAR(100) NOT NULL,
  `Gender` VARCHAR(10) NOT NULL CHECK (`Gender` IN ("Male", "Female", "Other")),
  `Email Address` VARCHAR(250) NOT NULL,
  PRIMARY KEY (`Customer ID`)
);

DROP TABLE `Customer`;