from flask import Flask, request, render_template, redirect, send_file
from json import loads, dumps
from static.lib.compiler import Compile
from static.lib.ELangJS import ELang
from datetime import datetime
import logging
import shutil
import yaml
import os

app = Flask(__name__)
logging.basicConfig(filename="static/logfile.log", level=logging.INFO)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
cur_dir = os.getcwd()
project_dir = os.path.join(cur_dir, "templates")
project_dir = os.path.join(project_dir, "projects")
names_data_path = os.path.join(project_dir, "name.data")
current_proj = os.path.join(cur_dir, "static")
current_proj = os.path.join(current_proj, "cur_proj.elham")


def user_agent_log(req):
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr) 
    platform = request.user_agent.platform
    browser = request.user_agent.browser
    version = request.user_agent.version
    logging.info("\n\n\n{} ENTERED!\n\nBrowser: {} \nVersion: {} \nOS: {} \nRequested: {} \nTime: {}\n\n\n".format(
        ip, browser, version, platform, req, datetime.now()))


@app.route("/", methods=["GET", "POST"])
def index():
    user_agent_log("INDEX HAVE BEEN REQUESTED!")
    return render_template("index.html")

@app.route("/save", methods=["POST"])
def save():
    user_agent_log("DATA SAVED!")
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
    user_agent_log("DATA LOADED!")
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
    user_agent_log("REQUESTED TO BUILD AND RUN GAME")
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
    user_agent_log("{} GAME FILE REQUESTED!".format(name))
    project_dir = os.path.join("projects", str(name))
    project_dir = os.path.join(project_dir, str(name + ".html"))

    return render_template(project_dir)

@app.route("/import", methods=["GET", "POST"])
def importer():
    user_agent_log("ASSET IMPORTED!")
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
    user_agent_log("ASSET REQUESTED!")
    with open(current_proj, "r") as f:
        name_of_proj = f.read()
    
    project_dir = os.path.join(os.getcwd(), "templates")
    project_dir = os.path.join(project_dir, "projects")
    project_dir = os.path.join(project_dir, name_of_proj)
    project_dir = os.path.join(project_dir, "asset")
    project_dir = os.path.join(project_dir, name)

    return send_file(project_dir)

@app.route('/export', methods=["POST"])
def export():
    user_agent_log("GAME EXPORT REQUESTED!")
    with open(current_proj, "r") as f:
        name = f.read()
    
    with open(names_data_path, "r") as f:
        data = f.read()
        data = loads(data)
    
    project_dir = os.path.join(os.getcwd(), "templates")
    project_dir = os.path.join(project_dir, "projects")
    project_dir_main = os.path.join(project_dir, name)
    project_dir = os.path.join(project_dir_main, "asset")
    
    try:
        data = data[name]
    except Exception as e:
        print(e)
        print("\n\nPROJECT MAY NOT EXIST! TRY SAVING!")
        return redirect('/')

    path_to_export = request.form["export-name"]

    if os.path.isdir(path_to_export):
        pass
    else:
        print("\nPATH {} DOES NOT EXIST".format(path_to_export))
        return redirect('/')

    asset_path = os.path.join(path_to_export, "asset")

    try:
        os.mkdir(asset_path)
    except Exception as e:
        print(e)

    asset_datas = os.listdir(project_dir)
    asset_data_get = []

    for i in asset_datas:
        asset_to_read = os.path.join(project_dir, i)
        with open(asset_to_read, "rb") as f:
            asset_data_get.append([i, f.read()])

    for i in asset_data_get:
        path_to_save = os.path.join(asset_path, i[0])
        with open(path_to_save, "wb") as f:
            f.write(i[1])
    
    template_path = os.path.join(path_to_export, "templates")
    if os.path.isdir(template_path):
        pass
    else:
        os.mkdir(template_path)
    
    game = os.path.join(project_dir_main, str(name + ".html"))
    if os.path.isfile(game):
        with open(game, "rb") as f:
            game_data = f.read()
    else:
        print("PLEASE RUN THE GAME TO BE ABLE TO EXPORT!")
        return redirect("/")
    
    game_export = os.path.join(template_path, "index.html")
    with open(game_export, "wb") as f:
        f.write(game_data)
    
    server = """from flask import Flask, send_file, render_template
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/asset/<name>", methods=["GET", "POST"])
def test1(name):    
    project_dir = os.path.join(os.getcwd(), "asset")
    project_dir = os.path.join(project_dir, name)

    return send_file(project_dir)

if __name__ == "__main__":
    from random import randint
    PORT = randint(0, 10000)
    app.run(host="0.0.0.0", port=PORT, debug=False)"""

    game_export = os.path.join(path_to_export, str(name + ".py"))
    with open(game_export, "w") as f:
        f.write(server)
    
    del game
    del game_export
    del data
    del path_to_export
    del path_to_save
    del asset_data_get
    del asset_datas
    del asset_path
    del asset_to_read
    del server
    del template_path
    del project_dir
    del project_dir_main

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)