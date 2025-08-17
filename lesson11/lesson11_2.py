import streamlit as st
import pandas as pd

st.title("我的第一個Streamlit應用")

# 載入數據
data = pd.DataFrame({
    '欄位A': [1, 2, 3],
    '欄位B': [4, 5, 6]
})

# 顯示表格
st.table(data)

# 互動元件例子
name = st.text_input("請輸入你的名字")
if st.button("送出"):
    st.write(f"哈囉，{name}！")