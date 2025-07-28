from .. import config
from ..utils.api_client import ApiClient


def get_all_categories(api: ApiClient) -> list:
    """
    Retrieves all governance category artifacts.

    Args:
        api: An authenticated ApiClient instance.

    Returns:
        A list of category artifacts.
    """
    response = api.get(config.CATEGORIES_SEARCH_URL)
    return response.get("rows", [])
