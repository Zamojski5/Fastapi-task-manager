from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, utils
from ..models import  User
from ..schemas import UserBase, UserOut
from ..database import engine, get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/user",
    tags=['Users']
)


@router.post("/",response_model=schemas.Token)
def create_user(user: schemas.UserBase, db: Session = Depends(get_db)):
    
    hashed_password = utils.hash(user.password)
    user.password = hashed_password


    new_user = models.User(**user.dict())    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user


@router.get("/{id}", response_model=UserOut)
def read_user(id: int, db: Session = Depends(get_db)):
    get_user = db.query(models.User).filter(models.User.id == id).first()
    if not get_user:
        raise HTTPException(status_code=404, detail=f"User {id} doesnt exist")
    return get_user

@router.get("/", response_model=list[UserOut])
def read_user(db: Session = Depends(get_db)):
    user = db.query(models.User).all()


    return user
