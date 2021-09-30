SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- DROP SCHEMA IF EXISTS `OSHES` ;
CREATE SCHEMA IF NOT EXISTS `OSHES` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
SHOW WARNINGS;
USE `OSHES` ;

-- -----------------------------------------------------
-- Table `OSHES`.`Customer`
-- -----------------------------------------------------
-- DROP TABLE IF EXISTS `OSHES`.`Customer` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `OSHES`.`Customer` (
  `Customer ID` VARCHAR(255) NOT NULL,
  `Password` VARCHAR(255) NOT NULL,
  `Name` VARCHAR(100) NOT NULL,
  `Gender` VARCHAR(10) NOT NULL,
  `PhoneNumber` CHAR(8) NOT NULL,
  `Address` VARCHAR(255) NOT NULL,
  `Email` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`Customer ID`),
  UNIQUE INDEX `Customer ID_UNIQUE` (`Customer ID` ASC))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `OSHES`.`Product`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `OSHES`.`Product` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `OSHES`.`Product` (
  `Product ID` INT NOT NULL,
  `Model` VARCHAR(15) NOT NULL,
  `Category` VARCHAR(15) NOT NULL,
  `Warranty` INT NOT NULL,
  `Price` INT NOT NULL,
  `Cost` INT NOT NULL,
  PRIMARY KEY (`Product ID`),
  UNIQUE INDEX `Product ID_UNIQUE` (`Product ID` ASC))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `OSHES`.`Administrator`
-- -----------------------------------------------------
-- DROP TABLE IF EXISTS `OSHES`.`Administrator` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `OSHES`.`Administrator` (
  `Admin ID` VARCHAR(255) NOT NULL,
  `Password` VARCHAR(60) NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `Gender` VARCHAR(10) NOT NULL,
  `PhoneNumber` CHAR(8) NOT NULL,
  PRIMARY KEY (`Admin ID`),
  UNIQUE INDEX `Admin ID_UNIQUE` (`Admin ID` ASC))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `OSHES`.`Item`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `OSHES`.`Item` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `OSHES`.`Item` (
  `Item ID` CHAR(4) NOT NULL,
  `Production Year` INT(4) NOT NULL,
  `Power Supply` VARCHAR(45) NOT NULL,
  `Color` VARCHAR(45) NOT NULL,
  `Factory` VARCHAR(45) NOT NULL,
  `Purchase Status` VARCHAR(45) NOT NULL,
  `Product ID` INT NOT NULL,
  PRIMARY KEY (`Item ID`),
  UNIQUE INDEX `Item ID_UNIQUE` (`Item ID` ASC),
  INDEX `fk_Item_Product1_idx` (`Product ID` ASC),
  CONSTRAINT `fk_Item_Product1`
    FOREIGN KEY (`Product ID`)
    REFERENCES `OSHES`.`Product` (`Product ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `OSHES`.`Request`
-- -----------------------------------------------------
-- DROP TABLE IF EXISTS `OSHES`.`Request` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `OSHES`.`Request` (
  `Request ID` INT NOT NULL AUTO_INCREMENT,
  `Request Date` DATE NOT NULL,
  `Request Status` VARCHAR(45) NOT NULL,
  `Customer ID` VARCHAR(255) NOT NULL,
  `Admin ID` VARCHAR(255),
  `Item ID` CHAR(4) NOT NULL UNIQUE,
  PRIMARY KEY (`Request ID`),
  UNIQUE INDEX `Request ID_UNIQUE` (`Request ID` ASC),
  INDEX `fk_Request_Customer_idx` (`Customer ID` ASC),
  INDEX `fk_Request_Administrator1_idx` (`Admin ID` ASC),
  INDEX `fk_Request_Item1_idx` (`Item ID` ASC),
  CONSTRAINT `fk_Request_Customer`
    FOREIGN KEY (`Customer ID`)
    REFERENCES `OSHES`.`Customer` (`Customer ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Request_Administrator1`
    FOREIGN KEY (`Admin ID`)
    REFERENCES `OSHES`.`Administrator` (`Admin ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Request_Item1`
    FOREIGN KEY (`Item ID`)
    REFERENCES `OSHES`.`Item` (`Item ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `OSHES`.`Service`
-- -----------------------------------------------------
-- DROP TABLE IF EXISTS `OSHES`.`Service` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `OSHES`.`Service` (
  `Service ID` INT NOT NULL AUTO_INCREMENT,
  `Service Status` VARCHAR(45) NOT NULL,
  `Admin ID` VARCHAR(255) NOT NULL,
  `Item ID` CHAR(4) NOT NULL,
  PRIMARY KEY (`Service ID`),
  UNIQUE INDEX `Service ID_UNIQUE` (`Service ID` ASC),
  INDEX `fk_Service_Administrator1_idx` (`Admin ID` ASC),
  INDEX `fk_Service_Item1_idx` (`Item ID` ASC),
  CONSTRAINT `fk_Service_Administrator1`
    FOREIGN KEY (`Admin ID`)
    REFERENCES `OSHES`.`Administrator` (`Admin ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Service_Item1`
    FOREIGN KEY (`Item ID`)
    REFERENCES `OSHES`.`Item` (`Item ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `OSHES`.`Purchase`
-- -----------------------------------------------------
-- DROP TABLE IF EXISTS `OSHES`.`Purchase` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `OSHES`.`Purchase` (
  `Item ID` CHAR(4) NOT NULL,
  `Purchase Date` DATE NOT NULL,
  `Customer ID` VARCHAR(255) NOT NULL,
  INDEX `fk_Purchase_Customer1_idx` (`Customer ID` ASC),
  PRIMARY KEY (`Item ID`),
  CONSTRAINT `fk_Purchase_Customer1`
    FOREIGN KEY (`Customer ID`)
    REFERENCES `OSHES`.`Customer` (`Customer ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Purchase_Item1`
    FOREIGN KEY (`Item ID`)
    REFERENCES `OSHES`.`Item` (`Item ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
