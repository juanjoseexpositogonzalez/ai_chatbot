from typing import Dict, Tuple

import streamlit as st
import streamlit_authenticator as stauth


def init_authenticator(config: Dict[str, str]) -> stauth.Authenticate:
    """Initializes the Streamlit Authenticator object from the config."""
    authenticator = stauth.Authenticate(
        credentials=config["credentials"],  # type: ignore[no-any-return]
        cookie_name=config["cookie"]["name"],  # type: ignore[no-any-return]
        cookie_key=config["cookie"]["key"],  # type: ignore[no-any-return]
        cookie_expiry_days=config["cookie"]["expiry_days"],  # type: ignore[no-any-return]
    )
    return authenticator


def run_auth_and_get_user(
    authenticator: stauth.Authenticate,
) -> Tuple[bool, str | None]:
    """Handles the login and returns the status and username if authenticated."""
    try:
        authenticator.login()
        auth_status = st.session_state.get("authentication_status")
        name = st.session_state.get("name")
        username = st.session_state.get("username")

        if auth_status:
            st.success(f"Welcome {name} 👋")
            return True, username
        elif auth_status is False:
            st.error("Invalid username or password")
        else:
            st.warning("Please enter your credentials")
    except (KeyError, ValueError) as e:
        st.error(f"An error occurred during authentication: {e}")

    return False, None
