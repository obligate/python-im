from flask import Flask, render_template, render_template_string, g, url_for

app = Flask(__name__, template_folder="templ")


@app.route("/")
def index():
    return "index"


@app.route("/html")
def html():
    return render_template("index.html")


@app.route("/html/str")
def html_str():
    # 不从磁盘读取文件，直接输出string
    html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
        </head>
        <body>
            <h1> render_template_string </h1>
        </body>
        </html>
    """
    return render_template_string(html)


@app.route("/html/zy")
def html_zy():
    return render_template("index_zy.html")


@app.route("/html/config")
def html_config():
    return render_template("index_config.html")


@app.before_request
def before_request():
    g.user = "zhangsan"


@app.route("/gf")
def g_function():
    url_list = []
    url_list.append(url_for('html', _external=True))
    url_list.append(url_for('html_config', _external=True))
    url_list.append(url_for('g_function'))

    for v in url_list:
        print(v)

    return render_template("index.html")


@app.context_processor
def inject_user():
    return dict(user=g.user)
