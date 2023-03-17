"""
Feedback Page using formsubmit.co API
"""
import streamlit as st
from utils import *


st.set_page_config(
        page_title="QueryKing | Contact",
        # page_icon="./assets/favicon.png",
        layout= "centered",
        initial_sidebar_state="expanded",
        menu_items={
        'Get Help': 'https://github.com/smaranjitghose/QueryKing',
        'Report a bug': "https://github.com/smaranjitghose/QueryKing/issues",
        'About': "## A minimalistic application to generate SQL queries using Generative AI built with Python and Streamlit"
        } )


st.title(":mailbox: How was your experience?")
hide_footer()
hide_hamburger_menu()
# Load Stylesheet(s) for relevant components
css_local("assets/styles/contact.css")
# Load and display animation
anim = lottie_local("assets/animations/contact.json")
st_lottie(anim,
            speed=1,
            reverse=False,
            loop=True,
            quality="medium", # low; medium ; high
            # renderer="svg", # canvas
            height=300,
            width=300,
            key=None,
            )
# HTML code for formsubmit contactform template
contact_form = """
            <form action="https://formsubmit.co/b2365a7af4d69269a92869bf9be52f1ba" method="POST">
            <input type="hidden" name="_captcha" value="true">
            <input type="hidden" name="_template" value="table">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here"></textarea>
            <button type="submit">Send</button>
            </form>
            """
st.markdown(contact_form,unsafe_allow_html=True)

