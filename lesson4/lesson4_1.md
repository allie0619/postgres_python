## world 欄位擷取
ˋˋˋsql
SELECT 洲名,國家,日期,總確認數,總死亡數,新增死亡數
FROM world;
ˋˋˋ

ˋˋˋsql

## 問題:

### 1.查詢亞洲總共多少人死亡
ˋˋˋsql
SELECT MAX (總死亡數) AS 亞洲總死亡數
FROM world
WHERE 洲名='亞洲';
ˋˋˋ

### 2.查詢全世界2020年的總確診數?
ˋˋˋsql
SELECT MAX (總確診數) AS 全世界總確診數
FROM world
WHERE 日期 BETWEEN '2020-01-01'  AND '2020-12-31';
ˋˋˋ

### 3.查國家名有"阿"字,總死亡數大於10000?
ˋˋˋsql
SELECT MAX(總死亡數) AS 國家總死亡數, 國家
FROM world
WHERE 國家 LIKE '%阿%' AND 總死亡數 > 10000
GROUP BY 國家;
ˋˋˋ

### 4.查詢哪個國家總確診數最多
ˋˋˋsql
SELECT MAX(總確診數) AS 國家總確診數, 國家
FROM world
GROUP BY 國家
ORDER BY 國家總確診數 DESC
LIMIT 1;
ˋˋˋ


### 5.查詢亞洲台灣 2020-06-25 的總確診數
ˋˋˋsql
SELECT 總確診數 AS "0625台灣總確診數"
FROM world
WHERE 日期 ='2020-06-25' AND 國家='台灣';
ˋˋˋ

### 6.總死亡數最高的國家
ˋˋˋsql
SELECT MAX(總死亡數) AS 國家總死亡數, 國家
FROM world
GROUP BY 國家
ORDER BY 國家總死亡數 DESC
LIMIT 1;
ˋˋˋ

### 7.台灣有多少人在2020確診?
ˋˋˋsql
SELECT MAX(總確診數) AS 台灣2020確診數
FROM world
WHERE 日期 BETWEEN'2020-01-01' AND'2020-12-31' AND 國家='台灣';
ˋˋˋ


### 8.排序各國總確診數
ˋˋˋsql
SELECT MAX(總確診數) AS 總確診數,國家
FROM world
GROUP BY 國家
ORDER BY 總確診數 DESC;
ˋˋˋ

### 9.查詢每百萬確診人數


### 10.台灣哪個月死亡人數最多人
ˋˋˋsql
SELECT TO_CHAR(日期, 'YYYY-MM') AS 月份,MAX(總死亡數) AS 總死亡數
FROM world
WHERE 國家='台灣'
GROUP BY 月份
ORDER BY 總死亡數 DESC
LIMIT 1;
ˋˋˋ

### 11.在哪個年度及月分，死亡數達到高峰
ˋˋˋsql
SELECT TO_CHAR(日期, 'YYYY-MM') AS 月份,MAX(總死亡數) AS 總死亡數
FROM world
GROUP BY 月份
ORDER BY 總死亡數 DESC
LIMIT 1;
ˋˋˋ

### 12.多明尼加確診數有多少?
SELECT MAX(總死亡數) AS 總死亡數
FROM world
WHERE 國家='多明尼加';


##14.查詢哪個國家總確診數最少
SELECT MAX(總確診數) AS 國家總確診 ,國家
FROM world
GROUP BY 國家
ORDER BY 國家總確診 
LIMIT 1;

##15.台灣每個月的死亡率

##16.查那個國家的死亡人數最低的前10名的國家
SELECT MAX(總死亡數) AS 國家總死亡數 ,國家
FROM world
GROUP BY 國家
ORDER BY 國家總死亡數 
LIMIT 10;

##17.查各國總死亡數佔確診數比例
SELECT 
  MAX(總死亡數) * 1.0 / NULLIF(MAX(總確診數), 0) AS 死亡率,
  國家
FROM world
GROUP BY 國家;

##18.哪一日死亡人數最多
SELECT 總死亡數,日期
FROM world
ORDER BY 總死亡數 DESC
LIMIT 1;


##19.2021 年各州總死亡數
SELECT MAX(總死亡數) AS 總死亡數 ,洲名
FROM world
WHERE 日期 BETWEEN '2021-01-01' AND'2021-12-31' 
GROUP BY 洲名;

##20.查詢 歐洲 2020-06-15 的總死亡數
SELECT MAX(總死亡數) AS 歐洲總死亡數 
FROM world
WHERE 日期 = '2021-06-15'  AND
洲名='歐洲';

##21.查詢總確診數單日大於5筆
SELECT 總確診數 , 日期 
FROM world
WHERE 總確診數>5;

##22.查詢各洲死亡佔確診數佔比
SELECT 
  MAX(總死亡數) * 1.0 / NULLIF(MAX(總確診數), 0) AS 死亡率,
  洲名
FROM world
GROUP BY 洲名;



SELECT MAX (總確診數) AS 總確診數
FROM world
WHERE 國家='台灣' AND 日期 BETWEEN '2020-01-01'  AND '2020-12-31';

ˋˋˋ


| 總確診數 | 
| --- |
| 700 |
