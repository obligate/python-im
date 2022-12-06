from flask import Flask

# 第一个参数是应用模块或者包的名称。 __name__ 是一个适用于大多数情况的快捷方式。
# 有了这个参数，Flask 才能知道在哪里可以找到模板和静态文件等东西。
app = Flask(__name__)


# 装饰器 app.route()
# 表示一个路由配置，即：用户在浏览器输入URL，使用对应的函数处理其中的业务逻辑（可写多个）
@app.route('/')
@app.route('/index')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
