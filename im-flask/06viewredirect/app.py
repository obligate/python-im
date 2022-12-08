from flask import Flask, redirect, abort, request

app = Flask(__name__)


@app.route("/index")
def index():
    return "index"


@app.route("/")
def hello_world():
    # 访问/时重定向到/index这个页面
    return redirect("/index")


@app.route("/ab1")
def ab1_index():
    # 当用户不满足某些条件的时候，就触发异常
    # ip拦截
    ip_list = ["127.0.0.1"]
    ip = request.remote_addr
    if ip in ip_list:
        abort(403)
    return "hello success"


@app.route("/ab2")
def ab2_index():
    # 当用户不满足某些条件的时候，就触发异常
    # ip拦截
    ip_list = ["127.0.0.2"]
    ip = request.remote_addr
    if ip in ip_list:
        abort(403)
    return "hello success"


@app.errorhandler(403)
def forbidden_page(err):
    print(err)
    return "您没有权限访问，请联系管理员开通权限"
