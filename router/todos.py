
from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import APIRouter , Depends, HTTPException, Path
from starlette import status
from models1 import Todos
from database1 import SessionLocal


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency =  Annotated[Session,Depends(get_db)]

class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3,max_length=100)
    priority: int = Field(gt=0,lt=6)
    completed: bool
@router.get("/",status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency):
    return db.query(Todos).all()

@router.get("/todo/{todo_id}",status_code=status.HTTP_200_OK)
async def read_one( db: db_dependency,todo_id: int = Path(gt=0)):
    return db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model1 is not None:
        return todo_model1
    else:
        raise HTTPException(status_code=404, detail="Not found")




@router.post("/todo",status_code=status.HTTP_201_CREATED)
async def create_todo(db:db_dependency,todo_request: TodoRequest):
    todo_model1 = Todos(**todo_request.dict())

    db.add(todo_model1)
    db.commit()

@router.put("/todo/{todo_id}",status_code=status.HTTP_202_ACCEPTED)
async def update_todo(db: db_dependency,todo_id: int,todo_request: TodoRequest):
    todo_model1 =db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model1 is None:
        raise HTTPException(status_code=404, detail="Not found")
    todo_model1.title = todo_request.title
    todo_model1.description = todo_request.description
    todo_model1.priority = todo_request.priority
    todo_model1.completed = todo_request.completed
    db.add(todo_model1)
    db.commit()
