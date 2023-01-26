-- Необходимо создать базу данных Академия (Academy), 
-- которая будет содержать информацию о сотрудниках и 
-- внутреннем устройстве академии.
-- Описание базы данных находится в конце этого файла.
-- Задание 2
-- Для базы данных Академия создайте такие запросы:

DROP TABLE IF EXISTS "py23_Departments";
CREATE TABLE IF NOT EXISTS "py23_Departments" (
	"id"	INTEGER NOT NULL UNIQUE,
	"Finansing"	INTEGER NOT NULL DEFAULT 0 CHECK(Finansing >=0),
	"Name"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)     )
INSERT INTO "py23_Departments" VALUES("1","1491","Пррграмирование");  
INSERT INTO "py23_Departments" VALUES("2","4181","Дизайн");
INSERT INTO "py23_Departments"  VALUES("3","44199","Сетевые технологии"); 
INSERT INTO "py23_Departments"  VALUES("4","22199", “Computer Science”); 



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
INSERT INTO "py23_Groups" (id,Name,Rate,Years) VALUES("1","FNNH",3,2);  
INSERT INTO "py23_Groups" (id,Name,Rate,Years) VALUES("3","UYUIK",4,5);   
INSERT INTO "py23_Groups" (id,Name,Rate,Years) VALUES("2","Дизайн",2,5);   


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

-- Описание
-- База данных Академия (Academy) содержит информацию
--  о сотрудниках и внутреннем устройстве академии.
-- Преподаватели, читающие лекции в академии представлены в виде таблицы Преподаватели (Teachers),
-- в которой собрана основная информация, такая как: имя, фамилия, 
-- данные о зарплате, а также дата приема на работу.
-- Также в базе данных присутствует информация о 
-- группах, хранимая в таблице Группы (Groups). Данные об 
-- факультетах и кафедрах содержатся в таблицах Факультеты (Faculties) и Кафедры (Departments) соответственно.
-- Таблицы
-- Ниже представлено детальное описание структуры 
-- каждой таблицы.
-- Кафедры (Departments)
-- ■ Идентификатор (Id). Уникальный идентификатор 
-- кафедры.
-- ▶ Тип данных — int.
-- ▶ Авто приращение.
-- ▶ Не может содержать null-значения.
-- ▶ Первичный ключ.
-- ■ Финансирование (Financing). Фонд финансирования -- кафедры.
-- ▶ Тип данных — money.
-- ▶ Не может содержать null-значения.
-- ▶ Не может быть меньше 0.
-- ▶ Значение по умолчанию — 0.
-- ■ Название (Name). Название кафедры.
-- ▶ Тип данных — nvarchar(100).
-- ▶ Не может содержать null-значения.
-- ▶ Не может быть пустым.
-- ▶ Должно быть уникальным.
-- Факультеты (Faculties)
-- ■ Идентификатор (Id). Уникальный идентификатор 
-- факультета.
-- ▶ Тип данных — int.
-- ▶ Авто приращение.
-- ▶ Не может содержать null-значения.
-- ▶ Первичный ключ.
-- ■ Декан (Dean). Декан факультета.
-- ▶ Тип данных — nvarchar(max).
-- ▶ Не может содержать null-значения.
-- ▶ Не может быть пустым.
-- ■ Название (Name). Название факультета.
-- ▶ Тип данных — nvarchar(100).
-- ▶ Не может содержать null-значения.
-- ▶ Не может быть пустым.
-- ▶ Должно быть уникальным.
-- Группы (Groups)
-- ■ Идентификатор (Id). Уникальный идентификатор 
-- группы.
-- ▶ Тип данных — int.
-- ▶ Авто приращение.
-- ▶ Не может содержать null-значения.
-- ▶ Первичный ключ.
-- ■ Название (Name). Название группы.
-- ▶ Тип данных — nvarchar(10).
-- ▶ Не может содержать null-значения.
-- ▶ Не может быть пустым.
-- ▶ Должно быть уникальным.
-- ■ Рейтинг (Rating). Рейтинг группы.
-- ▶ Тип данных — int.
-- ▶ Не может содержать null-значения.
-- ▶ Должно быть в диапазоне от 0 до 5.
-- ■ Курс (Year). Курс (год) на котором обучается группа.
-- ▶ Тип данных — int.
-- ▶ Не может содержать null-значения.
-- ▶ Должно быть в диапазоне от 1 до 5.
-- Преподаватели (Teachers)
-- ■ Идентификатор (Id). Уникальный идентификатор 
-- преподавателя.
-- ▶ Тип данных — int.
-- ▶ Авто приращение.
-- ▶ Не может содержать null-значения.
-- ▶ Первичный ключ.
-- ■ Дата трудоустройства (EmploymentDate). Дата приема 
-- преподавателя на работу.
-- ▶ Тип данных — date.
-- ▶ Не может содержать null-значения.
-- ▶ Не может быть меньше 01.01.1990.
-- ■ Ассистент (IsAssistant). Является ли преподаватель 
-- ассистентом.
-- ▶ Тип данных — bit.
-- ▶ Не может содержать null-значения.
-- ▶ Значение по умолчанию — 0.
-- ■ Профессор (IsProfessor). Является ли преподаватель 
-- профессором.
-- ▶ Тип данных — bit.
-- ▶ Не может содержать null-значения.
-- ▶ Значение по умолчанию — 0.
-- ■ Имя (Name). Имя преподавателя.
-- ▶ Тип данных — nvarchar(max).
-- ▶ Не может содержать null-значения.
-- ▶ Не может быть пустым.
-- ■ Должность (Position). Должность преподавателя.
-- ▶ Тип данных — nvarchar(max).
-- ▶ Не может содержать null-значения.
-- ▶ Не может быть пустым.
-- ■ Надбавка (Premium). Надбавка преподавателя.
-- ▶ Тип данных — money.
-- ▶ Не может содержать null-значения.
-- ▶ Не может быть меньше 0.
-- ▶ Значение по умолчанию — 0.
-- ■ Ставка (Salary). Ставка преподавателя.
-- ▶ Тип данных — money.
-- ▶ Не может содержать null-значения.
-- ▶ Не может быть меньше либо равно 0.
-- ■ Фамилия (Surname). Фамилия преподавателя.
-- ▶ Тип данных — nvarchar(max).
-- ▶ Не может содержать null-значения.
-- ▶ Не может быть пустым
