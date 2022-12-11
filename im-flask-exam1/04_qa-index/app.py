from flask import Flask

from models import db, User, UserProfile, Question, Answer, AnswerComment
from accounts.views import accounts
from qa.views import qa

app = Flask(__name__, static_folder='assets')
# 从配置文件加载配置
app.config.from_object('conf.Config')

# 数据库初始化
db.init_app(app)

# 注册蓝图
app.register_blueprint(accounts, url_prefix='/accounts')
app.register_blueprint(qa, url_prefix='/')


@app.route("/init_db")
def init_db():
    with app.app_context():
        db.drop_all()
        db.create_all()
    return "init db successfully"


@app.route("/init_user")
def init_user():
    for i in range(1, 10):
        user = User(id=i, username="Jack{}".format(i), nickname="张三{}".format(i), password="1234567",
                    status=1, is_super=0)
        db.session.add(user)
    db.session.commit()
    return "init user successfully"


@app.route("/init_user_profile")
def init_user_profile():
    for i in range(1, 10):
        userprofile = UserProfile(id=i, username="Jack{}".format(i), real_name="张三{}".format(i),
                                  maxim="我的个性签名{}".format(i),
                                  sex="男", address="地址{}".format(i), user_id=i)
        db.session.add(userprofile)
    db.session.commit()
    return "init user profile successfully"


@app.route("/init_qa")
def init_qa():
    count = 1
    for i in range(1, 10):
        for j in range(1, 10):
            count = (i - 1) * 10 + j
            qa = Question(id=count, title="钟南山团队从尿液中分离出新冠病毒，这对疫情防治有什么影响？",
                          desc="Vigorous Cooler： 尿液出现病毒并不罕见，但第一步是病毒要进入循环系统（血液、淋巴）。 比如寨卡病毒通过蚊子吸血进入循环系统，再进入泌尿系统。对于新型冠状病毒来说，第一步是通过呼吸系统进入下.",
                          content="27日，广州市政府新闻办在广州医科大学举办疫情防控专场新闻通气会，国家卫健委高级别专家组组长、国家呼吸系统疾病临床医学研究中心主任钟南山谈到疫情的预测时表示，疫情开始时，国外有流行病学家用权威的试验模型，预测2月初，中国感染新冠肺炎人数将达16万人。钟南山说：“这是没有考虑到国家的强力干预，也没有考虑春节后的延迟复工，我们也做了预测模型，2月中旬或下旬达到疫情高峰，确诊病例约六、七万人，投到国外权威期刊，被退了回来，感觉和上面的预测水平差太多，还有人给我微信‘你的话几天之内就会被碾个粉碎’。但事实上，我们预测更接近权威。",
                          is_valid=1, reorder=1, user_id=i)
            db.session.add(qa)
    db.session.commit()
    return "init qa successfully"


@app.route("/init_answer")
def init_answer():
    count = 1
    for i in range(1, 10):
        for j in range(1, 10):
            count = (i - 1) * 10 + j
            answer = Answer(id=count, content="回答{}".format(j), is_valid=1, user_id=i, q_id=i)
            db.session.add(answer)
    db.session.commit()
    return "init answer successfully "


@app.route("/init_answer_comment")
def init_answer_comment():
    import random
    count = 1
    for i in range(1, 10):
        for j in range(1, 10):
            count = (i - 1) * 10 + j
            answercomment = AnswerComment(id=count, content="评论{}".format(j), love_count=random.randint(1, 1000),
                                          is_public=1, is_valid=1, user_id=i, answer_id=i, q_id=i)
            db.session.add(answercomment)
    db.session.commit()
    return "init answer  comment successfully "
