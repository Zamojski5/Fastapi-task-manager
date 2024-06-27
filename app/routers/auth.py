from fastapi import APIRouter, Depends, status, HTTPException, requests
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import database, schemas, models, utils, oauth2





router = APIRouter(
    tags=['Authentication'],
    prefix="/login"
)


@router.post("/", response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm= Depends(), db: Session = Depends(database.get_db)):

    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"invalid Credentials"
            )
    
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,detail=f"invalid credentials"
        )
    
    #create token 
    access_token = oauth2.create_access_token(data={"user_id": str(user.id)})



    return {"access_token": access_token, "token_type":"bariera" }


# {
#     "email": "wp@wp.pl",
#     "password": "JebacPsy",
#     "beaier": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMiwiZXhwIjoxNzE5NDAyNzU0fQ.X6zzGI_QA2sBY6dpUHcT8TkyE9rCJZokboL8fOl2pG4"


# }