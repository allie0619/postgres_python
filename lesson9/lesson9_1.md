SELECT count (*) "筆數"
from "台鐵車站資訊";

SELECT count (name) as "台北車站筆數"
from "台鐵車站資訊"
where "stationAddrTw" like '％臺北％';

select *
from "每日各站進出站人數" left join "台鐵車站資訊" on "車站代碼" = "stationCode" 
where "stationName"='基隆';

select "name" as 站名 ,count("name") as 各站點筆數 ,avg ("進站人數") as "每年平均進站人數"
from "每日各站進出站人數" left join "台鐵車站資訊" on "車站代碼" = "stationCode" 
/*where "日期" between '2022-01-01' and  '2022-12-31' */
group by "name";

SELECT "name" AS 站名,date_part('year',"日期") AS "年份",COUNT("name") AS 筆數,AVG("進站人數") AS "進站人數"
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "車站代碼" = "stationCode"
WHERE "name" = '基隆'
GROUP BY "name","年份"
ORDER BY "進站人數" DESC;

SELECT
    t."stationName" AS "車站名稱",
    SUM(p."進站人數") AS "2022年進站總人數"
FROM "每日各站進出站人數" p
LEFT JOIN "台鐵車站資訊" t ON p."車站代碼" = t."stationCode"
WHERE DATE_PART('year', p."日期") = 2022
GROUP BY t."stationCode", t."stationName"
HAVING SUM(p."進站人數") > 5000000
ORDER BY SUM(p."進站人數") DESC;


/*
*基隆火車站2020,2021,2022,每年進站人數
*/
SELECT 
    s."stationName" as 車站名稱,
    EXTRACT(YEAR FROM r.日期) as 年份,
    SUM(r.進站人數) as 年度進站總人數
FROM 
    public.台鐵車站資訊 s
    JOIN public.每日各站進出站人數 r ON s."stationCode" = r.車站代碼
WHERE 
    s."stationName" = '基隆'
    AND EXTRACT(YEAR FROM r.日期) IN (2020, 2021, 2022)
GROUP BY 
    s."stationName",
    EXTRACT(YEAR FROM r.日期)
ORDER BY 
    年份;


/*
*基隆火車站,臺北火車站2020,2021,2022,每年進站人數
*/
SELECT 
    s."stationName" as 車站名稱,
    EXTRACT(YEAR FROM r.日期) as 年份,
    SUM(r.進站人數) as 年度進站總人數
FROM 
    public.台鐵車站資訊 s
    JOIN public.每日各站進出站人數 r ON s."stationCode" = r.車站代碼
WHERE 
    s."stationName" IN ('基隆', '臺北')
    AND EXTRACT(YEAR FROM r.日期) IN (2020, 2021, 2022)
GROUP BY 
    s."stationName",
    EXTRACT(YEAR FROM r.日期)
ORDER BY 
    s."stationName",
    年份;
/*
*查詢 2022 年平均每日進站人數超過 2 萬人的站點
*/
WITH daily_avg AS (
    SELECT 
        r.車站代碼,
        AVG(r.進站人數) as 平均每日進站人數
    FROM 
        public.每日各站進出站人數 r
    WHERE 
        EXTRACT(YEAR FROM r.日期) = 2022
    GROUP BY 
        r.車站代碼
    HAVING 
        AVG(r.進站人數) > 20000
)
SELECT 
    s."stationName" as 車站名稱,
    ROUND(d.平均每日進站人數, 0) as 平均每日進站人數
FROM 
    daily_avg d
    JOIN public.台鐵車站資訊 s ON s."stationCode" = d.車站代碼
ORDER BY 
    d.平均每日進站人數 DESC;