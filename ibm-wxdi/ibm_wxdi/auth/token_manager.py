import requests
import urllib3
from .. import config
from ..utils.exceptions import AuthenticationError

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class TokenManager:
    """Handles the retrieval and management of authentication tokens."""

    def __init__(self):
        self._token = None

    def get_token(self) -> str:
        """
        Retrieves a bearer token. Fetches a new one if not already available.

        Returns:
            The bearer token string.

        Raises:
            AuthenticationError: If token retrieval fails.
        """
        if self._token:
            return self._token

        payload = {"username": config.USERNAME, "password": config.PASSWORD}
        headers = {"Content-Type": "application/json"}

        try:
            response = requests.post(
                config.AUTHORIZE_URL, json=payload, headers=headers, verify=False
            )
            response.raise_for_status()
            self._token = response.json().get("token")
            if not self._token:
                raise AuthenticationError(
                    "Token not found in authorization response.")
            return self._token
        except requests.RequestException as e:
            raise AuthenticationError(
                f"Failed to obtain bearer token: {e}") from e
