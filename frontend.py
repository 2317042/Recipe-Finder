import os
from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

HTML_TEMPLATE = """..."""  # keep as before

BACKEND_URL = os.environ.get("BACKEND_URL", "http://127.0.0.1:8000")

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route("/search")
def search():
    item = request.args.get("item")
    if not item:
        return render_template_string(HTML_TEMPLATE, result="Please enter a recipe")
    response = requests.get(f"{BACKEND_URL}/search/{item}")
    return render_template_string(HTML_TEMPLATE, result=response.json())

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")  # host=0.0.0.0 makes it accessible from outside
