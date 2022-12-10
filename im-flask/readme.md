# Flask
## 入门Flask微框架
### 1. 入门Flask框架
#### 1.1 基本介绍
+ [Flask](https://flask.palletsprojects.com/en/2.2.x/)是Python实现的Web开发微框架
+ 小而美，丰富的周边扩展
+ flask的特点
  + 轻松掌握
  + 灵活掌握
  + 免费开源[源码](https://github.com/pallets/flask)
#### 1.2 安装flask
+ linux创建虚拟环境
```
# 创建虚拟环境  
virtualenv venv-im
# 激活虚拟环境  
source venv-im/bin/activate
#退出虚拟环境  
deactivate
```
+ windows创建虚拟环境
```
# 创建虚拟环境 
cd E:\Work\MyCode\python-venv\
virtualenv venv-im  
# 激活虚拟环境
E:\Work\MyCode\python-venv\venv-im\Scripts\activate
# 退出虚拟环境
deactivate
```
+ 第一种使用pip命令安装 
```
pip install flask
pip install -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com flask
```
![install flask](img/001.png)
+ 第二种 [源码](https://files.pythonhosted.org/packages/69/b6/53cfa30eed5aa7343daff36622843688ba8c6fe9829bb2b92e193ab1163f/Flask-2.2.2.tar.gz)安装  
```
wget https://files.pythonhosted.org/packages/69/b6/53cfa30eed5aa7343daff36622843688ba8c6fe9829bb2b92e193ab1163f/Flask-2.2.2.tar.gz
gzip -dc Flask-2.2.2.tar.gz | tar xvf -
cd Flask-2.2.2
python setup.py install
```
+ 验证是否已经安装成功
```
(venv-im) PS E:\Work\MyCode\python-im> python
Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.                        
>>> import flask
>>> flask.__version__
'2.2.2'
>>>
```
#### 1.3 第一个Flask程序
```
from flask import Flask

app = Flask(__name__)  

@app.route('/')
def  hello_word():
     return 'Hello World!'
```
### 2. MTV（Model、Template、View）模型
+ 1. 视图View
  - 视图扩展 `Flask-WTF / bootstrap-flask  / Flask-Uploads`
+ 2. 模型Model 
  - 模型扩展 `Flask-PyMongo / Flask-MongoKit / Flask-SQLAlchemy`
+ 3. 模板Template
  - 模板扩展`Jinja2`

### 3. Flask扩展
#### 3.1 启动选项及调试
+ 代码
```
from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def hello_world():
    return "Hello world in flask extension"


# v1.0 之后的版本，不推荐的写法
# if __name__ == "__main__":
#     app.run()
```
+ 启动服务器
```
# 步骤1： 设置环境变量
windows: set FLASK_APP=app.py
*inux:   export FLASK_APP=app.py
# 步骤2： flask run 启动内置web服务器
指定IP及端口：
flask run --host=0.0.0.0 --port=8001
或者：
flask run -h 0.0.0.0 -p 8001
```
![windows启动flask](img/002.png)
#### 3.2 开启调试模式
+ 代码修改后服务器自动重启
+ 步骤1： 设置环境变量
```
windows: set FLASK_ENV=development
*inux:   export FLASK_ENV=development
```
+ 步骤2： `flask run`启动内置web服务器
![启动调试模式](img/003.png)

#### 3.3开启调试模式v1.0以前
+ 直接执行app.py(v1.0以前)
+ 步骤1： 在文件中添加启动代码
```
if __name__ == "__main__":
    app.run(debug=True)
```
+ 步骤2：`python app.py`
> 提示： 切勿在生产环境下开启调试模式

#### 3.4 Flask的扩展
+ 什么是扩展： 为Flask应用增加功能的包
+ 有哪些常用的Flask扩展？
  + `Flask SQLAlchemy`
  + `Flask WTF`
  + `Flask mail`
  + `Flask RESTful`
+ [Flask的扩展](https://pypi.org/)
+ 为Flask写扩展
  + [英文链接](https://flask.palletsprojects.com/en/1.1.x/extensiondev/)
  + [中文链接](https://dormousehole.readthedocs.io/en/latest/extensiondev.html#extension-dev)
### 4.http基础知识
#### 4.1 URL及Http基础知识
+ 基本URL包含模式（或者协议）、服务器名称（或IP地址）、路径和文件名
`scheme://host[:port#]/path/.../[;url-params][?querey-string][#anchor]`
+ URL协议
  + http 超文本传输协议资源
  + https 用安全套接字层传送的超文本传输协议
  + ftp 文件传输协议
+ HTTP请求
  + GET
    + 可以用浏览器直接访问
    + 请求可以携带参数，但是有长度限制
    + 请求参数直接放在URL后面
  + POST
    + 不能使用浏览器直接访问
    + 对请求参数的长度没有限制
    + 可以用来上传文件等需求
+ HTTP常见状态码
  + 2xx 请求成功
  + 3xx 重定向
  + 4xx 请求错误
  + 5xx 服务器错误
#### 4.2 Url配置及路由
+ Pycharm配置调试模式
![Pycharm配置调试](img/004.png)
+ 路由配置
  + 方式一：使用装饰器 `@app.route(url_name, methods)`
  + 方式二：使用API配置 `app.add_url_rule(url,url_name,view_name)`
+ 方式一： 使用装饰器
  + 语法规则 `@app.route(url_name, methods)`
  + 参数解释
    + url：匹配的URL地址
    + methods：所支持的请求方式`(['GET','POST'])`
  + 示例： `@app.route("/login",methods=['GET','POST'])`
+ 方式二： 使用API配置
  + 语法规则 `app.add_url_rule(url,url_name,view_name)`
  + 参数解释
    + url： 匹配的URL地址
    + url_name: 给URL的命名
    + view_name: 视图函数
#### 4.3 路由匹配规则
+ 匹配整个文字 `@app.route("/hello")`
+ 传递参数  `@app.route("/user/< username >")`
+ 指定参数类型 `@app.route("/post/< int:post_id >")`
+ URL参数类型
  | 类型   | 描述                                |
  | ------ | ----------------------------------- |
  | string | 接受任何不包含斜杠 的文本（默认值） |
  | int    | 接受正整数                          |
  | float  | 接受正浮点数                        |
  | path   | 类似string，但可以包含斜杠          |
  | uuid   | 接受UUID字符串                      |
+ 查看URL规则列表 `app.url_map`
+ URL逆向解析（根据名称解析成URL字符串)
  + `url_for(url_name,**kwargs)`
  + 静态文件(js/css/图片)引用`url_for('static',filename='style.css')`

#### 4.4 视图函数中获取页面传值
+ URL中的值
```
@app.route("/page/<page>")
def list_user(page):
  return "您好，你是第{}页用户".format(page)
```
+ URL中的值为可选,一般在分页中经常用到，添加一个`@app.route("/user1/")`
```
@app.route("/user1/")
@app.route("/user1/<page>")
def list_user_opt(page=1):
    return "您好，你是user1第{}页用户".format(page)
```
### 5. flask请求与响应报文
#### 路由分发
![请求分派](img/005.png)
#### 上下文对象
+ 应用上下文
  + current_app 当前应用的实例
  + g  处理请求时的临时存储对象，每次请求都会重设这个变量
+ 请求上下文
  + request  请求对象，封装了客户端发出的HTTP请求中的内容
  + session  用户会话（dict），各请求之间的数据共享
+ 在分派请求之前激活应用上下文和请求上下文
+ 在请求处理完成后将其删除
#### 请求报文
+ 请求报文常见参数
  + method: 请求的类型(GET/POST/OPTIONS等)
  + form: POST请求数据dict
  + args: GET请求数据dict
  + values: POST请求和GET请求数据集合dict
  + files: 上传的文件数据dict
  + cookies: 请求中的cookie dict
  + headers: HTTP请求头
+ 请求钩子
  + 如下场景如何实现？
    + 每个请求中都要验证用户信息（是否已登录，是否有权限访问）
    + 限制来自某些IP的恶意请求
  + 使用钩子函数可以减少重复代码的编写，便于维护
  + `before_first_request` 服务器初始化后第一个请求到达前执行
  + `before_request` 每一个请求到达前执行
  + `after_request` 每次请求处理完成后执行，如果请求过程中产生了异常，则不执行
  + `teardown_reqeust` 每次请求处理完成之后执行，如果请求过程中产生了异常也执行
#### 响应报文
+ 响应
  + 可以是字符串
  + 可以是元组(tuple)
    + `(response,status,headers)`
    + `(response,headers)`
+ 响应报文
  + 响应元组
    + `response` 响应内容
    + `status` 响应状态码
    + `headers` 响应头信息
  + 使用make_response代替

### 6. flask视图
#### 重定向等内部视图
+ `redirect()`实现重定向
```
@app.route("/index")
def index():
    return "index"


@app.route("/")
def hello_world():
    # 访问/时重定向到/index这个页面
    return redirect("/index")
```
+ `abort()` 处理错误
```
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
```

## Flask模板语法与继承
### 1.什么是模板
07templatesintro
+ 怎样在浏览器展示HTML文件
+ 理解渲染机制
  + 没有模板渲染函数怎样在浏览器展示HTML文件
    + 1.在磁盘读取html字符串
    + 2.将满足特定规则的内容进行替换
    + 3.发送给浏览器展示
  ```
  @app.route("/show/html")
  def html_show():
    # 理解渲染机制
    # 1. 找到磁盘上的html文件地址(全路径)
    file_name = os.path.join(os.path.dirname(__file__), "templates", "index.html")
    # 2. 读取html文件中的内容
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_name, 'r', encoding="utf-8") as f:
        html = f.read()
        # 3. 替换html中的特殊字符({{time}})
        html = html.replace("{{time}}", now_time)
        # 4. 将html的内容发送给浏览器
        return html
  ```
+ 什么是模板
  + 模板其实就是一个包含响应文本的文件，其中用占位符(变量)表示动态部分，告诉模板引擎其具体的值需要从使用的数据中获取
  + 使用真实值替换变量，再返回最终得到的字符串，这个过程称为渲染
### 2.模板引擎介绍
08templatesdefaultengine
+ Flask使用Jinja2作为默认模板引擎
+ 安装
  + pip安装 `pip install Jinja2`
  + 源码安装 `python setup.py install`
+ 默认配置
  + `template_folder="templates"`  -- 模板的默认目录
  + `render_template()`     -- (x)html自动转义
  + `render_template_string()` -- 字符串自动转义
  + `{% autoescape %}` -- 手动设置是否转义
  + 全局函数和辅助对象 -- 增强模板的功能
#### 什么是转义
  + 把有特殊意义的字符显示出来
    + html标签中的`<>` -- `&lt;&gt;`
    + 代码中的`&` -- `&amp;`
    ![特殊字符转义对照表](img/006.png)
#### 全局对象
  + `config`    -- Flask的配置信息
  + `request`   -- 请求对象
  + `session`   -- 会话对象
  + `g`         -- 请求香港的全局变量（如：g.user)
#### 全局函数
+ `url_for()` URL解析函数（如：静态文件地址解析、链接跳转地址解析）
+ `get_flashed_messages()`  会话消息

#### 上下文处理器
+ 在模板的上下文中添加新的内容
+ 内容可以是变量，也可以是函数
```
@app.context_processor
def inject_user():
    return dict(user=g.user)
```
### 3.模板中变量的使用
09vari - index.html
#### 语法 `{{ value }}`
+ 基本数据类型的渲染 `{{ value }}`
+ dict类型数据的渲染 `{{ object.attribute }} ` 或者 `{{ object['attribute'] }}`
+ list/tuple类型数据的渲染
+ list/tuple嵌套dict复杂类型数据的渲染
### 4.模板语法 - 标签
#### 模板标签语法
  + 1. 语法 `{% tag %}`
  + 2. 语法
  ```
  {% tag %}
     内容
  {% endtag %}
  ```
####  if条件表达式
```
{% if condition_a %}
  满足了A条件
{% elif condition_b %}
  满足了B条件
{% else %}
  都不满足
{% endif %}
```
#### if标签中的is判断
```
{% if value is defined %}
......
{% endif %}
```
#### if内置的判断条件
+ `defined/undefined` 变量是否已经定义
+ `none` 变量是否为None
+ `number/string` 数字/字符串判断
+ `even/odd`  奇偶判断
+ `upper/lower` 大小写判断

#### if标签中的其他逻辑控制
```
and, or
==, !=
>, <
>=, <=
in, not in
```
#### for循环
```
<ul>
{% for key,value in data.items() %}
  <li class="{{ loop.cycle("odd","even")}}">
  {{ key }} : {{ value }}
  </li>
{% else %}
  <li>暂无数据</li>
{% endfor %}
</ul>
```
#### for循环体内的变量
+ `loop.index`    当前循环迭代的次数(从1开始)
+ `loop.index0`   当前循环迭代的次数(从0开始)
+ `loop.revindex` 到循环结束需要迭代的次数（从1开始）
+ `loop.revindex0`到循环结束需要迭代的次数（从0开始）
+ `loop.first`    如果是第一次迭代，为True
+ `loop.last`     如果是最后一次迭代，为True
+ `loop.length`   序列的长度
+ `loop.cycle`    在一串序列间期取值的辅助函数
#### for循环中使用continue/break
```
app.jinja_env.add_extension("jinja2.ext.loopcontrols")
{% for user in users %}
    {% if loop.index is even %}
      {% continue %}
    {% endif %}
{% endfor %}
```
> [添加其他扩展参考](https://jinja.palletsprojects.com/en/3.1.x/extensions/)

#### 添加注释
+ 不会显示在浏览器的HTML中
+ {# 注释内容 #}，在查看源码中不可见
+ 去除HTML中多余的空白
```
在块的开始或者结束放置一个减号(-), 不能有空格
{% for item in seq -%}
  {{ item }}
{%- endfor %}
```
![去除HTML中多余的空白](img/007.png)

#### 设置变量，赋值操作
+ 先设置，后使用，可以通过import导入
`{% set key,value = (1,2) %}`
+ 使用with代码块，实现块级作用域
```
{% with %}
  {% set value=42 %}
  {{ value }} 只在代码块中有效
{% endwith %}
```
#### 转义显示
+ 方式一： 视为字符串 `{{ "{{}} {%%}" }}`
+ 方式二： 使用raw标签
```
{% raw %}
  {% for key,value in data.items %}
    {{ key }} : {{ value }}
  {% endfor %}
{% endraw%}
```
### 5.模板语法 - 过滤器
09vari/user_filter.html
#### 什么是过滤器
+ 过滤器： 修改变量(如：格式化显示)
+ 用管道符号(|)分隔 `{{ name|striptags }}`
+ 可以链式调用 `{{ name|striptags|title }}`
+ 可以用圆括号传递可选参数 `{{ list|join(",")}}`
#### 过滤器的使用
+ 方式一： 用管道符号（|） `{{ value|safe }}`
+ 方拾二： 使用标签
```
{% filter upper %}
    This text becomes uppercase
{% endfilter %}
```
#### 内置的过滤器
+ 求绝对值 `{{ value|abs }}`
+ 默认值显示 `default(value, default_value="",boolean=False)`
  + `{{ value|default("默认值"")}}`
  + `{{ value|d("默认值")}}`
+ html转义 `{{ value|escape }} 或者 {{ value|e }}`
```
<h3>html转义过滤器的使用</h3>
{% autoescape False %}
<p>{{ html_value }}</p>
<p>{{ html_value|e }}</p>
{% endautoescape %}
```
+ 富文本内容转义显示 `{{ value|safe }}`
+ 倒序显示 `{{ value|reverse }}`
+ [更多内置过滤器](https://jinja.palletsprojects.com/en/3.1.x/templates/#list-of-builtin-filters)

#### 自定义过滤器
+ 方式一：使用装饰器注册
```
@app.template_filter("reverse")
def reverse_filter(s):
  return s[::-1]
```
+ 方式二： 调用函数注册
```
def reverse_filter(s):
    return s[::-1]
app.jinja_env.filters["reverse"]=reverse_filter
```
### 6.模板语法 - 全局函数
09vari/global_func.html
+ 全局韩式可在模板中直接使用
+ 示例：
```
<ul>
{% for i in range(10) %}
  <li> {{ i }}</li>
{% endfor %}
</ul>
```
#### 模板全局函数
+ `range([start],stop[,step])`
+ `dict(**items)`
+ `cycler(*items)` 可用于css类名的循环
```
<h3>cycler函数的使用</h3>
{% set class_name=cycler("row1","row2")%}
{% for i in range(10) %}
<p class="{{ class_name.next() }}">{{ i }}</p>
{% endfor %}
```
+ `joiner(sep=",")` 可用于字符串拼接
+ `url_for()` URL解析函数（如：静态文件地址解析、链接跳转地址解析）
### 7.模板中的宏
09vari/macro.html
#### 什么是宏
+ 把常用的功能抽取出来，使用可重用
+ 简单理解： 宏 ≈ 函数
+ 宏可以写在单独的html文件中
#### 定义宏
像书写函数一样定义宏
```
{% macro input(name,value="",type="text",size=20) -%}
<input type="{{ type }}" name="{{name}}" value="{{value|e}}" size="{{ size}}">
{%- endmacro%}
```
#### 使用宏 -- 像调用函数一样调用
```
<p> {{ input("username") }}</p>
<p> {{ input("password",type="password") }}</p>
```

#### 文件中宏的使用
09vari/macro_file.html
+ 1. 将前面定义的宏保存为forms.html
+ 2. 导入：
```
{% import "forms.html" as forms %}
{% from "forms.html" import input %}
```
+ 3. 使用  `<p>{{forms.input("username")}}</p>`
### 8.模板的继承与包含
10extendsinclude
index.html course.html coding.html
#### 继承实现
+ 步骤一：将可变的部分圈出来(base.html)
```
{% block content %}
  <!-- 内容区域-->
{% endblock %}
```
+ 步骤二： 继承父模板 `{% extends "base.html" %}`
+ 步骤三： 填充新的内容(index.html)
```
{% extends "base.html" %}
{% block content %}
<!-- 新的内容 -->
{% endblock %}
```
+ 步骤四： 复用父模板的内容（可选）
```
{% extends "base.html" %}
{% block header %}
  {{ super() }}
  <!-- 新的菜单内容 -->
{% endblock %}
```
#### 包含
article.html wenda.html
+ 步骤一： 将可变的部分拆出来(sidebar.html)
```
<div>
  这是右侧公共的部分
</div>
```
+ 步骤二： 将拆出来的部分包进来(index.html)
```
{% extends "base.html" %}
{% block content %}
<!--页面主要内容区域-->
{# 公用的区域#}
{% include "sidebar.html" %}
{% endblock %}
```
#### include标签
article.html ignore missing
wenda.html   without context
+ `{% include "sidebar.html" ignore missing %}` 
+ `{% include "sidebar.html" ignore missing with context %}`
+ `{% include "sidebar.html" ignore missing without context %}` 
+ `ignore missing` 如果模板不存在，Jinja2会忽略这条语句
+ `with context/without context` 是否携带当前页面的上下文

#### 代码复用
wenda.html
+ 当前页面的代码复用
```
{%block title %}{% endblock %}
<h1> {{self.title() }}</h1>
{% block content %}
{% endblock %}
```
#### 继承与包含的区别
+ 相关模板标签
  + `{% block sidebar %}{% endblock %}` -- 命名代码块
  +  `{% extends "base.html" %}`   -- 继承模块
  + `{% include "header.html" %}`  -- 包含代码块
### 9.消息闪现
11flashmessages
+ 第一步： 在视图中产生一个消息(提示/警告/错误)
```
flash(msg_content, msg_type)
参数msg_content: 消息内容
参数msg_type: 消息类型
```
+ 第二步：在模板中展示消息
```
get_flashed_messages(category_filter=["error"])
参数category_filter:对产生的消息按类别查询
<ul class="flashes">
  {% for category,message in  get_flased_messages(with_categories=true) %}
      <li class="{{ category }}"> {{ message }} </li>
  {% endfor %}
</ul>
```
+ 第三步： 需要设置secret_key
```
# session的安全机制，使用flash时需要设置该随机串
app.secret_key = "sk9uhuukk890"
```
## Flask中的ORM使用
### ORM介绍
#### 理解ORM
+ ORM(Object Relational Mapping) 对象关系映射
+ ORM的重要特性
  + 面向对象的编程思想，方便扩充
  + 少写（几乎不写）SQL，提升开发效率
  + 支持多种类型的数据库，方便切换
  + ORM技术成熟，能解决对大部分问题
### ORM安装
#### `flask-sqlclchemy`介绍及安装
+ 安装 
  + pip安装 `pip install -U Flask-SQLAlchemy --timeout 999`
  + 源码安装 `python setup.py install`
+ 安装依赖
  + `pip install mysqlclient`
#### flask-sqlalchemy配置
+ 数据库URI `SQLALCHEMY_DATABASE_URI` 统一资源标识符(uniform resource identifier,URI)是一个用于标识某一互联网资源名称的字符串
+ MySQL数据库URI参数格式 `mysql://root:root@localhost/mydatabase`
+ 多个数据库支持
```
SQLALCHEMY_BINDS={
  "db1":"mysqldb://localhost/users",
  "db2":"sqlite:////path/to/appmeta.db"
}
```
### ORM的CURD操作
12orm
#### 数据库模型设计
+ 绑定到Flask对象 `db = SQLAlchemy(app)`
+ ORM模型创建
```
class User(db.Model):
  id = db.Column(db.Integer,primary_key=True)
```
+ 指定表的名称  `__tablename__="life_user"`
+ 手动创建数据库
+ 创建表`db.create_all(bind="db1")`
+ 删除表 `db.drop_all()`
+ ORM模型自动类型支持
![ORM模型自动类型支持](img/008.png)
+ 一对多关系，外键关联
```
addresses=db.relationship("UserAddress", backref="address",lazy=True)
```
#### 新增/修改数据
+ 构造ORM模型对象
`user = User("admin","admin@example.com")`
+ 添加到`db.session`(备注：可添加多个对象)
` db.session.add(user) `
+ 提交到数据库
`db.session.commit()`

#### 物理删除数据
+ 查询ORM模型对象
`user = User.query.filter_by(username="zhangsan").first()`
+ 添加到db.session
`db.session.delete(user)`
+ 提交到数据库
`db.session.commit()`

#### ORM查询
+ 返回结果集(list)
  + 查询所有数据 `User.query.all()`
  + 按条件查询
  ```
    User.query.filter_by(username="zhangsan")
    User.query.filter(User.nickname.endswith("三")).all()
  ```
  + 排序  `User.query.order_by(User.username)`
  + 查询TOP10 `User.query.limit(10).all()`
+ 返回单个ORM对象
  + 根据主键pk查询 `User.query.get(1)`
  + 获取第一条记录 `User.query.first()`
+ 视图快捷函数： 有则返回，无则返回404
  + ` first() vs first_or_404() `
  + ` get()   vs get_or_404() `
+ 多表关联查询
  + `db.session.query(User).join(Address)`
  + `User.query.join(Address)`
+ 分页
  + 方式一： 使用offset和limit  `.offset(offset).limit(limit)`
  + 方式二：paginate分页支持 `.paginate(page=2,per_page=4)` 返回Pagination的对象
+ Pagination对象
  + has_prev/has_next  --- 是否有上一页/下一页
  + items              --- 当前页的数据列表
  + prev_num/next_num  --- 上一页/下一页的页码
  + total              --- 总记录数
  + pages              --- 总页数
```
<ul>
    {% for user in user_page_data.items %}
    <li>{{ user.username }} - {{ user.password }}</li>
    {% endfor %}
</ul>
{% if user_page_data.has_prev %}
<a href="{{ url_for('list_user', page=user_page_data.prev_num) }}">上一页</a>
{% else %}
<a>上一页</a>
{% endif %}
{% if user_page_data.has_next %}
<a href="{{ url_for('list_user', page=user_page_data.next_num) }}">下一页</a>
{% else %}
<a>下一页</a>
{% endif %}
</p>
```
+ 结合模板实现分页
  + 第一步： 准备数据 `list_user = User.query.filter_by(is_valid=1)`
  + 第二步： 分页 `list_user.paginate(page=2, per_page=4)`
  + 第三步： 在模板中实现分页操作
```
@app.route('/user/')
@app.route('/user/<int:page>/')
def list_user(page=1):
    """ 用户分页 """
    per_page = 3  # 每一页的数据大小
    # 1. 查询用户信息
    user_ls = User.query
    # 2. 准备分页的数据
    user_page_data = user_ls.paginate(page=page, per_page=per_page)
    return render_template('list_user.html', user_page_data=user_page_data)
```
## Flask表单的实现
### 表单介绍
test_form.html
#### 常见的表单元素
+ 表单标签  `<form>`
  + `action` 表单提交的`URl`地址
  + `method` 表单请求的方式（`GET/POST`）
  + `enctype` 请求内容的形式
    + `application/x-www-form-urlencoded`
    + `multipart/form-data`
+ 单号文本框/多行文本框
  + textarea 多行文本
  + 单行文本(type的不同值)
    + text -- 单行文本
    + password -- 密码
    + email   -- 邮箱
    + url     -- URL
    + number  -- 数字
    + color   -- 颜色
    + 日期时间等（date,month,week,time,datetime,datetime-local）
+ 选择(单选、多选、下拉选择)
  + 单选 `<input type="radio">`
  + 多选 `<input type="checkbox">`
  + 下拉选择 `<select> <option></option></select>`
+ 隐藏表单域 `<input type="hidden">`
+ 表单按钮 
  + `<input type="button">`
  + `<button></button>`
+ 文件上传框 `<input type="file">`
#### 在视图中获取表单值
+ GET请求
```
request.args.get("name", None)
```
+ POST请求
```
request.form.get("name", None)
```
### wtf表单介绍
page_form.html
#### flask-wtf表单介绍
+ 集成wtforms
+ CSRF保护
+ 与Flask-Uploads一起支持文件上传
+ 安装
  + pip安装 `pip install Flask-WTF`
  + 源码安装 `python setup.py install`
+ 配置（CSRF保护） `WTF_CSRF_SECRET_KEY="a random string"`
  + 如果使用flash配置了`SECRET_KEY`,`WTF_CSRF_SECRET_KEY`也可以不配置

#### 第一个表单模型
```
from flask_wtf import FlaskForm
from wtforms import StringField

class LoginForm(FlaskForm):
  username = StringField(label="用户名")
```
#### 表单常用字段类型及渲染
+ 表单字段的常用核心参数
  + label  -- label标签(如：输入框前的蚊子描述)
  + default  -- 表单的默认值
  + validators -- 表单验证规则
  + widget  -- 定制界面显示方式（如：文本框、选择框）
  + description -- 帮助文字
+ 表单渲染
  + 使用模板语法渲染表单内容
    + 表单输入区域： `{{ form.username }}`
    + 表单label： `{{ form.username.label.text }}`
+ 表单常用字段类型
  + 文本/字符串
    + `StringField`  -- 字符串输入
    + `PasswordField` -- 密码输入
    + `TextAreaField`  -- 长文本输入
    + `HiddenField`   -- 隐藏表单域
  + 数值(整数，小数)
    + `FloatField`  -- 浮点数输入
    + `IntegerField` -- 整数输入
    + `DecimalField` -- 小数输入(更精确)
  + 选择
    + `RadioField` -- radio单选
    + `SelectField` -- 下拉单选
    + `SelectMultipleField` -- 下拉多选
    + `BooleanField` -- 勾选（复选框）
  + 日期/时间
    + `DateField` -- 日期选择
    + `DateTimeField` -- 日期时间选择
  + 文件/文件上传
    + `FileField`  -- 文件单选
    + `MultipleFileField` -- 文件多选
  + 其它
    + `SubmitField`  -- 提交按钮
    + `FieldList`  -- 自定义的表单选择列表（如：选择用户对象）
    + `FormField` -- 自定义多个字段构成的选项
#### 通过表单保存数据
page_register.html
+ 第一步： 检测表单是否已经通过验证 `form.validate_on_submit()`
+ 第二步： 获取表单中传递过来的值 `form.field_name.data`
+ 第三步： 业务逻辑代码编写（可结合ORM）

#### CSRF表单保护
+ 默认开启CSRF保护
+ 关闭单个表单CSRF保护 `form = LoginForm(csrf_enabled=False)`
  + 1. LoginForm
  ```
        def __init__(self, csrf_enabled, *args, **kwargs):
        super().__init__(csrf_enabled=csrf_enabled, *args, **kwargs)
  ```
  + 2. app中实例化，csrf_enabled为False
  ` form = RegisterForm(csrf_enabled=False)`
+ 全局关闭(不推荐) `WTF_CSRF_ENABLED = FALSE`
#### 同步请求CSRF保护
+ 模板中添加csrf_token
```
{{ form.csrf_token }}
或者
<input type="hidden" name="csrf_token" value="{{csrf_token() }}"/>
```
### 表单验证
14formvalid
#### 表单验证
+ 步骤1： 导入内置的表单验证器(或自定义)`from wtforms.validators import DataRequired `
+ 步骤2： 配置到表单字段
```
username = StringField("用户名",validators=[InputRequired(),my_validator])
```
#### 内置表单验证器
+ `DataRequired/InputRequired` -- 必填
+ `Email/URL/UUID`   -- 电子邮箱/URL/UUID
+ `Length(min=-1, max=-1, message=None)`  -- 长度范围验证
+ `EqualTo(fieldname, message=None)` -- 两个字段输入的值相等（如：密码确认）

#### 自定义表单验证
+ 场景一： 只有本表单使用 `validate_username`
```
from flask_wtf import FlaskForm
from wtforms import StringField
class RegisterForm(FlaskForm):
    username = StringField(label='用户名', default='')
    password = PasswordField(label='密码', validators=[DataRequired('请输入密码')])
    birth_date = DateField(label='生日')
    age = IntegerField(label='年龄')
    submit = SubmitField('注册')

    def validate_username(self, field):
        # 强制验证用户名为手机号
        username = field.data
        pattern = r'^1[0-9]{10}$'
        if not re.search(pattern, username):
            raise ValidationError('请输入手机号码')
        return field
```
+ 场景二： 多个表单中使用，如： 验证手机号码 `phone_required`
```
import re

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, IntegerField
from wtforms.validators import DataRequired, ValidationError


def phone_required(form, field):
    # 自定义的手机号验证
    # 强制验证用户名为手机号
    username = field.data
    pattern = r'^1[0-9]{10}$'
    if not re.search(pattern, username):
        raise ValidationError('请输入手机号码')
    return field

class LoginForm(FlaskForm):
    """ 登录表单的实现 """
    username = StringField(label='用户名', default='admin', validators=[phone_required])
    password = PasswordField(label='密码')
    submit = SubmitField('登录')

# 用户注册表单
class RegisterForm(FlaskForm):
    username = StringField(label='用户名', default='')
    password = PasswordField(label='密码', validators=[DataRequired('请输入密码')])
    birth_date = DateField(label='生日')
    age = IntegerField(label='年龄')
    submit = SubmitField('注册')

    def validate_username(self, field):
        # 强制验证用户名为手机号
        username = field.data
        pattern = r'^1[0-9]{10}$'
        if not re.search(pattern, username):
            raise ValidationError('请输入手机号码')
        return field

```
### 图片上传
15formupload
#### 两个方式实现文件上传
+ 方式一： 不使用wtf实现
+ 方式二： 使用FileField并添加类型验证
+ 文件名称格式化 `from werkzeug.utils import secure_filename`
#### 图片上传 - 不使用wtf
img_upload.html
+ 第一步： 设置form的enctype `enctype="multipart/form-data"`
+ 第二步： 在视图函数中获取文件对象 `request.files`
+ 第三步： 保存文件 `f.save(file_path)`
#### 图片上传  - 验证
avatar_upload.html
+ `FileRequired`   -- 文件必须上传验证
+ `FileAllowed`    -- 文件类型验证
```
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import FileField


class UserAvatarForm(FlaskForm):
    """ 用户头像上传 """
    avatar = FileField(label='上传头像', validators=[
        FileRequired('请选择头像文件'),
        FileAllowed(['png'], '仅支持PNG图片上传')
    ])

```
#### 使用扩展: Flask-Uploads
+ 常用文件类型验证
+ 指定文件上传的目录
## Pycharm快捷键
+ ctrl+shift+f10 ：运行脚本
+ ctrl+/ ：注释行
+ ctrl+p ：查看函数参数
+ ctrl+Space ：基本的代码完成,可以根据需要调整 Ctrl + J
+ shift+enter ：另起一行
+ Alt + Enter : import导入
+ Ctrl + Alt + Space : 快速导入任意类
+ Ctrl + F12       弹出文件结构
+ Ctrl + H          类型层次结构
+ Ctrl + Shift + H   方法层次结构
+ Ctrl + Alt + H     调用层次结构
## Refer
+ [flask](https://flask.palletsprojects.com/en/2.2.x/)
+ [flask](https://dormousehole.readthedocs.io/en/latest/quickstart.html)
+ [flask 源码](https://github.com/pallets/flask)
+ [pypi](https://pypi.org/)
+ [flask扩展英文链接](https://flask.palletsprojects.com/en/1.1.x/extensiondev/)
+ [flask扩展中文链接](https://dormousehole.readthedocs.io/en/latest/extensiondev.html#extension-dev)
+ [Jinja其他扩展](https://jinja.palletsprojects.com/en/3.1.x/extensions/)
+ [更多内置过滤器](https://jinja.palletsprojects.com/en/3.1.x/templates/#list-of-builtin-filters)