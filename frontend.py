from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head><title>Recipe Finder</title></head>
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

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route("/search")
def search():
    item = request.args.get("item")
    if not item:
        return render_template_string(HTML_TEMPLATE, result="Please enter a recipe")
    response = requests.get(f"http://127.0.0.1:8000/search/{item}")
    return render_template_string(HTML_TEMPLATE, result=response.json())

if __name__ == "__main__":
    app.run(port=5000)
