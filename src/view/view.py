import requests
from fastapi import APIRouter, Request, Form
from fastapi.encoders import jsonable_encoder

from src.model.coins_model import Coin

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

coin_view = APIRouter(prefix="/coins")
templates = Jinja2Templates(directory="src/templates/")


class CoinModel:
    def __init__(self, first_coin, second_coin) -> None:
        self.first_coin = first_coin
        self.second_coin = second_coin


# async def post_basic_form(request: Request, username: str = Form(...), password: str = Form(...),
#                           file: UploadFile = File(...)):
#     print(f'username: {username}')
#     print(f'password: {password}')
#     content = await file.read()
#     print(content)
#     return templates.TemplateResponse("basicform.html", {"request": request})


@coin_view.post(f"/coin_comparator")
async def root(request: Request, coins_one: str = Form(...), coins_two: str = Form(...)):
    print(coins_one)
    print(coins_two)

    # form_data = coins_one
    # print(form_data)
    # form_conv = jsonable_encoder(form_data)
    # print('**************')
    # print(form_conv)
    # if Request.method == 'POST':
    # formContato = CoinModel(
    #     Request.form()
    #     Request.form['first_coin'],
    #     Request.form['second_coin'],
    #     )
    #     # print(coins_values)
    # # response = requests.get(f"{coins_values.coin_url_campare_two_coins}{coins_values.coin_one}-{coins_values.coin_two}")
# return response.text


@coin_view.get("/")
async def home(request: Request):
    return templates.TemplateResponse("coin_comparator.html", {"request": request})
