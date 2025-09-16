from flask import Flask, render_template_string, request
import requests
from threading import Thread
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ---------- Backend (FastAPI) ----------
backend = FastAPI()

backend.add_middleware(
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

@backend.get("/search/{item}")
def search_recipe(item: str):
    return recipes.get(item.lower(), {"error": "Recipe not found"})


# ---------- Frontend (Flask) ----------
frontend = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Recipe Finder</title>
</head>
<body>
    <h2>Recipe Finder</h2>
    <form method="get" action="/search">
        <input type="text" name="item" placeholder="Enter recipe">
        <button type="submit">Search</button>
    </form>

    {% if result %}
        <h3>Result:</h3>
        <pre>{{ result }}</pre>
    {% endif %}
</body>
</html>
"""

@frontend.route("/")
def home():
    return render_template_string(HTML_TEMPLATE)

@frontend.route("/search")
def search():
    item = request.args.get("item")
    if not item:
        return render_template_string(HTML_TEMPLATE, result="Please enter a recipe")
    response = requests.get(f"http://127.0.0.1:8000/search/{item}")
    return render_template_string(HTML_TEMPLATE, result=response.json())


# ---------- Run Both ----------
def run_backend():
    uvicorn.run(backend, host="127.0.0.1", port=8000)

if __name__ == "__main__":
    Thread(target=run_backend, daemon=True).start()
    frontend.run(port=5000)
