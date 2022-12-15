from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/ajax')
def index():
    return render_template('ajaxjs.html')


@app.route('/ajax/jsjs', methods=['GET', 'POST'])
def ajax_jsjs():
    return 'js ajax', 200
    # return 'js ajax', 500


@app.route('/ajax/json', methods=['GET', 'POST'])
def ajax_json():
    import json
    print(request.values)
    user = {
        'username': '张三',
        'nickname': '昵称',
        'profile': {
            'age': 23
        }
    }
    return json.dumps(user), 200
    # return json.dumps(user), 500
    # return json.dumps(user), 401




@app.route('/ajax/jq')
def ajax_jq():
    return render_template('ajaxjq.html')


@app.route('/ajax/shortcut')
def ajax_shortcut():
    return render_template('ajax_shortcut.html')
