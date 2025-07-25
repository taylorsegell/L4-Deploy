import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# --- Core CPD Configuration ---
CPD_CLUSTER_HOST = os.getenv("CPD_CLUSTER_HOST")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
PROJECT_ID = os.getenv("PROJECT_ID")
CATALOG_NAME = os.getenv("CATALOG_NAME")

if not all([CPD_CLUSTER_HOST, USERNAME, PASSWORD, PROJECT_ID, CATALOG_NAME]):
    raise EnvironmentError(
        "One or more required environment variables are not set. "
        "Please check your .env file."
    )

BASE_URL = f"https://{CPD_CLUSTER_HOST}"

# --- API Endpoints ---
AUTHORIZE_URL = f"{BASE_URL}/icp4d-api/v1/authorize"
CATALOGS_URL = f"{BASE_URL}/v2/catalogs"
CONNECTIONS_URL = f"{BASE_URL}/v2/connections"
GOVERNANCE_IMPORT_URL = f"{BASE_URL}/v3/governance_artifact_types/import"
CATEGORIES_SEARCH_URL = f"{BASE_URL}/v3/search?query=metadata.artifact_type:category"

# --- Data Source Details (Example for DB2) ---
DB2_NAME = "Data Warehouse"
DB2_DATASOURCE_TYPE = os.getenv("DB2_DATASOURCE_TYPE")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = "50001"
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
