from datetime import datetime

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
    return coin_one, coin_two


def get_coins(coin_one, coin_two):
    coins = verify_different_coin(coin_one, coin_two)
    response = requests.get(f'https://economia.awesomeapi.com.br/last/{coins[0]}-{coins[1]}')
    other_response = requests.get(f'https://economia.awesomeapi.com.br/last/{coins[1]}-{coins[0]}')
    other_response = other_response.json()
    response = response.json()

    today = datetime.today().strftime('%d/%m/%Y')
    response_adjusted, other_response_adjusted = adjust_values_response(response, other_response, today)

    return response_adjusted, other_response_adjusted


def adjust_values_response(response, other_response, today):
    response_adjusted = creating_dict(response, today)
    other_response_adjusted = creating_dict(other_response, today)
    return response_adjusted, other_response_adjusted


def creating_dict(values, today):
    data = dict()
    if "status" in values:
        return generate_error()
    for i in values.values():
        data['date'] = today
        data['ask'] = f"{float(i.get('ask')):.2f}"
        name = i.get('name').split('/')
        data['current_name'] = name[0]
        data['compare_name'] = name[1]
        data['high'] = f"{float(i.get('high')):.2f}"
        data['low'] = f"{float(i.get('low')):.2f}"
    return data


def generate_error():
    data = dict()
    data['date'] = "-"
    data['ask'] = "-"
    name = ("-", "-")
    data['current_name'] = name[0]
    data['compare_name'] = name[1]
    data['high'] = "-"
    data['low'] = "-"
    return data
