from pydantic import BaseModel


class Coin(BaseModel):
    coin_one: str
    coin_two: str
    coin_url_campare_two_coins: str = "https://economia.awesomeapi.com.br/last/"
