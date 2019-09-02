from flask import Flask, request, render_template, redirect
from json import loads, dumps
import yaml
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/save", methods=["POST"])
def save():
    
    data = request.form["data"]
    data = yaml.load(data)

    return redirect("/")

@app.route("/load/<name>", methods=["GET"])
def load(name):
    d = dumps({"lala": "koko"})
    return d

if __name__ == "__main__":
    app.run(debug=True)