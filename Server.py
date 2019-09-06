from flask import Flask, request, render_template, redirect, send_file
from json import loads, dumps
from static.lib.compiler import Compile
from static.lib.ELangJS import ELang
import shutil
import yaml
import os

app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
cur_dir = os.getcwd()
project_dir = os.path.join(cur_dir, "templates")
project_dir = os.path.join(project_dir, "projects")
names_data_path = os.path.join(project_dir, "name.data")
current_proj = os.path.join(cur_dir, "static")
current_proj = os.path.join(current_proj, "cur_proj.elham")

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
        "init": request.form["init"],
        "preload": request.form["preload"],
        "create": request.form["create"],
        "update": request.form["update"]
    }

    names_data[config["name"]] = final
    
    with open(names_data_path, "w") as f:
        f.write(dumps(names_data))
    
    with open(current_proj, "w") as f:
        f.write(str(config["name"]))

    return redirect("/")

@app.route("/load", methods=["POST"])
def load():

    name = request.form["name"]

    with open(names_data_path, "r") as f:
        names_data = f.read()
        names_data = loads(names_data)
    
    with open(current_proj, "w") as f:
        f.write(str(name))
    
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

    c = Compile(ELang, config['language'], config, data['init'], data['preload'], data['create'], data['update'])
    c = c.compile()

    name = os.path.join(project_dir, str(config["name"]))

    if os.path.isdir(name):
        pass
    else:
        os.mkdir(name)
    
    name = os.path.join(name, str(config["name"] + ".html"))

    with open(name, "w") as f:
        f.write(c)
    
    response = {
        "path": str("/" + config["name"]),
        "width": config["width"],
        "height": config["height"]
    }

    return dumps(response)

@app.route("/<name>.html", methods=["GET", "POST"])
def render_game(name):
    project_dir = os.path.join("projects", str(name))
    project_dir = os.path.join(project_dir, str(name + ".html"))

    return render_template(project_dir)

@app.route("/import", methods=["GET", "POST"])
def importer():

    with open(current_proj, "r") as f:
        name_of_proj = f.read()

    if request.method == "POST":
        path = os.path.join(os.getcwd(), "templates")
        path = os.path.join(path, "projects")
        path = os.path.join(path, name_of_proj)
        asset_path = os.path.join(path, "asset")
        if os.path.isdir(asset_path):
            f = request.files["file"]
            f.save(str(os.path.join(asset_path, f.filename)))
            return redirect("/")
        else:
            os.chdir(path)
            os.mkdir("asset")
            f = request.files["file"]
            f.save(str(os.path.join(asset_path, f.filename)))
            return redirect("/")

@app.route("/asset/<name>", methods=["GET", "POST"])
def test1(name):
    with open(current_proj, "r") as f:
        name_of_proj = f.read()
    
    project_dir = os.path.join(os.getcwd(), "templates")
    project_dir = os.path.join(project_dir, "projects")
    project_dir = os.path.join(project_dir, name_of_proj)
    project_dir = os.path.join(project_dir, "asset")
    project_dir = os.path.join(project_dir, name)

    return send_file(project_dir)

if __name__ == "__main__":
    app.run(debug=True)