from fastapi import FastAPI
import models1
from database import engine
from router import auth, todos, admin, users

app = FastAPI()

models1.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)