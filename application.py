# save this as app.py
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/publications")
def publications():
    return render_template("publications.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/code")
def code():
    return render_template("code.html")


if __name__ == "__main__":
    app.run()