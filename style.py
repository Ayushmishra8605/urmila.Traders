import streamlit as st


def apply_custom_design():
    # Page Title aur Layout set karein
    st.set_page_config(page_title="Urmila Traders", layout="centered")

    # Streamlit ka header aur footer chhupane ke liye CSS
    hide_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """
    st.markdown(hide_style, unsafe_allow_html=True)


def show_sidebar_content(phone_number):
    # Sidebar mein logo (bina gol kiye)
    # Check karein ki GitHub par image ka sahi naam yahi hai
   # st.sidebar.image("urmila traders.png", width=200)

    # Clickable phone number (Blue link)

    st.sidebar.markdown(f"### Contact Us: [+{8756085720}](tel:{phone_number})")
