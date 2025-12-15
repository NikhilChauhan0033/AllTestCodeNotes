CREATE DATABASE SQL_Practice;     /*command for create a database*/

DROP DATABASE SQL_Practice;			/*command for delete a database*/

USE SQL_Practice;     				/*USE is for now we will use this database for create our tables*/

/*GOOD HABIT FOR TO USE OF IF NOT EXISTS AND IF EXISTS FOR AVOIDING ERRORS*/
CREATE DATABASE IF NOT EXISTS SQL_Practice; 
DROP DATABASE IF EXISTS SQL_Practice;

CREATE TABLE Student1(   /*creation of table or create of our table schema schema mean design*/
id INT PRIMARY KEY,     /*primary key has 2 main features like not null and id should be unique*/
name VARCHAR(50),
age INT NOT NULL
);

INSERT INTO Student1 VALUES(1,"NIkhil",22); /*for add data to table*/
SELECT * FROM Student1;  					/*for view all data from table*/
SELECT name,age from Student1;             /*you can select like which column data you have to view*/
SELECT * FROM Student1 WHERE age>=18;      /*using where you can add an condition also we call it to clause*/
SELECT * FROM Student1 WHERE age>=18 AND id < 2;  /*you can add multiple conditions using AND*/
SELECT * FROM Student1 LIMIT 2;     /*like you can add an limit like how much data you want first 2 or etc*/
SELECT * FROM Student1 ORDER BY id ASC;  /*give you ascending order data using id*/
SELECT * FROM Student1 ORDER BY id DESC;  /*give you descending order data using id*/

INSERT INTO Student1 VALUES(2,"Aadi",14),(3,"Krutik",25); /*for add multiple data to table*/

DROP TABLE Student1;   /*for delete table*/

SHOW DATABASES;  /*Show all the database which there is our comupter*/

SHOW TABLES;     /*show the all currently use database tables */
SHOW TABLES;     /*show the all currently use database tables */
SHOW TABLES;     /*show the all currently use database tables */

SET SQL_SAFE_UPDATES = 0;  /*TRUN OFF THE SAFE MODE OF SQL IF YOU WANT UPDATE ANY DATA USE THIS FIRST*/
SET SQL_SAFE_UPDATES = 1;  /*TRUN ON THE SAFE MODE*/

UPDATE Student1    /*for update the data*/
SET age = 19 
WHERE name = "Aadi";

DELETE FROM Student1   /*for delete the data*/
WHERE age < 18;

SELECT * FROM Student1;

ALTER TABLE Student1   /*for add any column*/
ADD COLUMN Address varchar(300);

ALTER TABLE Student1  /*for delete any column*/
DROP COLUMN Address;

ALTER TABLE Student1 /*for rename any table */
RENAME TO Student1;

ALTER TABLE Student1 /*for change column namde */
CHANGE COLUMN age Age INT NOT NULL;

TRUNCATE TABLE Student1;   /*this will delete only all the tables values not table, drop delete the table with values*/

/*staring with joins*/

CREATE TABLE Student(
stuId INT PRIMARY KEY,
stuName VARCHAR(40)
);

INSERT INTO Student VALUES(1,"Nikhil"),(2,"Krutik"),(3,"Aadi");
INSERT INTO Student VALUES(4,"Dattu"),(5,"NanduBidi");

SELECT * FROM Student;

CREATE TABLE Course(
courId INT PRIMARY KEY,
courName VARCHAR(40),
FOREIGN KEY (courId) REFERENCES Student(stuId)
);

INSERT INTO Course VALUES(1,"IT"),(2,"rider"),(3,"arts"),(8,"Developer"),(9,"PanPati Shop");
INSERT INTO Course VALUES(8,"Developer"),(9,"PanPati Shop");

SELECT * FROM Course;

/*Inner Join*/
SELECT *
FROM Student as s
INNER JOIN Course as c
ON s.stuId = c.courId;

/*outer join have 3 joins*/
/*left join , right join , full join*/

/*left join*/
SELECT *
FROM Student as s
LEFT JOIN Course as c
ON s.stuId = c.courId;

/*right join */
SELECT *
FROM Student as s
RIGHT JOIN Course as c
ON s.stuId = c.courId;

/*full join*/
/*left join*/
SELECT *
FROM Student as s
LEFT JOIN Course as c
ON s.stuId = c.courId
UNION
/*Right join*/
SELECT *
FROM Student as s
RIGHT JOIN Course as c
ON s.stuId = c.courId;

/*Left Exclusive join*/
SELECT *
FROM Student as s
LEFT JOIN Course as c
ON s.stuId = c.courId
WHERE c.courId IS NULL;

/*Right Exclusive join*/
SELECT *
FROM Student as s
RIGHT JOIN Course as c
ON s.stuId = c.courId
WHERE c.courId IS NULL;




