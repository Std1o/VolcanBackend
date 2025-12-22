from fastapi import FastAPI
from volcan.presentation.api import router

app = FastAPI(
    max_request_size=None
)
app.include_router(router)