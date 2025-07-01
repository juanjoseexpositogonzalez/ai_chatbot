import logging

import streamlit as st

from ai_chatbot.assistant import Assistant, LLMModel
from ai_chatbot.gui.gui import AssistantGUI
from ai_chatbot.prompts.prompts import SYSTEM_PROMPT, WELCOME_MESSAGE
from ai_chatbot.utils.utils import prepare_environment, return_provider_from_model


def main():
    """Main function to run the Streamlit app for the AI Assistant."""

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    # Prepare the environment for the AI model
    prepare_environment()

    if st.session_state.get("model_selected") is None:
        model = LLMModel.LLAMA_3_INSTANT
        st.session_state["model_selected"] = model

    if "temperature" not in st.session_state:
        st.session_state["temperature"] = 0.7

    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "ai", "content": WELCOME_MESSAGE}]

    assistant = Assistant(
        system_prompt=SYSTEM_PROMPT,
        llm_model=st.session_state["model_selected"],
        temperature=st.session_state.get("temperature", 0.7),
        max_tokens=None,
        llm_provider=return_provider_from_model,
        message_history=st.session_state.messages,
        tools=None,  # Tools can be added later if needed
    )

    gui = AssistantGUI(assistant)
    gui.render()
