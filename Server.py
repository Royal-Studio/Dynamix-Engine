from flask import Flask, request, render_template, redirect
from json import loads, dumps
from static.lib.compiler import Compile
import yaml
import os

app = Flask(__name__)
cur_dir = os.getcwd()
project_dir = os.path.join(cur_dir, "static")
project_dir = os.path.join(project_dir, "projects")
names_data_path = os.path.join(project_dir, "name.data")

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/save", methods=["POST"])
def save():
    data = request.form["config"]
    config = yaml.load(data)

    with open(names_data_path, "r") as f:
        names_data = f.read()
        names_data = loads(names_data)
    
    final = {
        "config": request.form["config"],
        "preload": request.form["preload"],
        "create": request.form["create"],
        "update": request.form["update"]
    }

    names_data[config["name"]] = final
    
    with open(names_data_path, "w") as f:
        f.write(dumps(names_data))

    return redirect("/")

@app.route("/load", methods=["POST"])
def load():

    name = request.form["name"]

    with open(names_data_path, "r") as f:
        names_data = f.read()
        names_data = loads(names_data)
    
    try:
        data = names_data[name]
        return dumps(data)
    except Exception as e:
        print(e)
        return "<script>alert('{} DOES NOT EXIST YET!')</script>".format(name)

@app.route("/run", methods=["POST"])
def run():

    config = request.form["config"]
    config = yaml.load(config)

    with open(names_data_path, "r") as f:
        names_data = f.read()
        names_data = loads(names_data)
    
    data = names_data[config["name"]]
    
    c = Compile(config, data['preload'], data['create'], data['update'])
    c = c.compile()

    name = os.path.join(project_dir, str(config["name"] + ".html"))

    with open(name, "w") as f:
        f.write(c)

    return "SUCCESS"

if __name__ == "__main__":
    app.run(debug=True)