from webview import create_window, start
from flask import Flask, request, render_template
from multiprocessing import Process
from os import kill
from signal import SIGTERM

app = Flask(__name__)
window = create_window("EGB-ENGINE", url="http://127.0.0.1:5000",
    width=1500, height=1000, resizable=False, confirm_close=True)

def start_server():
    app.run()

def start_windows():
    start(window)

s = Process(target=start_server)
w = Process(target=start_windows)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

s.start()
w.start()