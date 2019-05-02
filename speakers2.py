
from flask import Flask, render_template,redirect,request,session, url_for, request
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
import requests
import logging
from datetime import timedelta

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = ''
app.config['SECRET_KEY'] = "lkkajdghdadkglajkgah"
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(hours=1)

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

class User(UserMixin):
  def __init__(self,id):
    self.id = id



logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('Init')

@app.route('/')
def status():
    if current_user.is_authenticated:	
	session.modified = True
    	logging.warning('Main Page')
    	uri = 'http://10.68.54.23:8000/room_status/'
    	r = requests.get(uri)
    	b = r.json()
    	status=r.status_code  
	session.ip_address = request.remote_addr
	print session.ip_address 
    	return render_template('index1.html', test = b )
    else: 
	return render_template('login.html', error_msg = " ")	

@app.route('/on/<room_on>')
def on(room_on):
    if current_user.is_authenticated:
	session.modified = True
    	uri = 'http://10.68.54.23:8000/room_on/' + room_on
    	r = requests.get(uri)
    	b = r.json()
    	status=r.status_code
    	return render_template('index1.html', test = b )
    else:
	return render_template('login.html', error_msg = " ")	

@app.route('/off/<room_off>')
def off(room_off):
    if current_user.is_authenticated:
	session.modified = True
    	uri = 'http://10.68.54.23:8000/room_off/' + room_off
    	r = requests.get(uri)
    	b = r.json()
    	status=r.status_code
    	return render_template('index1.html', test = b)
    else:
	return render_template('login.html', error_msg = " ")


@app.route('/login/')
def login():
    if current_user.is_authenticated:
	session.modified = True
        return redirect(url_for('status'))
    else:
    	#login_user(User(1))
    	return redirect(url_for('status'))

@app.route('/logout/')
def logout():
    if current_user.is_authenticated:	
    	logout_user()
    return render_template('login.html', error_msg = " ")
    
 
@app.route('/validate/', methods=['POST'])
def validate():

    error_msg = " "	
    if current_user.is_authenticated:	
	session.modified = True
    	return redirect(url_for('status'))
    else:
	
	
	
	username = request.form['UserName']
        password = request.form['Password']

	if not username  or not password:
		
		return render_template('login.html', error_msg = "User Name or Password Can Not Be Blank")
	
        


	uri = 'http://10.68.54.23:8000/validate_user/' + username + "/" + password
    	r = requests.get(uri)
    	b = r.json()
    	status=r.status_code
        user_id = b['id']
        user_authorized = b['Authorized']



	
	if user_authorized == "Y":
                user_id = int(user_id) 
		login_user(User(user_id))
                return redirect(url_for('status'))
	else:
		return render_template('login.html', error_msg = "Invlaid User Name or Password")
        





if __name__ == '__main__':
    #app.run(host= '10.68.54.4')
    app.run(host= '0.0.0.0')
    ## app.run()
