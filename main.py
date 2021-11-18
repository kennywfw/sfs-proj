from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

db = []

class Company(BaseModel):
    name: str
    category: str
    year_founded: int

@app.get('/')
def index():
    return{'key' : 'value'}

@app.get('/companies')
def get_companies():
    return db

@app.get('/companies/{company_id}')
def get_companies(city_id: int):
    return db[city_id-1]

@app.post('/companies')
def create_company(company: Company):
    db.append(company.dict())
    return db[-1]

@app.delete('/companies/{city_id}')
def delete_city(city_id: int):
    db.pop(city_id-1)
    return {}
