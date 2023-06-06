import requests
import json
import time
import datetime


def dump_nvd_database():

    base_url = 'https://services.nvd.nist.gov/rest/json/cves/2.0'

    result_per_page = 2000
    start_index = 0

    total_count = get_total_count(base_url)

    with open('nvd_database.json', 'a') as json_file:
        start_time = time.time()
        try:
            while start_index <= total_count:
                url = f'{base_url}?startIndex={start_index}&resultsPerPage={result_per_page}&'
                response = make_request(url)

                if response.status_code == 200:
                    json_data = response.json()
                    json.dump(json_data, json_file, indent=4)
                    json_file.write('\n')
                    print(f'Dumped {start_index} - {start_index + result_per_page - 1} records')

                start_index += result_per_page
                time.sleep(6)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred during the request: {e}")
        except json.JSONDecodeError as e:
            print(f"An error occurred while parsing the JSON response: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        end_time = time.time()
        duration = end_time - start_time
        print(f"Dumping the database took {duration:.2f} seconds")

def get_total_count(base_url):
    url = f'{base_url}?startIndex=0&resultsPerPage=1'
    response = make_request(url)
    if response.status_code == 200:
        json_data = response.json()
        print(json_data)
        print(datetime.datetime.now())
        return json_data['totalResults']

    return 0

def make_request(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'API-Key': '17c94377-b9f3-4d36-add6-fe2fe31e6ec3'
    }
    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    dump_nvd_database()
