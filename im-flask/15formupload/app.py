import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

from forms import UserAvatarForm

app = Flask(__name__)
app.config['WTF_CSRF_SECRET_KEY'] = 'abc1234abc'  # csrf
app.config['SECRET_KEY'] = '444abc'  # flash
# 自定义的配置扩展，表示文件上传的路径
app.config['UPLOAD_PATH'] = os.path.join(os.path.dirname(__file__), 'static/uploads')


@app.route('/')
def index():
    # 首页
    return render_template('index.html')


# 不使用wtf实现的文件上传
@app.route('/img/upload', methods=['GET', 'POST'])
def img_upload():
    if request.method == 'POST':
        # 获取文件列表
        files = request.files
        file1 = files.get('file1', None)
        if file1:
            # 保存文件
            f_name = secure_filename(file1.filename)
            print('filename:', f_name)
            file_name = os.path.join(app.config['UPLOAD_PATH'], f_name)
            if not os.path.exists(app.config["UPLOAD_PATH"]):
                os.makedirs(app.config["UPLOAD_PATH"])
            file1.save(file_name)
            print('保存成功')
        return redirect(url_for('img_upload'))
    return render_template('img_upload.html')


# 头像上传
@app.route('/avatar/upload', methods=['GET', 'POST'])
def avatar_upload():
    form = UserAvatarForm()
    if form.validate_on_submit():
        # 获取图片对象
        img = form.avatar.data
        f_name = secure_filename(img.filename)
        file_name = os.path.join(app.config['UPLOAD_PATH'], f_name)
        if not os.path.exists(app.config["UPLOAD_PATH"]):
            os.makedirs(app.config["UPLOAD_PATH"])
        img.save(file_name)
        print('保存成功')
        return redirect('/')
    else:
        print(form.errors)
    return render_template('avatar_upload.html', form=form)
