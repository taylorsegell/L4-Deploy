import requests
import logging
from .exceptions import APIError, NotFoundError

logger = logging.getLogger(__name__)


class ApiClient:
    """A client for making authenticated API calls."""

    def __init__(self, token: str):
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        })
        self.session.verify = False  # Disabling SSL verification as in original script

    def get(self, url: str, **kwargs):
        return self._request("GET", url, **kwargs)

    def post(self, url: str, **kwargs):
        return self._request("POST", url, **kwargs)

    def _request(self, method: str, url: str, **kwargs):
        """Internal request handler."""
        try:
            response = self.session.request(method, url, **kwargs)

            if response.status_code == 404:
                raise NotFoundError(f"Resource not found at {url}")

            response.raise_for_status()

            # Return JSON if possible, otherwise raw response
            try:
                return response.json()
            except requests.JSONDecodeError:
                return response

        except requests.HTTPError as e:
            logger.error(
                f"API Error: {e.response.status_code} - {e.response.text}")
            raise APIError(f"API call to {url} failed: {e}") from e
        except requests.RequestException as e:
            logger.error(f"Request Exception: {e}")
            raise APIError(f"Request to {url} failed: {e}") from e
