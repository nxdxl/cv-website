from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/en")
def en():
    return render_template("layout_new.html", language="en")

@app.route("/de")
def de():
    return render_template("home.html", language="de")

@app.route("/jp")
def jp():
    return render_template("home.html", language="jp")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
