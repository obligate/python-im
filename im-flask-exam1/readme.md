# Flask开发实现在线问答系统
## v1.0 首页的基本功能
### 整合前端页面
### ORM模型分析及实现
+ 先建立数据库，再db.create_all()
+ 使用蓝图后，db.create_all()的使用
+ 扩展知识点： 修改模型后的表同步(flask-migrate)
### 使用蓝图来改进项目
#### 蓝图的实现方式
+ 按功能划分
+ 按模块划分
#### 蓝图实现的过程
+ 第一步：按模块拆分
  + ORM模型、配置、常量、工具类、功能模块等
+ 第二步： 视图文件中，实例化一个蓝图对象
` accounts = Blueprint('accounts', __name__,template_folder='templates', static_folder='../assets')`
+ 第三步：注册蓝图
```
from accounts.views import accounts
app.register_blueprint(accounts, url_prefix='/accounts')
```
### 问题列表页开发
### 问题详情动态页面开发
+ 问题详情动态页面开发
  + 第一步，使用模板语法将详情页改造
  + 第二步，将需要展示评论，关注的信息从数据库取出
  + 第三步，取出第一条回答内容并展示共有多少回答
## v1.1 用户注册和登录
### 用户注册功能
+ 注册表单编写及验证
  + 用户名为手机号码，且不能重复
  + 昵称长度验证
  + 密码及确认密码
+ 使用ORM保存用户信息
+ flash消息闪现提示用户去登录
### 用户登录原理、实现简单的登录
+ 登录表单输入用户名和密码
+ 验证用户名和密码是否正确，执行登录操作
+ 记录登录日志
+ 跳转到上一次访问的页面或者首页
### 使用Flask扩展实现登录
### 登录验证


## v1.2 发布问题
### 问题发布
+ 实现发布表单及验证
+ 支持上传"题图"
### 问题发布，带图片
+ 安装 flask-ckeditor `pip install flask-ckeditor`
+ 配置Ckeditor并提交发布问题内容
### ajax异步请求，原理及实现（异步分页处理）
#### Ajax 原理
+ 步骤1: 创建XMLHttpRequest/ActiveObject对象
+ 步骤2： 注册回调函数
+ 步骤3： 配置请求参数
+ 步骤4： 发送请求
+ 步骤5： 创建回调
#### XMLHttpRequest对象
+ 用于在后台与服务器交换数据
+ XMLHttpRequest的几种状态
  + 0: 对象没有完成初始化
  + 1: 对象开始发送请求
  + 2: 对象的请求发送完成
  + 3: 对象开始读取服务器响应
  + 4: 对象读取服务器响应结束

#### jQuery中的AJAX函数
+ .ajax(options)函数
  + url     -- 请求地址
  + method  -- 请求类型
  + data    -- 请求参数
  + dataType -- 返回的数据类型(xml/html/json等)
  + headers  -- 请求头信息
  + success  -- 请求成功后的回调
  + error    -- 发生错误后的回调(状态码不为2xx)
  + complete -- 请求完成后的回调

#### AJAX快捷函数
+ `.post()`     -- post请求
+ `.get()`      -- get请求
```
      $('a').click(function () {
        $.get('http://127.0.0.1:8081/ajax/json', {
            'username': 'zhangsan',
            'password': '123123'
        }, function (res) {
          res = JSON.parse(res)
          console.log(res);
          console.log(res.username);
          alert('请求成功')
        })
      })
```
+ `.getJSON()`  -- get请求json数据
```
      $('a').click(function () {
        $.getJSON('http://127.0.0.1:8081/ajax/json', {
            'username': 'zhangsan',
            'password': '123123'
        }, function (res) {
          console.log(res);
          console.log(res.username);
          alert('请求成功')
        })
      })
```
+ ajax全局设置
  + ajaxSetup()全局设置使用场景
    + 请求响应拦截,如: http状态码为401调整到登录界面
    + 添加全局参数,如: error:function(event,statusText){}
    + 添加请求头信息
```
 $.ajaxSetup({
          headers: {
              'appfrom': 'h5'
          },
          error: function (event) {
            console.log(event.status);
            if(event.status === 401) {
                alert('请登录')
            } else {
               alert('发生了错误')
            }
          }
      })
```
### Restful风格接口
#### API步骤
+ 第一步： 后端（视图层）编写数据接口
+ 第二步： 前端（模板层）调用数据接口
+ 第三步:  渲染页面、绑定功能
#### 什么是RESTful API
+ REST就是一种设计API的模式
+ 是一种网络应用程序的设计风格和开发方式
#### RESTful API的特点
+ 每一个URI代表1中资源
  + URI不应该使用动作来描述
  + 错误示范
  ```
  GET     /getUser/1
  POST    /createUser
  PUT     /updateUser/1
  DELETE  /deleteUser/1
  ```
+ 更"纯净"的URL
```
// 所有的用户列表
http://localhost/users
// 编号为1的用户详细信息
http://localhost/users/1
```
+ 用不同的HTTP请求方式来操作它

  | 类型      | 描述 |
  | --------- | ---- |
  | POST      | 新增 |
  | GET       | 查询 |
  | PUT/PATCH | 修改 |
  | delete    | 删除 |

+ 更"精简"的方式处理结果

  | 状态码 | 描述                  | 请求方式       |
  | ------ | --------------------- | -------------- |
  | 200    | OK                    | GET            |
  | 201    | CREATED               | POST/PUT/PATCH |
  | 204    | NO CONTENT            | DELETE         |
  | 400    | INVALID REQUEST       | POST/PUT/PATCH |
  | 404    | NOT FOUND             | *              |
  | 500    | INTERNAL SERVER ERROR | *              |

```
{
  'code': 0,
  'data': ''
}
```

## v1.3 评论和点赞
### 回答问题（添加答案）
#### 添加回答
+ 构造回答表单
+ 保存表单数据到Answer中，将写回答对话框变为富文本
+ 将回答提交到文章详情，并给Flash消息提示回答成功
### 首页答案列表
+ 在视图中准备数据（回答列表）
+ 在HTML模板中替换动态内容（列表循环）
+ 页面效果实现（概要信息显示及切换）
+ 分页的实现思路
### 评论、回复评论
+ 取评论列表数据，并用循环改造
+ 计算创建时间和现在时间的差值
+ 评论下的回复列表
### 异步加载评论列表
### 为评论点赞


## Refer
+ flask-login 
  * [源码](https://github.com/maxcountryman/flask-login)
  * [文档](https://flask-login.readthedocs.io/en/latest/)
+ flask-ckeditor
  * [源码](https://github.com/greyli/flask-ckeditor)
  * [文档](https://flask-ckeditor.readthedocs.io/en/latest/)


