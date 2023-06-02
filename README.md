# NVD Database Dump using API 2.0 & Python

This project allows you to retrieve and dump the National Vulnerability Database (NVD) using the NVD API 2.0 and Python.

## Features

- Retrieves NVD data using the API 2.0
- Supports filtering by Common Platform Enumeration (CPE) name
- Dumps the data into a JSON file
- Error handling for API requests and exceptions

## Prerequisites

- Python 3.x
- Requests library: `pip install requests`

## How to Use

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/nvd-database-dump.git

2.Install the dependencies

    pip install -r requirements.txt

3.Open dump_nvd.py and modify the following variables according to your needs:
  
    API_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    API_KEY = "YOUR_API_KEY"
    OUTPUT_FILE = "NVD_Data.json"

4.Run the Script:

    python dump_nvd.py

5.NVD will be dumped in two specified JSON output


