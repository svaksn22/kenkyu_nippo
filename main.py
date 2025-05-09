import streamlit as st

def main():

    home = st.Page(page="pages/home.py", title="ホーム", icon=":material/home:", default=True)
    log = st.Page(page="pages/log.py", title="ログ", icon=":material/apps:")

    pg = st.navigation([home, log])
    pg.run()

if __name__ == "__main__":
    main()