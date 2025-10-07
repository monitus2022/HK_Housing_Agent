import streamlit as st
from config.settings import settings

class Layout:
    def __init__(self):
        self.set_page_config()
        self.render_title()
        self.description()

    @staticmethod
    def set_page_config():
        st.set_page_config(page_title=settings.app_name, layout="wide")

    @staticmethod
    def render_title():
        st.title(f"🏠 {settings.app_name}")
    
    @staticmethod
    def description():
        st.markdown(
            """
            This chatbot can help you with information about rent, estates, and housing trends in Hong Kong.
            Ask me anything!
            """
        )
        