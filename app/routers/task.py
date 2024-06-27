from typing import List
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, utils, oauth2
from ..oauth2 import get_current_user
from ..models import Task
from ..schemas import TaskSchema, TaskBase, UserBase, UserOut
from ..database import get_db
from sqlalchemy.orm import Session




router = APIRouter(
    prefix="/task",
    tags=['Tasks']
)



@router.get("/", response_model=List[TaskSchema])
def read_task(db: Session = Depends(get_db)):# current_user : int = Depends( oauth2.get_current_user) # only login users
    
   tasks = db.query(models.Task).all()  #fillter(models.Task.id == current_user.id # current_user : int = Depends( oauth2.get_current_user) # get users tasks only...
   return tasks



@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.TaskSchema)
def create_task(task: schemas.TaskCreate,db: Session = Depends(get_db), current_user : int = Depends( oauth2.get_current_user)):
    

    new_task = models.Task(owner_id=current_user.id,** task.dict())
    db.add(new_task)

    db.commit()
    db.refresh(new_task)
    

    return new_task





@router.get("/{id}", response_model=schemas.TaskSchema)
def read_task(id: int, db: Session = Depends(get_db), current_user : int = Depends( oauth2.get_current_user)):
    get_task = db.query(Task).filter(Task.id == id).first()
    if not get_task:
        raise HTTPException(status_code=404, detail=f"Task {id} not found")
    return get_task


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id: int,db: Session = Depends(get_db), current_user : int = Depends( oauth2.get_current_user)):
    

    task = db.query(models.Task).filter(models.Task.id == id )

    if task.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"Task {id} doesn't exist")
    
    task.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}",response_model=TaskSchema)
def update_task(id: int, task: schemas.TaskCreate, db: Session = Depends(get_db),current_user : int = Depends( oauth2.get_current_user)):
    
    task_query = db.query(models.Task).filter(models.Task.id == id)
    task_db = task_query.first()


    if task_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"Task {id} doesn't exist")
    
    task_data = task.dict()
    
    task_query.update(task_data,synchronize_session=False)
    db.commit()
    db.refresh(task_db)

    return task_db