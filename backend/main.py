from typing import List, Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Person(BaseModel):
    id: int
    name: str
    age: int


DB: List[Person] = [
    Person(id=1, name="Roman", age=34),
    Person(id=2, name="Hemdat", age=19),
    Person(id=3, name="Matan", age=13),
]


@app.get("/api")
def read_root():
    return DB


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
