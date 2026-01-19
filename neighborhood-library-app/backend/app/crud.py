
from sqlalchemy.orm import Session
from datetime import date
from app.models import Book, Member, Borrowing

def create_book(db: Session, book):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def create_member(db: Session, member):
    db_member = Member(**member.dict())
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member

def borrow_book(db: Session, data):
    active = db.query(Borrowing).filter(
        Borrowing.book_id == data.book_id,
        Borrowing.returned_at.is_(None)
    ).first()
    if active:
        raise ValueError("Book already checked out")

    borrow = Borrowing(
        book_id=data.book_id,
        member_id=data.member_id,
        borrowed_at=date.today()
    )
    db.add(borrow)
    db.commit()
    db.refresh(borrow)
    return borrow
