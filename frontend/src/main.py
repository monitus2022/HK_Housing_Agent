import streamlit as st
from ui.chatbox import Chatbox
from ui.layout import Layout

def main():
    layout = Layout()
    chatbox = Chatbox()
    chatbox.run()

if __name__ == "__main__":
    main()