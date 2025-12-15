#TEST - 1 Questions

CREATE DATABASE Test1;

USE Test1;

CREATE TABLE StudentInfo(
id INT PRIMARY KEY,
StudentName VARCHAR(20),
StudentEmail VARCHAR(30)
);

INSERT INTO StudentInfo VALUES(1,"Nikhil","Nikhil@gmail.com"),(2,"Krutik","Krutik@gamil.com"),(3,"Krutik","Krutik@gmail.com");
SELECT * FROM StudentInfo;

SET SQL_SAFE_UPDATES = 0;

#Write a query to remove duplicate values from a table without using DISTINCT.
DELETE t1 FROM StudentInfo t1
JOIN StudentInfo t2
ON t1.StudentName = t2.StudentName
AND t1.id > t2.id;

SELECT DISTINCT StudentName
FROM StudentInfo;

#How can you calculate the total number of rows in a table in MySQL?
SELECT COUNT(*) AS TotalRows
FROM StudentInfo;

#How do you connect to a MySQL database using the command-line interface?
mysql -u root -p

#How can you find the highest or lowest value in a column in MySQL?
SELECT MAX(id) AS HighestValue
FROM StudentInfo;

SELECT MIN(id) AS LowestValue
FROM StudentInfo;

#Display all the orders placed in the last 30 days from a table orders(order_date).
SELECT *
FROM orders
WHERE order_date >= NOW() - INTERVAL 30 DAY;

#Explain 1NF, 2NF, and 3NF with examples in 2–3 lines each.

#Write an SQL query to fetch all records from a table named 'students'.
SELECT * 
FROM students;

#Write a query to print min salary (10000) to max (50000) employees.
SELECT *
FROM employees
WHERE salary BETWEEN 10000 AND 50000;

#ANOTHER WAY
SELECT *
FROM employees
WHERE salary >= 10000 AND salary <= 50000;















