import streamlit as st
from Pages import page1

st.set_page_config(
    page_title="BoardGameGeeks Dashboard",
    page_icon=":game_die:",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None,
)


no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)


def main():
    st.sidebar.title("Navigation")
    page_options = [
        "Home",
]
    selected_page = st.sidebar.radio("Select Page", page_options)

    if selected_page == "Home":
        page1.show()


if __name__ == "__main__":
    main()
