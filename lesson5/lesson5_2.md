## 刪除employee、branch資料表如果 employee資料表存在
DROP TABLE IF EXISTS employee ;    #CASCADE 關聯刪除
DROP TABLE IF EXISTS branch ; 

## 創建 employee資料表
CREATE TABLE employee(
    emp_id SERIAL,
    name VARCHAR(20),
    birth_date DATE,
    sex VARCHAR(1),
    salary INT,
    branch_id INT,
    sup_id INT,
    PRIMARY KEY(emp_id)
);

## 創建 branch資料表
CREATE TABLE branch(
    branch_id INT,
    branch_name(20),
    manager_id INT, 
    PRIMARY KEY(branch_id), 
    FOREIGN KEY(manager_id) REFERENCES employee(emp_id) ON DELETE SET NULL
);

## 在 employee資料表新增外鍵branch_id,sup_id
ALTER TABLE employee ADD FOREIGN KEY(branch_id) 
REFERENCES branch(branch_id) ON DELETE SET NULL ;

ALTER TABLE employee ADD FOREIGN KEY(sup_id) 
REFERENCES branch(emp_id) ON DELETE SET NULL ;