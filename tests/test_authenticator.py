from typing import Any, Dict

import pytest
import streamlit_authenticator as stauth

from src.ai_chatbot.auth.authenticator import init_authenticator, run_auth_and_get_user


@pytest.fixture
def mock_config() -> Dict[str, Any]:
    return {
        "credentials": {
            "usernames": {
                "juanjo": {
                    "name": "Juanjo",
                    "email": "jjeg1979@gmail.com",
                    "password": "$2b$12$IpKadAkI...",  # hash generado
                }
            }
        },
        "cookie": {"name": "test_auth", "key": "testing123", "expiry_days": 1},
    }


def test_init_authenticator(mock_config: Dict[str, Any]):
    auth = init_authenticator(mock_config)
    assert isinstance(auth, stauth.Authenticate)


def test_run_auth_and_get_user_returns_false_when_not_logged_in(
    mock_config: Dict[str, Any],
):
    auth = init_authenticator(mock_config)
    # No se llama a .login() intencionalmente
    authenticated, user = run_auth_and_get_user(auth)
    assert not authenticated
    assert user is None
