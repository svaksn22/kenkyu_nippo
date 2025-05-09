import streamlit as st

# サイドバー定義
menu = ["ホーム", "記録"]

# 日報保持用

st.sidebar.title("メニュー")
for item in menu:
    st.sidebar.button(item)
# メインコンテンツ


st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

input_num=st.number_input("Input a number", value=0)
st.write("You entered:", input_num)
