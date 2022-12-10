from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import FileField


class UserAvatarForm(FlaskForm):
    """ 用户头像上传 """
    avatar = FileField(label='上传头像', validators=[
        FileRequired('请选择头像文件'),
        FileAllowed(['png'], '仅支持PNG图片上传')
    ])
