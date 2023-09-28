import json
import subprocess
import smtplib
import os
from typing import Tuple
from flask import Flask, render_template, url_for, redirect, request
from content import ContentProvider

app = Flask(__name__)
DEBUG = False
content_provider = ContentProvider(DEBUG)

def send_mail(mail_data: dict) -> bool:
    from_address = os.environ.get("FROM_ADDRESS")
    to_address = os.environ.get("TO_ADDRESS")
    password = os.environ.get("PASSWORD")

    message = f"From: {from_address}\r\nTo: {to_address}\r\nSubject: Message from website\r\n\r\nName: {mail_data['name']}\nE-Mail: {mail_data['email']}\nMessage: {mail_data['message']}"

    smtp_obj = smtplib.SMTP("smtp.mail.me.com", 587)
    smtp_obj.starttls()
    smtp_obj.login(from_address, password)

    try:
        send_status = smtp_obj.sendmail(from_addr=from_address, to_addrs=to_address, msg=message)
        if send_status != {}:
            print("There was a problem sending the email.")
            return False

    finally:
        smtp_obj.quit()
        return True


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
    data = {}
    data["name"] = request.form["name"]
    data["email"] = request.form["email"]
    data["message"] = request.form["message"]
    
    if send_mail(data):
        return redirect("/en")

    return redirect("/error")

if __name__ == "__main__":
    DEBUG = True
    content_provider = ContentProvider(DEBUG)
    app.run(host="0.0.0.0", port=5001, debug=True)
