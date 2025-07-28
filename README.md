# L4-Deploy

## Overview
L4-Deploy is a Python-based toolkit for automating API interactions and governance tasks with IBM Watson Data Integration (WXDI) and Cloud Pak for Data (CPD). It provides scripts, utilities, and examples for managing catalogs, connections, glossaries, and authentication workflows.

## Repository Structure

```
ibm-wxdi/
  examples/
    run_core_pipeline.py         # Example pipeline script
  ibm_wxdi/
    client.py                   # Main client for API interactions
    config.py                   # Configuration management
    admin/
      catalogs.py               # Catalog management
      connections.py            # Connection management
    auth/
      token_manager.py          # Authentication and token handling
    glossary/
      categories.py             # Glossary category management
      manage.py                 # Glossary management utilities
    utils/
      api_client.py             # API client utilities
      exceptions.py             # Custom exceptions
Lab/
  API Automation Lab.ipynb      # Jupyter notebook for API automation
  API Automation with CPD.ipynb # Jupyter notebook for CPD automation
  client.py                     # Lab client example
  governance_artifacts.zip      # Example governance artifacts
  import.py                     # Import script for artifacts
```

## Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Access to IBM Cloud Pak for Data or Watson Data Integration

### Installation
Clone the repository:

```bash
git clone https://github.com/taylorsegell/L4-Deploy.git
cd L4-Deploy
```

Install required Python packages (if requirements.txt is provided):

```bash
pip install -r requirements.txt
```

### Configuration
Edit `ibm-wxdi/ibm_wxdi/config.py` to set your API endpoints and credentials.

### Usage

- **Run Example Pipeline:**
  ```bash
  python ibm-wxdi/examples/run_core_pipeline.py
  ```
- **Interact with API:**
  Use `ibm_wxdi/client.py` to connect and perform operations.
- **Jupyter Notebooks:**
  Open notebooks in the `Lab/` folder for interactive automation and governance tasks.

## Features
- Catalog and connection management
- Authentication via token manager
- Glossary and category automation
- Example scripts and notebooks for rapid prototyping

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
MIT License

## Contact
For questions or support, contact [repo owner](https://github.com/taylorsegell).