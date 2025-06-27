from typing import Any, Dict, List

import streamlit as st

from ai_chatbot.assistant import Assistant, LLMModel


class AssistantGUI:
    """Class to handle the GUI for the AI Assistant."""

    def __init__(self, assistant: Assistant):
        """Initialize the GUI with the given assistant."""
        self.assistant = assistant
        self.messages = assistant.messages
        self.system_prompt = assistant.system_prompt

    def get_response(self, user_input: str) -> Any:
        """Get the response from the assistant based on user input."""
        return self.assistant.get_response(user_input)

    def set_state(self, key: str, value: str | List[Dict[str, str]]) -> None:
        """Set the state of the session."""
        st.session_state[key] = value

    def render_messages(self):
        """Render the chat messages in the Streamlit App."""
        options: Dict[str, str] = {
            "user": "human",
            "ai": "assistant",
            "assistant": "assistant",
            "system": "system",
        }

        for message in self.messages:
            if message["role"] in options:
                st.chat_message(options[message["role"]]).markdown(message["content"])
            else:
                st.error(f"Unknown role: {message['role']}")

    def render_user_input(self):
        """Render the user input field in the Streamlit App."""
        user_input = st.chat_input("Type your message here:...", key="input")

        if user_input and user_input != "":
            st.chat_message("human").markdown(user_input)

            response = self.get_response(user_input)  # type: ignore[no-any-return]
            st.write(response)

            self.messages.append({"role": "user", "content": user_input})
            self.messages.append({"role": "assistant", "content": response})

            self.set_state("messages", self.messages)

    def render(self):
        """Render the entire GUI."""
        with st.sidebar:
            st.logo(
                "https://upload.wikimedia.org/wikipedia/commons/0/0c/Chatbot_img.png"
            )
            st.title("AI Assistant")

            model_options = list(LLMModel)

            st.subheader("Model to use")
            st.selectbox(
                "Select AI Model from the list",
                options=model_options,
                key="model_selected",
                format_func=lambda x: x.value,  # type: ignore[arg-type]
            )

            model = st.session_state.model_selected
            self.set_state("model", model)  # type: ignore[arg-type]

            st.subheader("System Prompt")
            if "system_prompt" not in st.session_state:
                st.session_state.system_prompt = self.system_prompt.strip()

            self.set_state("system_prompt", self.system_prompt.strip())  # type: ignore[arg-type]

            st.text_area(
                "System Prompt",
                value=st.session_state.system_prompt,
                key="system_prompt",
            )

            st.subheader("Temperature")
            if "temperature" not in st.session_state:
                st.session_state.temperature = self.assistant.temperature

            self.set_state("temperature", self.assistant.temperature)  # type: ignore[arg-type]
            st.slider(
                "Temperature",
                min_value=0.0,
                max_value=1.0,
                value=self.assistant.temperature,
                key="temperature",
            )

        self.render_messages()
        self.render_user_input()
