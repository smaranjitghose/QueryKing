"""
Feedback Page using formsubmit.co API
"""
import streamlit as st
from utils import *
from PIL import Image
from streamlit_card import card




st.set_page_config(
        page_title="QueryKing | Feedback",
        # page_icon="./assets/favicon.png",
        layout= "centered",
        initial_sidebar_state="expanded",
        menu_items={
        'Get Help': 'https://github.com/smaranjitghose/QueryKing',
        'Report a bug': "https://github.com/smaranjitghose/QueryKing/issues",
        'About': "## A minimalistic application to generate SQL queries using Generative AI built with Python and Streamlit"
        } )


st.title("🤝🏽 Get in Touch")

hide_footer()
hide_hamburger_menu()

hasClicked = card(
        title="Smaranjit Ghose",
        text="Chief Developer",
        image="https://avatars.githubusercontent.com/u/46641503?v=4",
        url="https://github.com/smaranjitghose"
        )
        

st.write("### Want to Sponsor Me?")

st.write("[![Ko-Fi](https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/smaranjitghose)")

