
##匯入資料表(台鐵車站資訊,每日各站進出站人數)

## 在

```sql
ALTER TABLE "台鐵車站資訊" ADD PRIMARY KEY ("stationCode");

```

```sql
ALTER TABLE "每日各站進出站人數" ADD FOREIGN KEY ("車站代碼")
REFERENCES "台鐵車站資訊"("stationCode") ON DELETE SET NULL;
```



