from fastapi import FastAPI
from src.app.api.routes import router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:7567"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
