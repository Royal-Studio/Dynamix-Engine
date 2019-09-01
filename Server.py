from flask import Flask, request, render_template, redirect
from json import loads, dumps

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/test", methods=["GET", "POST"])
def test():
    j = {
        "Hello": "HOHO!"
    }
    return render_template("index.html", jn=j)

@app.route("/save", methods=["POST"])
def save():
    data = request.form["save"]
    data = data.replace("'", '"')
    data = loads(data)
    print(data["Hello"])

    return redirect("/test")

@app.route("/load", methods=["GET", "POST"])
def load():
    d = dumps({"lala": "koko"})
    print(d)
    return d

if __name__ == "__main__":
    app.run(debug=True)