create database college;
#create database if not exists college;
#drop database if exists company;

use college;

create table student(
id int primary key,
name varchar(50),
age int not null
);

insert into student values(1,"AMAN", 26);
insert into student values(2,"PRATIP", 22);
insert into student values(3,"BIJU", 23);
insert into student values(4,"SOUNAK", 21);
select * from student;
#show databases;
show tables;

/*QUESTION: create a database for your company named XYZ.
step 1: create a table inside this DB to store empoyee info (id, name, and salary).
step 2: add the following information in the DB
        1. "ADAM", 25000
        2. "BOB", 30000
        3. "JONES", 40000
step 3: select & view all your table data */
CREATE DATABASE XYZ;
USE XYZ;
CREATE TABLE EMPLOYEE (
ID INT PRIMARY KEY, NAME VARCHAR (50),
SALARY FLOAT
);
INSERT INTO EMPLOYEE
(ID, NAME, SALARY) 
VALUES
(1, "ADAM", 25000), 
(2, "BOB", 30000),
(3, "JONES", 40000);
SELECT*FROM EMPLOYEE INFORMATION;

#################################################################
create database exam;
use exam;
create table student(
rollno int primary key,
name varchar(50)
);
select * from student;
create table temp1 (
	id int unique
);
insert into temp1 values(101);
insert into temp1 values(101);
select * from temp1;

#################################################################

create database abc;
use abc;
create table emp (
	id int ,
   --  name varchar (50),
--     age int,
    -- city varchar(50),
   --  primary key (id,name)
   salary int default 25000
);
insert into emp (id) values (101);
select * from emp;

##################################################################

create database college;
use college;
-- DROP DATABASE COLLEGE;

create table student (
	rollno int primary key,
    name varchar(50),
    marks int not null,
    grade varchar(1),
    city varchar(20)
);
insert into student 
(rollno, name, marks, grade, city)
values
(101,"pratip", 78, "C", "PUNE"),
(102,"biju", 93, "A", "MUMBAI"),
(103,"kaju", 85, "B", "MUMBAI"),
(104,"raju", 96, "A", "DELHI"),
(105,"ajju", 12, "F", "DELHI"),
(106,"mizo", 82, "B", "DELHI");
select * from student;

-- alter table student
-- drop column age ;

-- alter table student
-- add column age int not null default 19;


-- alter table student
-- modify column age varchar(2);

-- alter table student
-- change age stu_age int;

-- insert into student 
-- (rollno, name, marks, stu_age)
-- values
-- (107,"jonathan", 80,100);

-- alter table student
-- drop column stu_age;

-- alter table stu
-- rename to student;

-- truncate table student;






-- GENERAL ORDER
/*select city
from student
where grade ="A"
group by city
having max(marks)>93
order by city asc;
*/

-- SELECT * FROM STUDENT;
-- SELECT name , marks FROM student;
-- select city from student;
-- select distinct city from student;
-- select * from student where marks>80 and city = "mumbai";
-- select * from student where marks>90 or city = "mumbai";
-- select * from student where marks between 80 and 90;
-- select * from student where city in ("delhi", "mumbai");
-- select * from student where city not in ("delhi", "mumbai");
-- select * from student limit 4;
-- select * from student order by city asc;
-- select * from student order by city desc;
-- select avg (marks) from student;
-- select max(marks) from student;
-- select min(marks) from student;
-- select city,name, count(rollno) from student group by city,name;


/* QUESTION : WRITE THE QUERY TO FIND AVG MARKS IN EACH CITY IN ASCENDING ORDER. */

-- select city, avg (marks) from student group by city order by city ;     [GROUP BY CLAUSE]

-- select city, avg (marks) from student group by city order by avg(marks) desc ;      -- for ecending we have to mention it 

-- select city, count(name) from student group by city having max(marks)>90;       [HAVING CLAUSE]

-- TABLE RELATED QUERIES    :   UPDATE
-- SET SQL_SAFE_UPDATES=0;  -- TO TURN OFF THE "SAFE" MODE 

