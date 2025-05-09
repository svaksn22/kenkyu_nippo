import streamlit as st
import time

# 日報



st.set_page_config(
    page_title="My new app",
    page_icon="🎈",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("研究記録アプリ")
st.text_area("研究内容", key='report', placeholder="研究内容を入力してください")
st.markdown(st.session_state.report)