from flask import Flask, render_template

app = Flask(__name__)

# 1. 为模板引擎添加扩展，支持break/continue语法
app.jinja_env.add_extension("jinja2.ext.loopcontrols")


# 2. 需要在页面添加
# { % if loop.index > 2 %}
# { %
# break %}
# { % endif %}

@app.route("/")
def index():
    # 模板变量的使用
    # 1. 简单数据类型的渲染
    age = 50
    money = 66.55
    name = "张三"
    # 2. 用户信息dict
    user_info = {
        "username": "张三",
        "nickname": "Jack",
        "address.city": "广州",
        "address.area": "番禺"
    }
    # 3. 元组和列表
    tuple_city = ("北京", "上海", "广州", "深圳")
    list_city = ("北京", "上海", "广州", "深圳")

    # 4. 复杂的数据结构
    list_user = [
        {
            "username": "Jasper",
            "address": {
                "city": "北京"
            }
        },
        {
            "username": "Alex",
            "address": {
                "city": "上海"
            }
        }
    ]
    return render_template("index.html",
                           age=age,
                           money=money,
                           name=name,
                           user_info=user_info,
                           tuple_city=tuple_city,
                           list_city=list_city,
                           list_user=list_user
                           )


@app.route("/tag")
def tag():
    # 模板标签的使用
    var = 1
    list_user = [
        {"username": "张三三", "age": 33, "address": "北京"},
        {"username": "李思思", "age": 22},
        {"username": "王三三", "age": 31, "address": "广州"},
        {"username": "黄思思", "age": 25},
    ]
    list_empty = []
    return render_template("tag.html",
                           var=1,
                           list_user=list_user,
                           list_empty=list_empty
                           )


#  过滤器的使用
@app.route("/filter")
def use_filter():
    welcome = "hello,jasper"
    default_var = "传的值hello"
    default_none = None
    html_value = "<h2>标题加粗</h2>"
    phone_number = "13344444444"
    return render_template("user_filter.html",
                           welcome=welcome,
                           default_var=default_var,
                           default_none=default_none,
                           html_value=html_value,
                           phone_number=phone_number
                           )


# 电话号码脱敏处理，过滤器的编写
# 13344444444  -> 133****4444
@app.template_filter("phone_format")
def phone_format(phone_number):
    return phone_number[0:3] + "****" + phone_number[7:]


@app.route("/gf")
def golbal_func():
    return render_template("global_func.html")


# 模板中宏的使用
@app.route("/macro")
def macro():
    return render_template("macro.html")

# 模板中宏的使用
@app.route("/macro_file")
def macro_file():
    return render_template("macro_file.html")
