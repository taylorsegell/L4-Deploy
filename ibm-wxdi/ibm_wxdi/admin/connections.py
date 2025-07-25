import logging
from .. import config
from ..utils.api_client import ApiClient
from ..utils.exceptions import APIError

logger = logging.getLogger(__name__)


def define_db2_connection(api: ApiClient, project_id: str) -> str:
    """
    Defines a connection to a DB2 Warehouse within a project.

    Args:
        api: An authenticated ApiClient instance.
        project_id: The ID of the project to add the connection to.

    Returns:
        The asset ID of the newly created connection.
    """
    payload = {
        "datasource_type": config.DB2_DATASOURCE_TYPE,
        "name": config.DB2_NAME,
        "properties": {
            "database": config.DB_DATABASE,
            "username": config.DB_USERNAME,
            "password": config.DB_PASSWORD,
            "host": config.DB_HOST,
            "port": config.DB_PORT,
            "ssl": "true",
        },
    }
    url = f"{config.CONNECTIONS_URL}?project_id={project_id}"

    logger.info(f"Defining connection for '{config.DB2_NAME}'...")
    response = api.post(url, json=payload)

    asset_id = response.get("metadata", {}).get("asset_id")
    if not asset_id:
        raise APIError(
            "Failed to get asset_id from define connection response.")

    logger.info(
        f"Successfully defined DB2 connection with Asset ID: {asset_id}")
    return asset_id
