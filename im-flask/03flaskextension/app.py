from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def hello_world():
    return "Hello world in flask extension,ok"


# v1.0 之后的版本，不推荐的写法
# if __name__ == "__main__":
#     app.run()
