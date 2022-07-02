import requests


def validator_sames_coin(coin_one, coin_two):
    if coin_one == coin_two and coin_one != "USD":
        coin_one = "USD"
    else:
        coin_one = "BRL"
    return coin_one, coin_two


def verify_different_coin(coin_one: str, coin_two: str):
    if coin_one == coin_two:
        return validator_sames_coin(coin_one, coin_two)
    return (coin_one, coin_two)


def get_coins(coin_one, coin_two):
    coins = verify_different_coin(coin_one, coin_two)
    response = requests.get(f'https://economia.awesomeapi.com.br/last/{coins[0]}-{coins[1]}')
    other_response = requests.get(f'https://economia.awesomeapi.com.br/last/{coins[1]}-{coins[0]}')
    other_response = other_response.json()
    response = response.json()
    for i in response.values():
        data = dict()
        data['ask'] = i.get('ask')
        name = i.get('name').split('/')
        data['current_name'] = name[0]
        data['compare_name'] = name[1]
        data['high'] = i.get('high')
        data['low'] = i.get('low')
    print(data)
    for i in other_response.values():
        other_data = dict()
        other_data['ask'] = i.get('ask')
        name = i.get('name').split('/')
        other_data['current_name'] = name[0]
        other_data['compare_name'] = name[1]
        other_data['high'] = i.get('high')
        other_data['low'] = i.get('low')
    print(other_data)
    return data, other_data
