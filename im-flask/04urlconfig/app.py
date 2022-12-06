from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def hello_world():
    """ 视图函数"""
    return "Hello world in 04 url config,ok"


app.add_url_rule("/home", "home", hello_world)


@app.route("/url_map")
def get_url_map():
    print(app.url_map)
    return str(app.url_map)


@app.route("/user/<page>")
def list_user(page):
    return "您好，你是第{}页用户".format(page)


@app.route("/user1/")
@app.route("/user1/<page>")
def list_user_opt(page=1):
    return "您好，你是user1第{}页用户".format(page)
