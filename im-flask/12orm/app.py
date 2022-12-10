from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@127.0.0.1/test_flask"
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'life_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    birth_date = db.Column(db.Date, nullable=True)
    age = db.Column(db.Integer, default=0)


class UserAddress(db.Model):
    """ 用户的地址 """
    __tablename__ = 'life_user_addr'
    id = db.Column(db.Integer, primary_key=True)
    addr = db.Column(db.String(256), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('life_user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('address', lazy=True))


# 首页
@app.route("/")
def index():
    return render_template("index.html")


# 初始化db
@app.route("/init_db")
def init_db():
    with app.app_context():
        db.drop_all()
        db.create_all()
    return "init db successfully"


# 初始化数据
@app.route("/init_data")
def init_data():
    for i in range(1, 10):
        user = User(id=i, username="张三{}".format(i), password="1234567", birth_date="2022-12-09")
        db.session.add(user)
    db.session.commit()
    return "init data successfully"


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
