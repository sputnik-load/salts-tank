from salts_tank_app import app
from flask import request
import socket
import time


@app.route("/")
@app.route("/index")
def index():
    return request.args.get("aaa") \
            or "No parameters given"


@app.route("/conn")
def conntime():
    try:
        target = request.args.get("target", "localhost")
        port = int(request.args.get("port", "80"))
        s = socket.socket(socket.AF_INET,
                          socket.SOCK_STREAM)
        s.settimeout(1)
        st = time.time()
        s.connect((target, port))
        connect_time = time.time() - st
    except Exception:
        connect_time = 0.0

    if "s" in locals():
        s.close()

    return str(connect_time)
