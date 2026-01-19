
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import BorrowCreate
from app import crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def borrow(data: BorrowCreate, db: Session = Depends(get_db)):
    try:
        return crud.borrow_book(db, data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
