import requests
import endpoints

def get_function():
    response = requests.get(endpoints.drivers)
    if response.status_code == 200:
        data = response.json()
        print(f'success, You get data from {endpoints.drivers}')
    else:
        print(f'Status code fail with: {response.status_code}')



