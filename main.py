import requests
import json

API_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"
API_KEY = "17c94377-b9f3-4d36-add6-fe2fe31e6ec3"
OUTPUT_FILE = "NVD_Data.json"

'''
#this is an optional function that implements the cpeName parameter

def get_cve_data(cpe_name):
    b_url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    url = f"{b_url}?cpeName={cpe_name}"
    response2 = requests.get(url)

    if response2.status_code == 200:
        data2 = response2.json()
        return data2
    else:
        print("Failed to retrieve CVE data")
        return None; 
'''

try:
    response = requests.get(API_URL, headers={"API_Key": API_KEY})

    response.raise_for_status()

    data = response.json()

    with open(OUTPUT_FILE, "w") as file:
        json.dump(data, file, indent=4)

    print("Data dumped successfully to", OUTPUT_FILE)


except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
