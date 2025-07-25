import time
import logging
from datetime import datetime, timedelta
from .. import config
from ..utils.api_client import ApiClient
from ..utils.exceptions import APIError

logger = logging.getLogger(__name__)


def import_from_zip(api: ApiClient, zip_file_path: str):
    """
    Imports governance artifacts from a ZIP file and monitors the progress.

    Args:
        api: An authenticated ApiClient instance.
        zip_file_path: The local path to the .zip file.
    """
    headers = {"Authorization": api.session.headers["Authorization"]}

    with open(zip_file_path, 'rb') as f:
        files = {'file': (zip_file_path, f, 'application/zip')}
        params = {'merge_option': 'specified'}

        response = api.post(
            config.GOVERNANCE_IMPORT_URL, headers=headers, files=files, params=params
        )

    if response.status_code == 202:
        process_id = response.json().get("process_id")
        logger.info(
            f"Governance artifact import started. Process ID: {process_id}")
        _monitor_import_status(api, process_id)
    else:
        logger.info("Governance artifacts imported synchronously.")


def _monitor_import_status(api: ApiClient, process_id: str):
    status_url = f"{config.GOVERNANCE_IMPORT_URL}/status/{process_id}"
    start_time = datetime.now()

    while True:
        status_data = api.get(status_url)
        status = status_data.get("status")
        step = status_data.get("step_number", 0)
        total = status_data.get("total_steps", 1)

        elapsed = str(timedelta(seconds=(datetime.now() - start_time).seconds))
        progress = (step / total) * 100 if total > 0 else 0
        logger.info(
            f"Import progress: {progress:.2f}% complete. Elapsed: {elapsed}")

        if status == "SUCCEEDED":
            logger.info(
                "✅✅✅ Governance artifacts import completed successfully. ✅✅✅")
            break
        if status == "FAILED":
            raise APIError(
                f"Import process {process_id} failed: {status_data}")

        time.sleep(30)
