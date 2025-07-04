from fastapi import FastAPI
from src.app.api.routes import router

app = FastAPI()
app.include_router(router)
