from flask import Flask, render_template, url_for, redirect, request
from helper.content_provider import ContentProvider
from helper.mailer import Mailer

app = Flask(__name__)
DEBUG = False
content_provider = ContentProvider(DEBUG)
mailer = Mailer()

@app.route("/")
@app.route("/en")
def en():
    return content_provider.language_site("en")

@app.route("/de")
def de():
    return render_template("home.html")

@app.route("/jp")
def jp():
    return content_provider.language_site("jp")

@app.route("/en/projects/website")
def website():
    video_source = ""
    heading = "CV-Website"
    paragraphs = []
    return render_template("project_read_more.html", video_source=video_source, heading=heading, paragraphs=paragraphs)

@app.route("/en/projects/downloader")
def downloader():
    return render_template("project_read_more.html")

@app.route("/en/projects/banking")
def banking():
    return render_template("project_read_more.html")

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    if mailer.send_mail(name, email, message):
        return redirect("/en")
    
    return redirect("/error")

if __name__ == "__main__":
    DEBUG = True
    content_provider = ContentProvider(DEBUG)
    app.run(host="0.0.0.0", port=5001, debug=True)
