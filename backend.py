import subprocess
import webbrowser
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# Enable CORS so frontend can talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dummy recipe database
recipes_db = {
    "pasta": ["Creamy Alfredo", "Spaghetti Bolognese", "Pesto Pasta"],
    "chicken": ["Grilled Chicken", "Butter Chicken", "Chicken Curry"],
    "egg": ["Omelette", "Scrambled Eggs", "Egg Curry"]
}

@app.get("/recipes/{query}")
def get_recipes(query: str):
    query = query.lower()
    matches = [r for key, recs in recipes_db.items() if query in key for r in recs]
    return {"recipes": matches if matches else ["No recipes found"]}


if __name__ == "__main__":
    # Start frontend (Vite)
    subprocess.Popen(["npm", "run", "dev"], cwd="frontend")

    print("\n✅ Backend running at: http://127.0.0.1:8000")
    print("👉 Click this link to open frontend: http://localhost:5173\n")

    # Start backend
    uvicorn.run(app, host="127.0.0.1", port=8000)
