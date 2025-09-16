from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

recipes = {
    "pasta": {"name": "Creamy Pasta", "ingredients": ["pasta", "cream", "cheese"]},
    "pizza": {"name": "Cheese Pizza", "ingredients": ["dough", "tomato", "cheese"]},
    "salad": {"name": "Green Salad", "ingredients": ["lettuce", "cucumber", "olive oil"]},
}

@app.get("/")
def root():
    return {"message": "Recipe Finder Backend is running!"}

@app.get("/search/{item}")
def search(item: str):
    return recipes.get(item.lower(), {"error": "Recipe not found"})
