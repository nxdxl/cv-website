import json
import subprocess
from typing import Tuple
from flask import Flask, render_template, url_for, redirect, request
app = Flask(__name__)
DEBUG = False

def read_json(path: str) -> dict:
    with open(path, "r") as json_file:
        return json.load(json_file)

def send_mail(mail_data: list) -> None:
    subprocess.run(["bash", "/app/send.sh", mail_data[0], mail_data[1], mail_data[2]])

def set_en_projects() -> list:

    projects = []

    if not DEBUG:
        projects.append(read_json("/app/static/content/en/work_projects.json"))
        projects.append(read_json("/app/static/content/en/personal_projects.json"))
        return projects

    projects.append(read_json("/Users/tom/projects/cv-website/static/content/en/work_projects.json"))
    projects.append(read_json("/Users/tom/projects/cv-website/static/content/en/personal_projects.json"))
    return projects

def set_en_about() -> Tuple[list, str]:
    about_list = []
    if not DEBUG:
        about_dict = read_json("/app/static/content/en/about.json")
    else:
        about_dict = read_json("/Users/tom/projects/cv-website/static/content/en/about.json")

    for item in about_dict.values():
        about_list.append(item)
    return about_list, about_dict["heading"]


@app.route("/")
@app.route("/en")
def en():
    projects = set_en_projects()
    about_list, heading = set_en_about()
    return render_template("home.html", language="en", project_lists=projects, about_heading=heading, about_p=about_list)

@app.route("/de")
def de():
    return render_template("home.html", language="de")

@app.route("/jp")
def jp():
    return render_template("home.html", language="jp")

@app.route("/contact", methods=["POST"])
def contact():
    data = []
    data.append(request.form["name"])
    data.append(request.form["email"]) 
    data.append(request.form["message"])
    
    send_mail(data)

    return redirect("/en")

if __name__ == "__main__":
    DEBUG = True
    app.run(host="0.0.0.0", port=5001, debug=True)
