import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.view.view import coin_view
from starlette.staticfiles import StaticFiles
app = FastAPI()

app.include_router(coin_view)
app.mount("/static", StaticFiles(directory="src/static"), name="static")

if __name__ == '__main__':
    uvicorn.run(app, port=4000, debug=True)

