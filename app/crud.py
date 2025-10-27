from sqlalchemy.orm import Session
from app.models import books
from app.schemas import schemas

def create_book(db: Session, book: schemas.BookCreate):
    new_book = books.Book(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

def get_books(db: Session):
    return db.query(books.Book).all()

def get_book(db: Session, book_id: int):
    return db.query(books.Book).filter(books.Book.id == book_id).first()

def update_book(db: Session, book_id: int, updated_book: schemas.BookCreate):
    book = get_book(db, book_id)
    if book:
        for key, value in updated_book.dict().items():
            setattr(book, key, value)
        db.commit()
        db.refresh(book)
    return book

def delete_book(db: Session, book_id: int):
    book = get_book(db, book_id)
    if book:
        db.delete(book)
        db.commit()
        return True
    return False