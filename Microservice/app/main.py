from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

fake_movie_db = [
    {
        'name':'Terminator',
        'genre':['Action','Adventure'],
        'casts':['Arnold S', 'Mike', 'Resfod']
    }
]

class Movie(BaseModel):
    name:str
    genre:List[str]
    casts:List[str]

@app.get('/', response_model=List[Movie])
async def index():
    return fake_movie_db
    # return {"Real":"Python"}

@app.get('/1')
async def index():
    return {"Real":"Python"}

@app.post('/', status_code=201)
async def add_movie(payload: Movie):
    movie = payload.dict()
    fake_movie_db.append(movie)
    return {'id': len(fake_movie_db) - 1}