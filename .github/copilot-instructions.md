# Copilot 專案指引

這個專案是一個 PostgreSQL 和 Python 的教學資源，主要關注資料庫操作和數據分析。以下是重要的專案資訊：

## 專案結構

- `lesson3/`：SQL 基礎語法教學，包含建立和管理資料表
- `lesson4/`：包含 `world.csv` 數據集
- `lesson5/`：進階 SQL 和數據分析內容
- `lesson6/`：台鐵車站進出站資訊分析專案
  - `台鐵車站資訊_202507131451.csv`：車站基本資料
  - `每日各站進出站人數_202507131451.csv`：進出站統計數據
  - `進出站資訊.sql`：資料庫結構定義

## 資料庫結構

主要的資料表結構：

```sql
-- 台鐵車站資訊表
CREATE TABLE public.台鐵車站資訊 (
    "stationCode" int4 NOT NULL PRIMARY KEY,
    "stationName" varchar(50),
    "name" varchar(50),
    "stationAddrTw" varchar(50),
    "stationTel" varchar(50),
    gps varchar(50),
    "haveBike" varchar(50)
);

-- 每日進出站人數表
CREATE TABLE public.每日各站進出站人數 (
    日期 date,
    車站代碼 int4,
    進站人數 int4,
    出站人數 int4,
    FOREIGN KEY (車站代碼) REFERENCES public.台鐵車站資訊("stationCode")
);
```

## 命名規範

- 資料表名稱使用中文，以反映其實際用途
- 欄位名稱根據數據性質使用中文或英文
- 主鍵和外鍵關係應明確定義

## 資料處理原則

1. CSV 檔案匯入時需注意編碼格式（建議使用 UTF-8）
2. 日期格式統一使用 `date` 型別
3. 數值型資料使用適當的整數型別（int4）

## 建議的開發工作流程

1. 先檢視課程文件（`.md` 檔案）了解概念
2. 參考 SQL 檔案中的表結構定義
3. 實作資料匯入和分析功能
4. 確保外鍵關係正確性
