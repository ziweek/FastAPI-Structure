# from typing import List

# from fastapi import Depends, FastAPI, HTTPException
# from sqlalchemy.orm import Session

from fastapi import FastAPI

from routers import users, items
from models import models
from config.database import engine

from config.connection import SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(users.router)
app.include_router(items.router)
