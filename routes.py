from app import app as mapp
from flask import request
import yaml
import os
import magichue


def get_ip():
    if "rgb_ip" not in mapp.global_data:
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(ROOT_DIR, '../../configuration.yml')
        with open(config_path) as file:
            data = yaml.load(file.read())
        mapp.global_data["rgb_ip"] = data["rgb_ip"]
    return mapp.global_data["rgb_ip"]


@mapp.route("/rgb", methods=['GET', 'POST'])
def rgb_admin():
    body = request.get_json()
    r = body.get("r", 0)
    g = body.get("g", 0)
    b = body.get("b", 0)

    for ip in get_ip():
        light = magichue.Light(ip)
        light.on = True
        light.rgb = (r, g, b)

    return str(get_ip())
