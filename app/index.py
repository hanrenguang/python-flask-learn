from flask import Flask, render_template, request, json, session, url_for, escape
from flask_script import Manager
from flask_bootstrap import Bootstrap
import pymysql, time, threading
from flask_sockets import Sockets

app = Flask(__name__)
# manager = Manager(app)
bootstrap = Bootstrap(app)

# 多线程
# class myThread (threading.Thread):
#     def __init__(self, func, fg):
#         threading.Thread.__init__(self)
#         self.func = func
#         self.flag = fg
#     def run(self):
#        # 获得锁，成功获得锁定后返回True
#        # 可选的timeout参数不填时将一直阻塞直到获得锁定
#        # 否则超时后将返回False
#         threadLock.acquire()
#         self.func()
#         # 释放锁
#         threadLock.release()

# # def print_time():
# #     time.sleep(10)

# threadLock = threading.Lock()
# threads = []
# flag = 0

# # Home
# @app.route('/')
# @app.route('/index')
# def index():
#     global flag
#     flag = flag + 1
#     thread = myThread(index_func, flag)
#     thread.start()
#     threads.append(thread)
#     for t in threads:
#     	t.join()
#     	print(t.flag)
#     	return render_template('index.html')

# def index_func():
# 	time.sleep(10)

# Home
@app.route('/', methods=['GET'])
def index():
    if 'username' in session:
        return render_template('hello.html', user = escape(session['username']))
    return render_template('index.html')

# hello page
@app.route('/user', methods=['GET'])
def user():
	if 'username' in session:
	    return render_template('websocket.html', user = escape(session['username']))
	return render_template('unregistered.html')

# login api
@app.route('/login', methods=['POST'])
def login():
	if request.method == 'POST':
	    username = request.json['username'].strip(' ')
	    password = request.json['password']

	    if username == '':
	    	return json.jsonify(success=False,
	    		                msg='用户名不能为空')

	    connection = pymysql.connect(host='localhost', user='root', password='hrg', db='flaskapp')
	    cursor = connection.cursor()
	    try:
	    	sql = "SELECT `username`, `password`, `level` FROM `admin` WHERE `username`=%s"
	    	temp = cursor.execute(sql, (username,))
	    	if temp == 0:
	    		return json.jsonify(success=False,
	    			                msg='用户不存在')
	    	
	    	result = cursor.fetchone()
	    finally:
	    	connection.close()

	    if password != result[1]:
	    	return json.jsonify(success=False,
	    		                msg='密码错误')

	    session['username'] = username
	    return json.jsonify(success=True,
	    	                username=username)


# logout api
@app.route('/logout', methods=['POST'])
def log_out():
	session.pop('username', None)
	return json.jsonify(success=True)

# websocket test
@app.route('/websocket')
def websocket(ws):
	while True: 
		message = ws.receive()
		print(message)
		ws.send("帅哥")

# 404 NOT FOUND
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


app.secret_key = '\xb7>M{Yd\xa4\xe6(\xd8;\x00\x1c\xac\x8d\xbb\xe6\x7f\xa3\xe5\xd3[\x04\x8d'
 
if __name__ == '__main__':
    app.run(debug=True)