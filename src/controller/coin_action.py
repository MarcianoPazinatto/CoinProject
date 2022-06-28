import requests


def get_coins(coin_one, coin_two):
    response = requests.get(f'https://economia.awesomeapi.com.br/last/{coin_one}-{coin_two}')
    response = response.json()
    for i in response.values():
        data = dict()
        data['ask'] = i.get('ask')
        data['name'] = i.get('name')
        data['high'] = i.get('high')
        data['low'] = i.get('low')
    print(data)
    return data
