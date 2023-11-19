CREATE DATABASE IF NOT EXISTS adventureworks;
CREATE TABLE  `adventureworks`.`address` (
  `AddressID` int(11) NOT NULL AUTO_INCREMENT,
  `AddressLine1` varchar(60) NOT NULL,
  `AddressLine2` varchar(60) DEFAULT NULL,
  `City` varchar(30) NOT NULL,
  `StateProvinceID` int(11) NOT NULL,
  `PostalCode` varchar(15) NOT NULL,
  `ModifiedDate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
   PRIMARY KEY (`AddressID`)
);

select * from `adventureworks`.`address`;