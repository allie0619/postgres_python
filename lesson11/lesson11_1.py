# 當輸出df變數時,st.write()會自動執行
"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import datasource

st.sidebar.title("台鐵車站資訊")
st.sidebar.header("2023年各站進出人數")
st.subheader("進出站人數顯示區")

# 1
# stations = datasource.get_stations_names()
# station=st.sidebar.selectbox(
#     "請選擇車站",
#     (stations))

# 2
# @st.cache_resource
# def get_stations():
#     """取得車站資料"""
#     return datasource.get_stations_names()

# stations = get_stations()
# station = st.sidebar.selectbox(
#     "請選擇車站",
#     stations,
# )

# 3
@st.cache_resource
def get_stations():
    """取得車站資料"""
    return datasource.get_stations_names()

stations = get_stations()
if stations is None:
    st.error("無法取得車站資料，請稍後再試。")
    st.stop()

#sidebar要先顯示常用的車站名稱
#使用者可以很快的選擇
#如果不常用的車站名稱,再使用selectbox

# 先取前六個站為常用站（可改為固定清單或從使用者設定讀取）
common_stations = ['臺北', '桃園','新竹', '台中', '臺南', '高雄','其他'] 

# 在 sidebar 顯示常用站列表，並加上「其他」選項（當總站數大於常用站數時）

choice = st.sidebar.radio("快速選擇常用車站", common_stations)

if choice == "其他":
    station = st.sidebar.selectbox(
        "請選擇車站",
        stations,
    )
else:
    station = choice

st.write("您選擇的車站:", station)