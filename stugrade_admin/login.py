import mysql.connector
from flask import Flask,render_template,request,url_for,redirect,session,flash,current_app
from flask_bootstrap import Bootstrap
import traceback

app=Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = '123456'
# app.config.from_object('settings')

@app.route('/index',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/',methods=['GET','POST'])
def login():
    return render_template('login.html')

def Response_headers(content):    

    resp = Response(content)    

    resp.headers['Access-Control-Allow-Origin'] = '*'    

    return resp 

@app.route('/login')

def getLoginRequest():

#查询用户名及密码是否匹配及存在

    #连接数据库,此前在数据库中创建数据库TEST
    conn = mysql.connector.connect(user='root', password='Summer-2018', database='test')
    cursor = conn.cursor()
    
    uname=request.args.get('user')
    pwd=request.args.get('password')
    print(uname)
    
    sql = 'select * from user WHERE user=%s and password=%s'
 
    # try:

        # 执行sql语句
        
    cursor.execute(sql,[uname,pwd])
    results = cursor.fetchall()
    print(results)
    print(len(results))

    if len(results)==1:

        return render_template('success.html')

    else:

        return render_template('fail.html')

        # 提交到数据库执行

    conn.commit()
    
    # except:
    #     return '<h3>错误</h3>'

    # #     # 如果发生错误则回滚

    #     traceback.print_exc()

    #     conn.rollback()

    # 关闭数据库连接

    cursor.close()

@app.route('/addindex',methods=['GET','POST'])
def addindex():
    return render_template('add.html')
    

@app.route('/add')
def add():
    conn = mysql.connector.connect(user='root', password='Summer-2018', database='test')
    cursor = conn.cursor()
    if request.method!='POST':
        addnumber = request.args.get('id')
        sql1='select * from stuinfo where id=%s'
        cursor.execute(sql1,[addnumber])
        results1 = cursor.fetchall()
        print(len(results1))
        if len(results1)!=0:
            return "您输入的学号已存在"
        else:
            addname = request.args.get('stuname')
            addgrade1 = request.args.get('Chinese')
            addgrade2 = request.args.get('Math')
            addgrade3 = request.args.get('English')
            # adddepartment = request.form.get('adddepartment')
            if addname != None and addnumber != None:            #不为空则添加
                # conn = mysql.connector.connect(user='root', password='Summer-2018', database='test')
                # cursor = conn.cursor()
                sql = 'insert into stuinfo (id,name) values (%s,%s)'
                sql2 = 'insert into stugrade1 (id,Chinese,Math,English) values (%s,%s,%s,%s)'
                cursor.execute(sql,[addnumber, addname])
                cursor.execute(sql2,[addnumber, addgrade1, addgrade2, addgrade3])
                conn.commit()
                cursor.close() 
                return render_template('jump.html')
                
            else:
                return "输入错误" 
            
    else:
        return "gagag" 

@app.route('/delindex',methods=['GET','POST'])
def delindex():
    return render_template('del.html')
    

@app.route('/del')
def delete():
    conn = mysql.connector.connect(user='root', password='Summer-2018', database='test')
    cursor = conn.cursor()
    if request.method!='POST':
        delnumber = request.args.get('id')
        sql3='select * from stuinfo where id=%s'
        cursor.execute(sql3,[delnumber])
        results2 = cursor.fetchall()
        print(len(results2))
        if len(results2)==0:
            return "您输入的学号不存在"
        else:
            delname = request.args.get('stuname')
            # addgrade1 = request.args.get('Chinese')
            # addgrade2 = request.args.get('Math')
            # addgrade3 = request.args.get('English')
            # adddepartment = request.form.get('adddepartment')
            if delnumber != None:            #不为空则删除
                # conn = mysql.connector.connect(user='root', password='Summer-2018', database='test')
                # cursor = conn.cursor()
                sqldel = 'delete from stuinfo where id=%s'
                sqldel1='delete from stugrade1 where id=%s'
                cursor.execute(sqldel,[delnumber])
                cursor.execute(sqldel1,[delnumber])
                conn.commit()
                cursor.close() 
                return render_template('deljump.html')
                
            else:
                return "输入错误" 
            
    else:
        return "gagag" 



if __name__ == '__main__': 
   app.run(debug=True)