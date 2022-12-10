from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from forms import RegisterForm, LoginForm

app = Flask(__name__)
# 如果配置了SECRET_KEY，可以不配WTF_CSRF_SECRET_KEY，保留SECRET_KEY
# app.config["WTF_CSRF_SECRET_KEY"] = "r45xxyi1355abc"
app.config["SECRET_KEY"] = "7899ssydgy"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@127.0.0.1/test_flask"
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'life_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    birth_date = db.Column(db.Date, nullable=True)
    age = db.Column(db.Integer, default=0)


@app.route("/")
def index():
    return render_template("index.html")

# 用户登录
@app.route('/login', methods=['GET', 'POST'])
def page_form():
    form = LoginForm()
    if form.validate_on_submit():
        print('登录成功')
    else:
        print(form.errors)
    return render_template('page_login.html', form=form)


# 用户注册
@app.route('/user/register', methods=['GET', 'POST'])
def page_register():
    form = RegisterForm()
    # 用户在提交表单的时候，会触发validate_on_submit
    if form.validate_on_submit():
        # 表单验证通过，接下来处理业务逻辑
        # 1. 获取表单数据
        username = form.username.data
        password = form.password.data
        birth_date = form.birth_date.data
        age = form.age.data
        # 2. 构建用户对象
        user = User(
            username=username,
            password=password,
            birth_date=birth_date,
            age=age
        )
        # 3. 提交到数据库
        db.session.add(user)
        db.session.commit()
        print('添加成功')
        # 4. 跳转到登录页面
        return redirect(url_for('index'))
    else:
        # 打印错误信息
        print(form.errors)
    return render_template('page_register.html', form=form)
