import streamlit as st

from src.ai_chatbot.aimodel import generate_response


def initialize_messages(ai_role: str) -> None:
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "system", "content": f"You are a {ai_role}."}
        ]


def show_messages() -> None:
    """Displays the messages in the chat."""
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"**User:** {message['content']}")
        elif message["role"] == "assistant":
            st.markdown(f"**Assistant:** {message['content']}")


def interaction():
    """Defines the interaction with the user with streamlit."""
    st.title("AI Chatbot")
    st.write("This is a simple AI chatbot interface using Streamlit.")
    user_input = st.text_input("Type your message here:")
    if user_input and user_input != "":
        st.chat_message("user").markdown(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})
        response = generate_response(user_input)
        st.chat_message("assistant").markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
