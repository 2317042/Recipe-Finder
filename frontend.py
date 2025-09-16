# frontend.py
import tkinter as tk
from tkinter import messagebox
import requests

def search_recipe():
    query = entry.get()
    if not query:
        messagebox.showwarning("Input Error", "Please enter a recipe name")
        return
    
    try:
        response = requests.get(f"http://127.0.0.1:8000/search", params={"query": query})
        data = response.json()

        results.delete(1.0, tk.END)  # clear old text

        if not data or not data.get("meals"):
            results.insert(tk.END, "No recipes found.\n")
            return
        
        for meal in data["meals"]:
            results.insert(tk.END, f"🍽 {meal['strMeal']}\n")
            results.insert(tk.END, f"Category: {meal['strCategory']}\n")
            results.insert(tk.END, f"Area: {meal['strArea']}\n")
            results.insert(tk.END, f"Instructions: {meal['strInstructions'][:200]}...\n\n")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch recipes: {e}")

# GUI setup
root = tk.Tk()
root.title("Recipe Finder")
root.geometry("600x400")

label = tk.Label(root, text="Enter recipe name:")
label.pack()

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

search_btn = tk.Button(root, text="Search", command=search_recipe)
search_btn.pack(pady=5)

results = tk.Text(root, wrap=tk.WORD, height=15)
results.pack(pady=10)

root.mainloop()
