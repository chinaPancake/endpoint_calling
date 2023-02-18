import requests
import endpoints

def get_pet(id:str):
    url = (f'{endpoints.drivers}{id}')
    response = requests.get(url = url)
    if response.status_code == 200:
        data = response.json()
        print(f'success, You get data from {endpoints.drivers}')
        print(data)
    else:
        print(f'Status code fail with: {response.status_code}')

get_pet(id='1')

