import logging
from . import config
from .auth.token_manager import TokenManager
from .utils.api_client import ApiClient
from .utils.exceptions import InitializationError
from .admin import catalogs as catalog_admin
from .admin import connections as connection_admin
from .glossary import manage as glossary_manager
from .glossary import categories as category_glossary

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class IbmWxdiClient:
    """
    A client for interacting with the IBM Watsonx Data & AI Platform.
    """

    def __init__(self):
        logger.info("Initializing IBM WXDI Client...")
        try:
            self._token_manager = TokenManager()
            self.token = self._token_manager.get_token()
            self._api = ApiClient(self.token)

            self.project_id = config.PROJECT_ID
            catalog_info = catalog_admin.get_catalog_by_name(
                self._api, config.CATALOG_NAME)
            self.catalog_id = catalog_info["metadata"]["guid"]

            logger.info(
                f"Client initialized for Project '{self.project_id}' and Catalog '{config.CATALOG_NAME}' ({self.catalog_id})")

            self.admin = AdminModule(self)
            self.glossary = GlossaryModule(self)

        except Exception as e:
            raise InitializationError(
                f"Failed to initialize IbmWxdiClient: {e}") from e


class AdminModule:
    """Provides access to administrative functions."""

    def __init__(self, client: IbmWxdiClient):
        self._client = client

    @property
    def connections(self):
        return BoundAdminConnections(self._client)


class BoundAdminConnections:
    def __init__(self, client: IbmWxdiClient):
        self._client = client

    def define_db2(self):
        return connection_admin.define_db2_connection(self._client._api, self._client.project_id)


class GlossaryModule:
    """Provides access to glossary functions."""

    def __init__(self, client: IbmWxdiClient):
        self._client = client

    def import_from_zip(self, file_path: str):
        return glossary_manager.import_from_zip(self._client._api, file_path)

    def get_all_categories(self):
        return category_glossary.get_all_categories(self._client._api)
