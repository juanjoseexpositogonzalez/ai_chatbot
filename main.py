import streamlit as st

from src.ai_chatbot.chatbot import initialize_messages, interaction, show_messages


def main():
    st.write("AI Chatbot Interface")
    ai_role = "Sherlock Holmes"
    initialize_messages(ai_role)
    show_messages()
    interaction()


if __name__ == "__main__":
    main()
