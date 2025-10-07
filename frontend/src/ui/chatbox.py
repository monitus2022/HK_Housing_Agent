import streamlit as st
from services.llm import LLMService
from logger import frontend_logger

class Chatbox:
    def __init__(self):
        self._init_session()
        self.llm_service = LLMService()
        frontend_logger.info("Chatbox initialized.")

    def _init_session(self):
        if "messages" not in st.session_state:
            st.session_state.messages = [
                {"role": "assistant", "content": "Hi there! Ask me anything about rent, estates, or housing trends."}
            ]

    def render_chat_history(self):
        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).markdown(msg["content"])

    def get_user_input(self) -> str:
        user_input = st.chat_input("Type your question here...")
        if user_input:
            st.chat_message("user").markdown(user_input)
            st.session_state.messages.append({"role": "user", "content": user_input})
            frontend_logger.info(f"User input received: {user_input}")
            return user_input
        frontend_logger.info("No user input received.")
        return None

    def generate_response(self, user_input):
        with st.spinner("Generating response..."):
            reply = self.llm_service.get_prompt_response(user_input)
        if reply:
            st.chat_message("assistant").markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
            frontend_logger.info(f"Assistant response: {reply}")
        else:
            error_msg = "Sorry, I couldn't process your request at the moment."
            st.chat_message("assistant").markdown(error_msg)
            st.session_state.messages.append({"role": "assistant", "content": error_msg})
            frontend_logger.error(f"Failed to generate response for user input: {user_input}")

    def run(self):
        self.render_chat_history()
        user_input = self.get_user_input()
        if user_input:
            self.generate_response(user_input)
            