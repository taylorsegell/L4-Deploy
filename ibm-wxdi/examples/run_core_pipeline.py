import logging
from ibm_wxdi.client import IbmWxdiClient
from ibm_wxdi.utils.exceptions import IbmWxdiError

logger = logging.getLogger(__name__)


def main():
    """
    Executes a pipeline to define connections and import governance artifacts.
    """
    logger.info("--- Starting WXDI Core Pipeline ---")
    try:
        client = IbmWxdiClient()
        logger.info("\n--- Defining Data Connections ---")
        db2_connection_id = client.admin.connections.define_db2()
        logger.info(f"DB2 Connection created with ID: {db2_connection_id}")
        logger.info("\n--- Importing Governance Artifacts ---")
        client.glossary.import_from_zip("governance_artifacts.zip")
        logger.info("\n--- Fetching Glossary Categories ---")
        categories = client.glossary.get_all_categories()
        logger.info(f"Successfully fetched {len(categories)} categories.")
        logger.info("\n--- WXDI Core Pipeline Finished Successfully ---")
    except IbmWxdiError as e:
        logger.error(f"A pipeline error occurred: {e}", exc_info=True)
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}", exc_info=True)


if __name__ == "__main__":
    main()
