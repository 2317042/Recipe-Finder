# backend.py
from fastapi import FastAPI
import requests
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Recipe Finder Backend is running!"}

@app.get("/search")
def search_recipes(query: str):
    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={query}"
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    uvicorn.run("backend:app", host="127.0.0.1", port=8000, reload=True)
