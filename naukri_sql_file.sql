---creating the database
CREATE DATABASE edulab;


--- Using the edulab databse
USE edulab;


--- creating the dataanalyst_ncr table consiting of all the columns
CREATE TABLE `edulab`.`dataanalyst_ncr` (
  `job_title` VARCHAR(512) NULL,
  `experience_required` VARCHAR(45) NULL,
  `company_name` VARCHAR(512) NULL,
  `job_description_page` VARCHAR(512) NULL,
  `key_skills` VARCHAR(1024) NULL,
  `job_description` VARCHAR(2048) NULL,
  `salary` VARCHAR(224) NULL,
  `job_id` INT NOT NULL AUTO_INCREMENT,
  `last_updated_on` DATETIME NULL,
  PRIMARY KEY (`job_id`));


---creating the location_jobs table consisting of all the columns

CREATE TABLE `edulab`.`location_jobs` (
  `job_id` INT NOT NULL,
  `location_id` INT NOT NULL,
  `location` VARCHAR(1024) NULL,
  PRIMARY KEY (`job_id`, `location_id`));

--- creating foreign key using both the table

ALTER TABLE `edulab`.`location_jobs` 
ADD CONSTRAINT `job_id`
  FOREIGN KEY (`job_id`)
  REFERENCES `edulab`.`dataanalyst_ncr` (`job_id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
