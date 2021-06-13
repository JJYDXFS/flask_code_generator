"""
Flask 常用代码 生成器
"""
def choice_menu():
    """
    选项菜单页
    """
    print("---------------------------------------------------------------")
    print("在以下选项中选择一个demo：")
    print("1. basic flask demo",end="\t\t")
    print("2. get demo")
    print("3. post demo",end="\t\t\t")
    print("4. render demo")
    print("5. mysql demo (pymysql)",end="\t\t")
    print("6. 退出 EXIT")

def flask_template():
    """
    基础flask模板
    """
    template="""
from flask import Flask, request, render_template, jsonify, redirect
from flask_cors import *
import pymysql
import json
import copy

# 指定静态文件目录
app = Flask(__name__,static_url_path='/static/',template_folder='templates')
# 允许跨域访问
CORS(app, resources=r'/*')

# 主页
@app.route('/')
def index():
    return "Hi Flask!"

if __name__ == '__main__':
    app.debug=True  # 默认开启debug模式
    # host=0.0.0.0 port=5000
    app.run('0.0.0.0', 5000)
"""
    print(template)

def get_demo():
    """
    GET接口模板
    """
    name=input("请输入GET接口名称：")
    template="""
@app.route('/api/{name}', methods=['GET'])
def {name}():
    '''
    {name}
    '''
    # request.args.get 用于获取GET所传参数
    value=request.args.get('key')
    
    return json.dumps({{'result':'success'}},ensure_ascii=False)
""".format(name=name)

    print(template)

def post_demo():
    """
    POST接口模板
    """
    name=input("请输入POST接口名称：")
    post_template="""
@app.route('/api/{name}', methods=['POST'])
def {name}():
    '''
    {name}
    '''
    value=request.form['key'] # 获取表单中的参数
    # img = request.files['file']   # 获取表单中的文件
    
    return json.dumps({{'result':'success'}},ensure_ascii=False)    
""".format(name=name)

    print(post_template)

def mysql_damo():
    '''
    pymysql操纵MySQL demo
    '''
    connect_template="""
db = pymysql.connect(host='主机ip', 
                    user='用户名',
                    password='密码',
                    database='数据库名',
                    cursorclass=pymysql.cursors.DictCursor)
"""

    mysql_template=connect_template+"""
cursor = db.cursor()    # 创建一个游标对象

sql=\"\"\"要执行的SQL语句;\"\"\"

cursor.execute(sql) # 执行语句
data=cursor.fetchall()  # 获取字典形式查询结果 .fatchone()方法获取单条数据
db.close() # 关闭连接
"""
    print(mysql_template)


def render_demo():
    '''
    模板渲染demo
    '''
    name=input("输入路由的名字：")
    render_template="""
@app.route('/{name}')
def {name}():
    '''
    {name}
    '''
    key='hi'    # 传给模板的参数

    # return redirect('http://www.baidu.com') # 重定向到任意url
    return render_template("html-template-name.html",title = key)   # 静态文件渲染模板样式并传参
""".format(name=name)

    print(render_template)

def bye():
    print("Bye!")
    exit(0)

def default():
    print("序号输入有误")

switch = {'1': flask_template,
    '2': get_demo,
    '3': post_demo,
    '4': render_demo,
    '5': mysql_damo,
    '6': bye,
}

if __name__=="__main__":
    print("-----------------欢迎来到flask代码傻瓜生成器！-----------------")
    print("----------Welcome to naive demo generator for flask----------")
    while True:
        choice_menu()
        choice = input("请输入demo序号：")
        print("---------------------------------------------------------------")
        switch.get(choice, default)()