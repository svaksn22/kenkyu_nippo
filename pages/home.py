import streamlit as st
import time
import os
from datetime import datetime, timezone

# 日報
st.session_state.setdefault("state","start")
st.session_state.setdefault("start_time","登校前")

st.set_page_config(
    page_title="My new app",
    page_icon="🎈",
    layout="wide",
    initial_sidebar_state="expanded",
)

def check_log():
    if os.path.exists("log/state.txt"):
        with open("log/state.txt", "r") as f:
            line = f.readline()
            if line.split(" ")[0] == "start":
                st.session_state.state = "start"
            elif line.split(" ")[0] == "record":
                st.session_state.state = "record"
                st.session_state.start_time = line.split(" ")[1].strip()
            elif line.split(" ")[0] == "end":
                st.session_state.state = "end"
                st.session_state.start_time = line.split(" ")[1].strip()
                st.session_state.end_time = line.split(" ")[2].strip()
                st.session_state.report = line.split(" ")[3].strip()
    else:
        with open("log/state.txt", "w") as f:
            f.write("start")
        st.session_state.state = "start"


def record_start():
    st.session_state.start_time = datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d,%H:%M:%S")
    print(st.session_state.start_time)
    st.success("登校しました")
    st.session_state.state = "record"
    with open("log/state.txt", "w") as f:
        f.write(f"{st.session_state.state} {st.session_state.start_time}\n")


def record_report():
    st.session_state.end_time = datetime.now(timezone.utc).astimezone().strftime('%Y-%m-%d,%H:%M:%S')
    st.session_state.state = "end"
    with open("log/state.txt", "w") as f:
        f.write(f"{st.session_state.state} {st.session_state.start_time} {st.session_state.end_time} {st.session_state.report}\n")
    st.success("今日の研究内容を記録しました")

def main():
    if st.session_state.state == "start":
        st.write(f"{st.session_state.start_time}")
        st.button("登校する", on_click=record_start)

    elif st.session_state.state == "record":

        st.write(f"登校：{st.session_state.start_time}")
        print(st.session_state.start_time)
        st.text_area("研究内容", key='report', placeholder="研究内容を入力してください")
        st.button("帰宅する", on_click=record_report)

    elif st.session_state.state == "end":
        st.write(f"登校：{st.session_state.start_time}")
        st.write(f"帰宅：{st.session_state.end_time}")
        st.write("今日の研究内容")
        with open("log/state.txt", "r") as f:
            line = f.readline()
            st.write(line.split(" ")[3].strip())
    

if __name__ == "__main__":
    check_log()
    st.title("研究記録アプリ")
    main()

