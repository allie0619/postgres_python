/* 建立STUDENT資料*/
CREATE TABLE student(
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(20),
    major VARCHAR(20),
    PRIMARY KEY(student_id)
);

/* 新增資料*/
INSERT INTO student VALUES(1,'小白','歷史')
INSERT INTO student VALUES(2,'小黑','生物')
INSERT INTO student VALUES(3,'小綠','NULL')

INSERT INTO student(name,major) VALUES('小綠','歷史');