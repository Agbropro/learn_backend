import sys
import os

from fastapi import FastAPI
from db_structure import Base, engine
from ..internal.delivery.routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="MY AI SERVER")
app.include_router(router)