from flask import Flask, render_template

app = Flask(__name__)


# 首页
@app.route("/")
def index():
    return render_template("index.html")


# 免费课程
@app.route("/course")
def course():
    return render_template("course.html")


# 实战课程
@app.route("/coding")
def coding():
    return render_template("coding.html")


# 手记
@app.route("/article")
def article():
    return render_template("article.html")


# 问答
@app.route("/wenda")
def wenda():
    wenda = "wenda??"
    return render_template("wenda.html", wenda=wenda)
