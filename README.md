# Flask 常用代码 生成器

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)



因为 [Flask](https://flask.palletsprojects.com/en/2.0.x/) 使用方便，总会时不时用它进行一些后端开发。但每次代码都基本是固定的格式，想用时就要打开笔记里或者以前开发的项目里Ctrl C + Ctrl V。觉得有点麻烦  



所以编一个傻瓜代码生成器吧，把经常会用到的demo写进去。用的时候直接生成似乎就方便一些  



目前收录demo如下

\- basic flask demo | 最基础的flask模板，可直接运行

\- get demo | GET接口模板，附带一个获取参数的方法

\- post demo | POST接口模板，附带一个获取文件的方法

\- render demo | 渲染页面模板，附带一个重定向demo

\- mysql damo (pymysql) | 基于pymysql库，参考[PyMySQL’s documentation](https://pymysql.readthedocs.io/en/latest/index.html)

## 运行示例

![2021-06-09_113448](https://jjydxfs.oss-cn-beijing.aliyuncs.com/md/2021-06-09_113448.jpg)

---

## MySQLDB
为 pymysql 的查询封装了一个 MySQLDB 类，便于重复使用   
```python
import pymysql
from MySQLDB import MySQLDB
# 使用时先新建一个实例
db_mysql = MySQLDB(host='localhost',
                user='root',
                password='password',
                database='mysql')
# 定义sql查询语句
sql1="""set @var = 1;"""
sql2="""select * from user;"""
# 向 MySQLDB 实例的.query()方法传递要执行的sql语句列表
# 将以字典形式返回 顺序执行后列表中sql语句 的查询结果
print(db_mysql.query([sql1,sql2]))
```