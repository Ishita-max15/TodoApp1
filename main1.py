from fastapi import FastAPI
import models1
from database1 import engine
from router import auth, todos

app = FastAPI()

models1.Base.metadata.create_all(bind=engine)
app.include_router(auth.router)
app.include_router(todos.router)