-- update student set grade ="O"where grade = "A";
-- update student set grade="B" where marks between 80 and 90;
-- update student set marks = marks+1;
-- delete from student where marks<33; [when we delete some data we should be very carefull because we can't get it again]




SELECT *FROM STUDENT;

/* QUESTION : FOR THE GIVEN TABLE, FIND THE TOTAL PAYMENT ACCORDING TO EACH PAYMENT METHOD.

				CUSTOMER ID 	CUSTOMER NAME 		  	MODE				CITY
				101				OLIVIA BARRETT			NETBANKING			PORTLAND
                102				ETHAN SINCLAIR			CREDIT CARD			MIAMI
                103				MAYA HERNANDEZ			CREDIT CARD			SEATTLE
                104				LIAM DONOVAN			NETBANKING			DENVER
                105				SOPHIA NGUYEN			CREDIT CARD			NEW ORLEANS
                106				CALEB FOSTER			DEBIT CARD			MINNEAPOLIS
                107				AVA PATEL				DEBIT CARD			PHOENIX
                108				LUCAS CARTER			NETBANKING			BOSTON
                109				ISABELLA MARTINEZ		NETBANKING			NASHVILLE
                110				JACKSON BROOKS			CREDIT CARD			BOSTON
*/

CREATE DATABASE CUSTOMER;
USE CUSTOMER;
CREATE TABLE PAYMENT(
	CUSTOMERID INT PRIMARY KEY,
    CUSTOMERNAME VARCHAR(50),
    MODE VARCHAR(20),
    CITY VARCHAR(20)
);
-- DROP TABLE PAYMENT;
-- DROP DATABASE CUSTOMER;
 
INSERT INTO PAYMENT
(CUSTOMERID, CUSTOMERNAME, MODE, CITY)
VALUES

	(101,"OLIVIA BARRETT","NETBANKING","PORTLAND"),
	(102,"ETHAN SINCLAIR","CREDIT CARD","MIAMI"),
	(103,"MAYA HERNANDEZ","CREDIT CARD","SEATTLE"),
	(104,"LIAM DONOVAN","NETBANKING","DENVER"),
	(105,"SOPHIA NGUYEN","CREDIT CARD","NEW ORLEANS"),
	(106,"CALEB FOSTER","DEBIT CARD","MINNEAPOLIS"),
	(107,"AVA PATEL","DEBIT CARD","PHOENIX"),
	(108,"LUCAS CARTER","NETBANKING","BOSTON"),
	(109,"ISABELLA MARTINEZ","NETBANKING","NASHVILLE"),
	(110,"JACKSON BROOKS","CREDIT CARD","BOSTON");
                
SELECT MODE, COUNT(CUSTOMERID) FROM PAYMENT GROUP BY MODE;


##########################################################################################################
/*
-- FORIEGN  KEY & PRIMARY KEY
CREATE DATABASE UNIVERSITY;
USE UNIVERSITY;
-- DROP DATABASE UNIVERSITY;

create table student (
	rollno int primary key,
    name varchar(50),
    marks int not null,
    grade varchar(1),
    city varchar(20)
);
insert into student 
(rollno, name, marks, grade, city)
values
(101,"pratip", 78, "C", "PUNE"),
(102,"biju", 93, "A", "MUMBAI"),
(103,"kaju", 85, "B", "MUMBAI"),
(104,"raju", 96, "A", "DELHI"),
(105,"ajju", 12, "F", "DELHI"),
(106,"mizo", 82, "B", "DELHI");
CREATE TABLE DEPT (
	ID INT PRIMARY KEY,
    NAME VARCHAR(50)
);
-- DROP TABLE DEPT;
INSERT INTO DEPT 
VALUES
(101,"ENGLISH"),
(102,"IT");
SELECT * FROM DEPT;
UPDATE DEPT 
SET ID = 103
WHERE ID = 101;

CREATE TABLE TEACHER(
	ID INT PRIMARY KEY,
    NAME VARCHAR(50),
    DEPT_ID INT,
    FOREIGN KEY (DEPT_ID) REFERENCES DEPT(ID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);
INSERT INTO TEACHER 
VALUES
(101,"ADAM", 101),
(102,"BOB",102);
SELECT * FROM TEACHER;
-- DROP TABLE TEACHER;
*/

/* QUESTION : IN THE STUDENT TABLE :
				A. CHANGE THE NAME OF THE COLUMN "NAME" TO "FULL_NAME".
                B. DELETE ALL THE STUDENTS WHO SCORED MARKS LESS THAN 80.
                C. DELETE THE COLUMN FOR GRADES.
*/

/*create database college;
use college;
-- DROP DATABASE COLLEGE;

create table student (
	rollno int primary key,
    name varchar(50),
    marks int not null,
    grade varchar(1),
    city varchar(20)
);
insert into student 
(rollno, name, marks, grade, city)
values
(101,"pratip", 78, "C", "PUNE"),
(102,"biju", 93, "A", "MUMBAI"),
(103,"kaju", 85, "B", "MUMBAI"),
(104,"raju", 96, "A", "DELHI"),
(105,"ajju", 12, "F", "DELHI"),
(106,"mizo", 82, "B", "DELHI");
select * from student;
-- A. CHANGE THE NAME OF THE COLUMN "NAME" TO "FULL_NAME". 
alter table student
change name full_name  varchar(50);

-- B. DELETE ALL THE STUDENTS WHO SCORED MARKS LESS THAN 80.
delete from student
where marks<80;

-- C. DELETE THE COLUMN FOR GRADES.
alter table student 
drop column grade;
 */
########################################################################
 
-- joins
create database college;
use college;
-- drop database college;

create table student(
	id int primary key,
    name varchar(50)
);

insert into student (id, name)
values
(101,"adam"),
(102,"bob"),
(103,"casey");
select * from student;

create table course(
	id int primary key,
    course varchar(50)
);

insert into course (id, course)
values
(102,"english"),
(105,"math"),
(103,"science"),
(107,"computer science");
select * from course;
 
-- WRITE SQL COMMANDS TO DISPLAY THE LEFT EXCLUSIVE JOIN & THE RIGHT EXCLUSIVE JOIN:
select * from student as s
left join course as c
on s.id=c.id
where c.id is null;

select * from student as s
right join course as c
on s.id=c.id
where s.id is null;

-- WRITE SQL COMMANDS TO DISPLAY THE COMBINE OF THE LEFT EXCLUSIVE JOIN & THE RIGHT EXCLUSIVE JOIN:
select * from student as s
left join course as c
on s.id=c.id
where c.id is null
union
select * from student as s
right join course as c
on s.id=c.id
where s.id is null;



-- FOR SELF JOIN
create table employee(
	id int primary key,
    name varchar(50),
    manager_id int
);

insert into employee (id , name,manager_id)
values
(101,"adam",103),
(102,"bob",104),
(103,"casey", null),
(104,"donald", 103);
select * from employee;

select a.name as manager_name, b.name
from employee as a
join employee as b
on a.id = b.manager_id;

-- UNION
select name from employee
union 
select name from employee;

-- UNION ALL
select name from employee
union all
select name from employee;

-- FULL JOIN
select * from student as s
left join course as c
on s.id=c.id
UNION
select * from student as s
right join course as c
on s.id=c.id;

-- RIGHT JOIN
select * from student as s
right join course as c
on s.id=c.id;

-- LEFT JOIN
select * from student as s
left join course as c
on s.id=c.id;

-- INNER JOIN
select * from student
inner join course
on student.id =course.id;

##########################################################################

-- SQL SUB QUERIES

create database college;
use college;
-- DROP DATABASE COLLEGE;

create table student (
	rollno int primary key,
    name varchar(50),
    marks int not null,
    grade varchar(1),
    city varchar(20)
);
insert into student 
(rollno, name, marks, grade, city)
values
(101,"pratip", 78, "C", "PUNE"),
(102,"biju", 93, "A", "MUMBAI"),
(103,"kaju", 85, "B", "MUMBAI"),
(104,"raju", 96, "A", "DELHI"),
(105,"ajju", 12, "F", "DELHI"),
(106,"mizo", 82, "B", "DELHI");
select * from student;

select avg (marks) from student;
select name, marks from student where marks > 74.3333;
-- SUB QUERIES [EX. : 1]
select name, marks
from student
where marks > (select avg (marks)
from student);

-- [EX. : 2] 
select rollno from student where rollno % 2 = 0;
select name,rollno from student where rollno in (102,104,106);

select name,rollno from student where rollno in(select rollno from student where rollno % 2 = 0);

-- SUB QUERIES EXAMPLE WITH FROM
select * from student where city = "delhi";

select max(marks) from (select * from student where city = "delhi")as temp;
-- another methode
select max(marks) from student where city ="mumbai";

-- SUB QUERIES EXAMPLE WITH SELECT
select (select max(marks) from student), name from student;


-- MySQL VIEWS                  it's a virtual table not the real table.
create view view1 as
select rollno, name from student;
select * from view1;
-- drop view view1;



 





















    

