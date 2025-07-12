## world 欄位擷取
ˋˋˋsql

SELECT 洲名,國家,日期,總確認數,總死亡數,新增死亡數
FROM world;


## 問題:

### 1.查詢亞洲總共多少人死亡
ˋˋˋsql

SELECT MAX (總死亡數) AS 亞洲總死亡數
FROM world
WHERE 洲名='亞洲';


### 2.查詢全世界2020年的總確診數?
ˋˋˋsql

SELECT MAX (總確診數) AS 全世界總確診數
FROM world
WHERE 日期 BETWEEN '2020-01-01'  AND '2020-12-31';


### 3.查國家名有"阿"字,總死亡數大於10000?
ˋˋˋsql

SELECT MAX(總死亡數) AS 國家總死亡數, 國家
FROM world
WHERE 國家 LIKE '%阿%' AND 總死亡數 > 10000
GROUP BY 國家;


### 4.查詢哪個國家總確診數最多
ˋˋˋsql

SELECT MAX(總確診數) AS 國家總確診數, 國家
FROM world
GROUP BY 國家
ORDER BY 國家總確診數 DESC
LIMIT 1;



### 5.查詢亞洲台灣 2020-06-25 的總確診數
ˋˋˋsql

SELECT 總確診數 AS "0625台灣總確診數"
FROM world
WHERE 日期 ='2020-06-25' AND 國家='台灣';


### 6.總死亡數最高的國家
ˋˋˋsql

SELECT MAX(總死亡數) AS 國家總死亡數, 國家
FROM world
GROUP BY 國家
ORDER BY 國家總死亡數 DESC
LIMIT 1;


### 7.台灣有多少人在2020確診?
ˋˋˋsql

SELECT MAX(總確診數) AS 台灣2020確診數
FROM world
WHERE 日期 BETWEEN'2020-01-01' AND'2020-12-31' AND 國家='台灣';



### 8.排序各國總確診數
ˋˋˋsql

SELECT MAX(總確診數) AS 總確診數,國家
FROM world
GROUP BY 國家
ORDER BY 總確診數 DESC;


### 9.查詢每百萬確診人數


### 10.台灣哪個月死亡人數最多人
ˋˋˋsql

SELECT TO_CHAR(日期, 'YYYY-MM') AS 月份,MAX(總死亡數) AS 總死亡數
FROM world
WHERE 國家='台灣'
GROUP BY 月份
ORDER BY 總死亡數 DESC
LIMIT 1;


### 11.在哪個年度及月分，死亡數達到高峰
ˋˋˋsql

SELECT TO_CHAR(日期, 'YYYY-MM') AS 月份,MAX(總死亡數) AS 總死亡數
FROM world
GROUP BY 月份
ORDER BY 總死亡數 DESC
LIMIT 1;


### 12.多明尼加確診數有多少?
ˋˋˋsql

SELECT MAX(總死亡數) AS 總死亡數
FROM world
WHERE 國家='多明尼加';


### 13.查詢哪個國家總確診數最少
ˋˋˋsql

SELECT MAX(總確診數) AS 國家總確診 ,國家
FROM world
GROUP BY 國家
ORDER BY 國家總確診 
LIMIT 1;


### 14.查那個國家的死亡人數最低的前10名的國家
ˋˋˋsql

SELECT MAX(總死亡數) AS 國家總死亡數 ,國家
FROM world
GROUP BY 國家
ORDER BY 國家總死亡數 
LIMIT 10;

### 15.查各國總死亡數佔確診數比例
ˋˋˋsql

SELECT 
  MAX(總死亡數) * 1.0 / NULLIF(MAX(總確診數), 0) AS 死亡率,
  國家
FROM world
GROUP BY 國家;

### 16.哪一日死亡人數最多
ˋˋˋsql

SELECT 總死亡數,日期
FROM world
ORDER BY 總死亡數 DESC
LIMIT 1;


### 17.2021 年各州總死亡數
ˋˋˋsql

SELECT MAX(總死亡數) AS 總死亡數 ,洲名
FROM world
WHERE 日期 BETWEEN '2021-01-01' AND'2021-12-31' 
GROUP BY 洲名;

### 18.查詢 歐洲 2020-06-15 的總死亡數
ˋˋˋsql

SELECT MAX(總死亡數) AS 歐洲總死亡數 
FROM world
WHERE 日期 = '2021-06-15'  AND
洲名='歐洲';

### 19.查詢總確診數單日大於5筆
ˋˋˋsql

SELECT 總確診數 , 日期 
FROM world
WHERE 總確診數>5;

### 20.查詢各洲死亡佔確診數佔比
ˋˋˋsql

SELECT 
  MAX(總死亡數) * 1.0 / NULLIF(MAX(總確診數), 0) AS 死亡率,
  洲名
FROM world
GROUP BY 洲名;


ˋˋˋsql
SELECT MAX (總確診數) AS 總確診數
FROM world
WHERE 國家='台灣' AND 日期 BETWEEN '2020-01-01'  AND '2020-12-31';

ˋˋˋ


| 總確診數 | 
| --- |
| 700 |
