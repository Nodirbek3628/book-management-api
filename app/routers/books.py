from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud
from app.schemas import schemas
from app.db.database import LocalSession

router = APIRouter(prefix="/books", tags=["Books"])

def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schemas.BookBase])
def read_books(db: Session = Depends(get_db)):
    books = crud.get_books(db)
    return books


@router.get("/{book_id}", response_model=schemas.BookBase)
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.post("/", response_model=schemas.BookBase)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)

@router.put("/{book_id}", response_model=schemas.BookBase)
def update_book(book_id: int, updated_book: schemas.BookCreate, db: Session = Depends(get_db)):
    book = crud.update_book(db, book_id, updated_book)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    success = crud.delete_book(db, book_id)
    if not success:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}