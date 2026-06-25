import streamlit as st

st.title("🎭 推しスケ")

name = st.text_input("芸人名")

if st.button("検索"):
    st.write("検索する芸人:", name)
