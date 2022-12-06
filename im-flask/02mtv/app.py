from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def hello_world():
    return 'Hello World!'


@app.route('/hello')
def hello():
    user = {
        'name': '张三'
    }
    return render_template('hello.html', user=user)


if __name__ == '__main__':
    app.run()
