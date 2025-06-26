from typing import Final

import streamlit as st

from src.ai_chatbot.chatbot import initialize_messages, interaction, show_messages

if __name__ == "__main__":
    st.set_page_config(page_title="AI Chatbot", page_icon=":robot_face:")
    AI_ROLE: Final[str] = "Sherlock Holmes"
    st.title("AI Chatbot")
    st.write("This is a simple AI chatbot interface using Streamlit.")
    initialize_messages(AI_ROLE)
    interaction()
    show_messages()
