from flask import Flask, render_template, request
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name = name)

@app.route('/login', methods=['GET', 'POST'])
@app.route('/login/<user>')
def login(user = ''):
	if request.method == 'POST':
	    username = request.json['name']
	    #userage = request.json['age']
	    #return "user: %s, age: %s" % (username, userage)
	    return username
	else:
		return render_template('login.html', user = user)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
 
if __name__ == '__main__':
    manager.run()