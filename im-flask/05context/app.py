from flask import Flask, current_app, request, make_response, render_template

app = Flask(__name__)


@app.route("/index")
def hello_world():
    print(app)
    print(current_app)
    print(app == current_app)  # 值相等 True
    print(app is current_app)  # 引用不同 False
    return "index"


# 请求报文
# 1. 获取get参数
# 2. 解析请求头中的IP地址
@app.route("/te/request")
def te_request():
    # 1. 获取get参数
    get_args = request.args
    print(get_args)
    # 页码一定是正整数
    page = request.args.get("page", 1)
    print(page)
    # 服务器所在的主机地址
    headers = request.headers
    print(headers)
    print("服务器所在的主机地址 {}".format(headers.get("host")))
    # 获取ip地址
    ip = request.remote_addr
    print("远程ip地址 {}".format(ip))
    # 获取user-agent
    user_agent = request.headers.get("user-agent", None)
    print("User-Agent: {}".format(user_agent))
    return "request success"


@app.route("/")
def index():
    return "index"


# 服务器启动后第一个请求到达
@app.before_first_request
def first_request():
    print("first_request")


# 每一个请求到达前
@app.before_request
def per_request():
    print("before request")


# 响应报文
@app.route("/te/response1")
def te_response1():
    return "response1 success"


# 响应报文
@app.route("/te/response2")
def te_response2():
    return "response2 success", 201


# 响应报文
@app.route("/te/response3")
def te_response3():
    return "response3 success", 401, {
        "user_id": "my_user_id"
    }


# 响应报文
@app.route("/te/response4")
def te_response4():
    # 构造一个响应对象
    # resp = make_response('这是一个响应对象')
    # resp = make_response('这是一个响应对象', 403)
    resp = make_response('这是一个响应对象', 403, {
        "token": "abc123"
    })
    # 也可以通过响应头来修改
    resp.headers['user_id'] = "myid_123"
    resp.status = 200
    return resp


# 响应报文, 使用html
@app.route("/te/response5")
def te_response5():
    html = "<html><body><h1 style='color:#f00'>HTML文本显示</h1></body></html>"
    resp = make_response(html)
    return resp


# 响应报文, 从文件中读取html
@app.route("/te/html")
def te_html():
    html = render_template("index.html")
    return html


# 响应报文, 从文件中读取html1
@app.route("/te/html1")
def te_html1():
    html = render_template("index.html")
    resp = make_response(html, 400)
    return resp
