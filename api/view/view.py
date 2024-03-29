import requests
from fastapi import APIRouter, Request, Form
from fastapi.encoders import jsonable_encoder
from api.controller.coin_action import get_coins
from api.model.coins_model import Coin

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

coin_view = APIRouter()
templates = Jinja2Templates(directory="api/templates/")


class CoinModel:
    def __init__(self, first_coin, second_coin) -> None:
        self.first_coin = first_coin
        self.second_coin = second_coin


@coin_view.post(f"/comparator")
async def root(request: Request, coins_one: str = Form(...), coins_two: str = Form(...)):

    response = get_coins(coins_one, coins_two)

    return templates.TemplateResponse("basicform.html", {"request": request,
                                                         "response": response[0],
                                                         "other_response": response[1]})


@coin_view.get("/")
async def home(request: Request):
    return templates.TemplateResponse("coin_comparator.html", {"request": request})


@coin_view.get("/")
async def home(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})
