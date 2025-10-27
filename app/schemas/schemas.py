from pydantic import BaseModel, Field

class BookBase(BaseModel):
    title: str = Field(example="Clean Code")
    author: str = Field(example="Robert C. Martin")
    genre: str = Field(example="Programming")
    year: int = Field(ge=0, le=2100, example=2008)
    rating: float = Field(example=4.8)


class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: str
    author: str
    genre: str
    year: int
    rating: float

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True