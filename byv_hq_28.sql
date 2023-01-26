DROP TABLE IF EXISTS "py23_Departments";
CREATE TABLE IF NOT EXISTS "py23_Departments" (
	"id"	INTEGER NOT NULL UNIQUE,
	"Finansing"	INTEGER NOT NULL DEFAULT 0 CHECK(Finansing >=0),
	"Name"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)     )
INSERT INTO "py23_Departments" VALUES("1","1491","Пррграмирование");  
INSERT INTO "py23_Departments" VALUES("2","4181","Дизайн");
INSERT INTO "py23_Departments"  VALUES("3","44199","Сетевые технологии"); 
INSERT INTO "py23_Departments"  VALUES("4","22199",“Computer Science”); 

DROP TABLE IF EXISTS "py23_Faculties";
CREATE TABLE IF NOT EXISTS "py23_Faculties" (
	"id"	INTEGER UNIQUE,
	"Dean"	TEXT NOT NULL,
	"Name"	TEXT NOT NULL UNIQUE CHECK(NOT NULL),
	PRIMARY KEY("id" AUTOINCREMENT)     );
INSERT INTO "py23_Faculties" VALUES("1","Ярошкін Сергій Сергійович","ИТД";  
INSERT INTO "py23_Faculties" (Dean,Name) VALUES("Таран Андрій Ігорович","ЕКЛМН");   
INSERT INTO "py23_Faculties" (Dean,Name) VALUES("Белоусов Юрий Владимирович","ЕПРСТ");   

DROP TABLE IF EXISTS "py23_Groups" (
CREATE TABLE IF NOT EXISTS "py23_Groups" (
	"id"	INTEGER UNIQUE,
	"Name"	TEXT NOT NULL UNIQUE,
	"Rate"	INTEGER NOT NULL CHECK("Rate" >= 1  AND "Rate"<=5),
	"Years"	INTEGER NOT NULL CHECK("Years" >= 1  AND "Years"<=5),
	PRIMARY KEY("id" AUTOINCREMENT)
)
INSERT INTO "py23_Groups" (id,Name,Rate,Years) VALUES("1","ЯрошкінСергійСергійович",3,2);  
INSERT INTO "py23_Groups" (id,Name,Rate,Years) VALUES("3","ТаранАндрійІгорович",4,1);   
INSERT INTO "py23_Groups" (id,Name,Rate,Years) VALUES("2","Дизайн",2,3);   


DROP TABLE IF EXISTS "py23_Teachers";
CREATE TABLE IF NOT EXISTS "py23_Teachers" (
	"id"	INTEGER UNIQUE,
	"EmploymentDateDDMMYY"	INTEGER NOT NULL,
	"IsAssistant"	INTEGER NOT NULL DEFAULT 0,
	"IsProfessor"	INTEGER NOT NULL DEFAULT 0,
	"Name"	TEXT NOT NULL UNIQUE,
	"Surname"	TEXT NOT NULL,
    "Position"	TEXT NOT NULL,
	"Premium"	INTEGER NOT NULL DEFAULT 0 CHECK("Premium">=0),
	"Salary"	INTEGER NOT NULL CHECK("Salary">0),
	PRIMARY KEY("id" AUTOINCREMENT)     );
INSERT INTO "py23_Teachers" (id,EmploymentDateDDMMYY,IsAssistant,IsProfessor,Name,Surname,Position,Premium,Salary) 
VALUES("1",160299,0,1,"Ярошкін","Сергій","English",1000,1491);  
INSERT INTO "py23_Teachers" (id,EmploymentDateDDMMYY,IsAssistant,IsProfessor,Name,Surname,Position,Premium,Salary) 
VALUES("2",301197,1,0,"Таран","Андрій","Python",1200,481);   
INSERT INTO "py23_Teachers" (id,EmploymentDateDDMMYY,IsAssistant,IsProfessor,Name,Surname,Position,Premium,Salary) 
 VALUES("3",110588,1,0,"Стрельченко","Олександр","Html",950,142);   
-- 1. Вывести таблицу кафедр, но расположить ее поля в обратном порядке.№1 + сортировка по названию
select "Name","Finansing", "id"
from py23_Departments
order by "Name" ASC
-- 2. Вывести названия групп и их рейтинги с уточнением имен полей именем таблицы.
--  + сортировка по рейтингу от большего к меньшему + первые 3 
select "Name","Rate"
from "py23_Groups"
order by "Rate" DESC;
-- 5. Вывести фамилии преподавателей, которые являются профессорами и ставка которых превышает 1050.
select "Name"
from "py23_Teachers"
WHERE ("IsProfessor"==1 AND "Salary">1050)
-- 6. Вывести названия кафедр, фонд финансирования 
-- которых меньше 11000 или больше 25000. от 11000 до 25000
SELECT "Name", "Finansing"
from "py23_Departments"
WHERE ("Finansing"<=25000 AND "Finansing">=11000);
-- 7. Вывести названия факультетов кроме факультета “Computer Science”.
SELECT "Name"
from "py23_Departments"
WHERE ("Name"!="Computer Science");
-- Необязательное:
-- 8. Вывести фамилии и должности преподавателей, которые не являются профессорами.
select "Surname", "Position"
from "py23_Teachers"
WHERE ("IsProfessor"==0)

-- 9. Вывести фамилии, должности, ставки и надбавки 
-- ассистентов, у которых надбавка в диапазоне от 160 
-- до 550.
select "Surname", "Position", "Salary", "Premium"
from "py23_Teachers"
WHERE ("IsAssistant"==1 AND "Premium">= 160 AND "Premium"<550)
-- 10. Вывести фамилии и ставки ассистентов.
select "Surname", "Position"
from "py23_Teachers"
WHERE ("IsProfessor"==0)
-- 13. Вывести фамилии ассистентов, имеющих зарплату 
-- (сумма ставки и надбавки) не более 1200.
select "Surname"
from "py23_Teachers"
WHERE ("IsAssistant"==1 "Salary"+"Premium"<1200)

-- 14. Вывести названия групп 5-го курса, имеющих рейтинг 
-- в диапазоне от 2 до 4.
SELECT "Name"
from "py23_Groups"
WHERE ("Years"==5 AND "Rate">1 AND "Rate"<5);

-- 15. Вывести фамилии ассистентов со ставкой меньше 550 
-- или надбавкой меньше 200.
select "Surname"
from "py23_Teachers"
WHERE ("IsAssistant"==1 AND "Salary"<550 AND "Premium"<200)
