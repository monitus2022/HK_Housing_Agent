import streamlit as st

class Chatbox:
    def __init__(self):
        self._init_session()

    def _init_session(self):
        if "messages" not in st.session_state:
            st.session_state.messages = [
                {"role": "assistant", "content": "Hi there! Ask me anything about rent, estates, or housing trends."}
            ]

    def render_chat_history(self):
        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).markdown(msg["content"])

    def get_user_input(self):
        user_input = st.chat_input("Type your question here...")
        if user_input:
            st.chat_message("user").markdown(user_input)
            st.session_state.messages.append({"role": "user", "content": user_input})
            return user_input
        return None

    def generate_response(self, user_input):
        # response = openai.ChatCompletion.create(
        #     model="gpt-4",
        #     messages=st.session_state.messages
        # )
        # reply = response.choices[0].message["content"]
        reply = f"You were saying: {user_input}"  # Placeholder for bot response
        st.chat_message("assistant").markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})

    def run(self):
        self.render_chat_history()
        user_input = self.get_user_input()
        if user_input:
            self.generate_response(user_input)
            