from fastapi import FastAPI
from volcan.presentation.api import router

app = FastAPI()
app.include_router(router)