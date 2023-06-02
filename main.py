import requests
import json

API_URL = "https://services.nvd.nist.gov/rest/json/cves/1.0"
API_KEY = "17c94377-b9f3-4d36-add6-fe2fe31e6ec3"
OUTPUT_FILE = "NVD_Data.json"

params = {"startIndex": 0, "resultPerPage": 2000}


# this is an optional function that implements the cpeName parameter
"""
def get_cve_data(CPE_Name):
    b_url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    url = f"{b_url}?cpeName={CPE_Name}"
    response2 = requests.get(url)

    if response2.status_code == 200:
        data2 = response2.json()
        return data2
    else:
        print("Failed to retrieve CVE data")
        return None


cpe_name = "cpe:2.3:o:microsoft:windows_10:1607:*:*:*:*:*:*:*"
cve_data = get_cve_data(cpe_name)
"""
try:
    """
    cve_data:
       with open("cve_data.json", "w") as json_file:
           json.dump(cve_data, json_file, indent=4)
    """
    response = requests.get(API_URL, params=params, headers={"API_Key": API_KEY})

    response.raise_for_status()

    data = response.json()


    total_results=data["totalResults"]
    all_entries = []

    while len(all_entries) < total_results:
        for entry in data["result"]["CVE_Items"]:
            all_entries.append(entry)

            params["startIndex"] += params["resultPerPage"]

            response = requests.get(API_URL, params=params)
            """headers={"API_Key": API_KEY}"""
            response = requests.get(API_URL)
            print(response.text)

            data = response.json()

            try:
                data = response.json()

            except json.JSONDecodeError as e:
                print("Error decoding JSON response:", e)
                print("Response content:", response.content)

    with open("nvd_DB.json", "w") as file:
        json.dump(all_entries, file)

    print(f"Successfully dumped {total_results} entries to nvd_DB.json")


    with open(OUTPUT_FILE, "w") as file:
        json.dump(data, file, indent=4)

    print("Data dumped successfully to", OUTPUT_FILE)


except requests.exceptions.RequestException as e:
    print("An error occurred:", e)



'''

This option allows to create a CLI to accept parameters such as API key and optionally CPE name

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

'''