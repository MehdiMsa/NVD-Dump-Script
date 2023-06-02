import argparse
import requests
import json

API_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"
OUTPUT_FILE = "NVD_Data.json"


def get_cve_data(cpe_name):
    url = f"{API_URL}?cpeName={cpe_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Failed to retrieve CVE data")
        return None


def dump_nvd_data(api_key, cpe_name=None):
    if cpe_name:
        cve_data = get_cve_data(cpe_name)
        if cve_data:
            with open("cve_data.json", "w") as json_file:
                json.dump(cve_data, json_file, indent=4)

    headers = {"API_Key": api_key}
    response = requests.get(API_URL, headers=headers)

    if response.status_code == 200:
        data = response.json()
        with open(OUTPUT_FILE, "w") as file:
            json.dump(data, file, indent=4)
        print("Data dumped successfully to", OUTPUT_FILE)
    else:
        print("Failed to retrieve NVD data")


def main():
    parser = argparse.ArgumentParser(description="NVD Database Dump using API 2.0 & Python")
    parser.add_argument("-k", "--api-key", required=True, help="API Key for NVD API 2.0")
    parser.add_argument("-c", "--cpe-name", help="CPE name for filtering CVE data")
    args = parser.parse_args()

    dump_nvd_data(args.api_key, args.cpe_name)


if __name__ == "__main__":
    main()
