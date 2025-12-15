CREATE DATABASE Student;

USE Student;

CREATE TABLE Student(
rollNo INT PRIMARY KEY,
name VARCHAR(50),
marks INT NOT NULL,
grade VARCHAR(1),
city VARCHAR(50)
);

INSERT INTO Student(rollNo,name,marks,grade,city) 
VALUES(101,"Nikhil",99,"A","MUMBAI"),
(102,"Krutik",93,"A","MUMBAI"),
(103,"Aaadi",91,"A","MUMBAI"),
(104,"Pratik",29,"F","MUMBAI"),
(105,"Satish",59,"C","MUMBAI"),
(106,"Vipul",48,"D","MUMBAI");

SELECT * FROM Student;
SELECT name,marks from Student;
SELECT * FROM Student WHERE marks > 70;
SELECT * FROM Student WHERE marks > 70 AND city = "MUMBAI";


CREATE DATABASE CollegeInfo;
USE CollegeInfo;

CREATE TABLE department(
id INT PRIMARY KEY,
name varchar(50)
;

CREATE TABLE TeacherDepartment(
id int PRIMARY KEY,
name varchar(60),
deptId int,
FOREIGN KEY (deptId) REFERENCES department(id)
ON DELETE CASCADE     /*help if you make change any changes to department table it also reflect here*/
ON UPDATE CASCADE	  /*help if you make change any changes to department table it also reflect here*/
);

INSERT INTO department VALUES(101,"COMMERCE"),(102,"IT"),(103,"ARTS");
SELECT * FROM department;

UPDATE department
SET id = "104"    
WHERE id = "101";

INSERT INTO TeacherDepartment VALUES(101,"Nik",101),(102,"Krutik",102),(103,"Janvi",103);
SELECT * FROM TeacherDepartment;
