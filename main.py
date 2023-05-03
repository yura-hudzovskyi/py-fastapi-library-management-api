from datetime import date

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import crud
import schemas
from database import SessionLocal

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/authors", response_model=list[schemas.Author])
def get_authors(db: Session = Depends(get_db), skip: int = 0, limit: int = 5):
    return crud.get_authors(db=db, skip=skip, limit=limit)


@app.get("/authors/{author_id}", response_model=schemas.Author)
def get_author(author_id: int, db: Session = Depends(get_db)):
    return crud.get_author(db=db, author_id=author_id)


@app.post("/authors", response_model=schemas.AuthorCreate)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    return crud.create_author(db=db, author=author)


@app.put("/authors/update/{author_id}", response_model=schemas.Author)
def update_author(
    author_id: int,
    name: str = None,
    bio: str = None,
    db: Session = Depends(get_db),
):
    return crud.update_author(
        db=db,
        author_id=author_id,
        name=name,
        bio=bio,
    )


@app.delete("/authors/delete/{author_id}", response_model=schemas.Author)
def delete_author(author_id: int, db: Session = Depends(get_db)):
    return crud.delete_author(db=db, author_id=author_id)


@app.get("/books", response_model=list[schemas.Book])
def get_books(
    db: Session = Depends(get_db), skip: int = 0, limit: int = 5, author_id: int = None
):
    return crud.get_books(db=db, skip=skip, limit=limit, author_id=author_id)


@app.get("/books/{book_id}", response_model=schemas.Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    return crud.get_book(db=db, book_id=book_id)


@app.post("/books", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db=db, book=book)


@app.put("/books/update/{book_id}", response_model=schemas.Book)
def update_book(
    book_id: int,
    title: str = None,
    summary: str = None,
    publication_date: date = None,
    db: Session = Depends(get_db),
):
    return crud.update_book(
        db=db,
        book_id=book_id,
        title=title,
        summary=summary,
        publication_date=publication_date,
    )


@app.delete("/books/delete/{book_id}", response_model=schemas.Book)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    return crud.delete_book(db=db, book_id=book_id)
