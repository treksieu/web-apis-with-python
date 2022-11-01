# dictionary-api-python-flask/app.py
from flask import Flask, request, jsonify, render_template
from model.dbHandler import match_exact, match_like

app = Flask(__name__)


@app.get("/")
def index():
  response = {"usage":"/dict?=<word>"}
  return jsonify(response)


@app.get("/dict")

def dictionary():
    """
    DEFAULT ROUTE
    This method will
    1. Accept a word from the request
    2. Try to find an exact match, and return it if found
    3. If not found, find all approximate matches and return
    """
    word = request.args.get("word")
    if not word:
        return jsonify({"status":"error","data":"pls choose a word"})

    # Try to find an exact match

    definitions = match_exact(word)
    if definitions:
        return jsonify({"status":"success", "data":definitions})

    # Try to find an approximate match
    definitions = match_like(word)
    if definitions:
        return jsonify({"status":"partial","data":definitions})
    else:
        return jsonify({"status":"error","data":"word not found"})
    
if __name__ == "__main__":
    app.run()
