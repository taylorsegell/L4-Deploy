from .. import config
from ..utils.api_client import ApiClient
from ..utils.exceptions import NotFoundError


def get_catalog_by_name(api: ApiClient, name: str) -> dict:
    """
    Finds a catalog's details by its name.

    Args:
        api: An authenticated ApiClient instance.
        name: The name of the catalog to find.

    Returns:
        A dictionary containing the catalog's metadata.

    Raises:
        NotFoundError: If no catalog with the given name is found.
    """
    catalogs_data = api.get(config.CATALOGS_URL)
    for catalog in catalogs_data.get("catalogs", []):
        if catalog.get("entity", {}).get("name") == name:
            return catalog
    raise NotFoundError(f"Catalog with name '{name}' not found.")
