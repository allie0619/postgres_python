## 建立資料表的語法

ˋˋˋsql
CREATE TABLE [IF NOT EXISTS] table_name (
   column1 datatype(length) column_constraint,
   column2 datatype(length) column_constraint,
   ...
   table_constraints
);
```

ˋˋˋsql
## 建立一個student資料表
CREATE TABLE IF NOT EXISTS student(
    student_id SERIAL PRIMARY KEY,
    name  VARCHAR(20) NOT NULL,
    major VARCHAR(20) UNIQUE
);
ˋˋˋ
## 刪除一個student資料表
ˋˋˋsql

DROP TABLE IF EXISTS student;

ˋˋˋ
## 新增1筆資料
ˋˋˋsql

INSERT INTO student(name,major)
VALUESㄩ('呂育君','歷史');

ˋˋˋ
## 新增多筆資料
ˋˋˋsql

INSERT INTO student(name,major)
VALUES('小柱','生物'),('信忠','英語');

ˋˋˋ

## 取得資料

ˋˋˋsql
SELECT  name,major   
FROM student;

SELECT  *
FROM student
WHERE name='信忠';

SELECT  *
FROM student
WHERE major='歷史'
ORDER BY student_id DESC;    

SELECT  *
FROM student
WHERE major='歷史'
ORDER BY student_id DESC
LIMIT 1;     
ˋˋˋ
##修改和刪除

ˋˋˋsql
SELECT  *
FROM student
WHERE major='歷史'
ORDER BY student_id DESC
LIMIT 1;    

UPDATE student 
SET name='阿柱',
    major='數學'
WHERE student_id = 2;

DELETE FROM student
WHERE student_id = 2;

DELETE FROM student
WHERE student_id in (1,3);
ˋˋˋ
##更改日期型別和更新字串成為Date
ˋˋˋsql
ALTER TABLE world
ALTER COLUMN 日期 TYPE DATE
USING 日期 :: DATE ;
ˋˋˋ

