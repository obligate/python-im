from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, IntegerField


# 登录表单
class LoginForm(FlaskForm):
    username = StringField(label='用户名', default='admin')
    password = PasswordField(label='密码')
    submit = SubmitField('登录')


# 用户注册表单
class RegisterForm(FlaskForm):
    # def __init__(self, csrf_enabled, *args, **kwargs):
    #     super().__init__(csrf_enabled=csrf_enabled, *args, **kwargs)

    username = StringField(label='用户名', default='')
    password = PasswordField(label='密码')
    birth_date = DateField(label='生日')
    age = IntegerField(label='年龄')
    submit = SubmitField('注册')
