from fastapi import FastAPI
from app.db.database import engine, Base
from .routers.books import router as books_router



Base.metadata.create_all(bind=engine)


app = FastAPI(title="Book Management API")
app.include_router(books_router)


@app.get("/", tags=["root"])
def root():
    return {"message": "Welcome to Book Management API"}