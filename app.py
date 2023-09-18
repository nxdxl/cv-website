import json
import subprocess
from flask import Flask, render_template, url_for, redirect, request
app = Flask(__name__)

def read_json(path: str) -> dict:
    with open(path, "r") as json_file:
        return json.load(json_file)

def send_mail(mail_data: list) -> None:
    subprocess.run(["sh", "/app/sendmail.sh", mail_data[0], mail_data[1], mail_data[2]])

@app.route("/")
@app.route("/en")
def en():
    work_projects = read_json("/app/static/content/en/work_projects.json")["projects"]
    # work_projects = read_json("/Users/tom/projects/cv-website/static/content/en/work_projects.json")["projects"]

    personal_projects = read_json("/app/static/content/en/personal_projects.json")["projects"]
    # personal_projects = read_json("/Users/tom/projects/cv-website/static/content/en/personal_projects.json")["projects"]

    university_projects = read_json("/app/static/content/en/uni_projects.json")["projects"]
    # university_projects = read_json("/Users/tom/projects/cv-website/static/content/en/uni_projects.json")["projects"]

    return render_template("home.html", language="en", work_projects=work_projects, personal_projects=personal_projects, university_projects=university_projects)

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
    app.run(host="0.0.0.0", port=5001, debug=True)
