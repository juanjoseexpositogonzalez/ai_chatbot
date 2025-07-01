from typing import Final

import streamlit as st

from ai_chatbot.auth.authenticator import (
    init_authenticator,
    run_auth_and_get_user,
)
from ai_chatbot.auth.config_loader import load_config
from app import main


def run() -> None:
    config_file: Final[str] = "src/ai_chatbot/config/config.yaml"
    config = load_config(config_file)

    st.set_page_config(  # ✅ IMPORTANT! This should be the first thing!
        page_title="AI Assistant",
        page_icon=":robot:",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    authenticator = init_authenticator(config)

    authenticated, _ = run_auth_and_get_user(authenticator)

    if authenticated:
        authenticator.logout("Logout", "sidebar", key="logout_btn_main")
        main()


if __name__ == "__main__":
    run()
