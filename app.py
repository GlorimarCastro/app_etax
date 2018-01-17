'''
Created on Jan 16, 2018

@author: galarwen
'''

from flask import Flask, flash, request
from flask import render_template
from flask.json import jsonify
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user, login_required


app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config['SECRET_KEY'] = 'SET T0 4NY SECRET KEY L1KE RAND0M H4SH'

@app.route('/')
def test():
    return 'Hello World'



'''
-----------------------------------------------------
            DASHBOAR                        DASHBOARD
-----------------------------------------------------
'''
@app.route('/dashboard', methods=['GET', 'POST'])
def home():
    return render_template("sideBar.html")

'''
-----------------------------------------------------
            LOGING                             LOGING
-----------------------------------------------------
'''
@app.route('/login')
def login():
    return render_template('example.html')

@app.route('/user_login', methods=['GET', 'POST'])
def user_Login():
    print 'entro'
    data = request.get_json(force=True)
    dude = User.get(data['email'])
    #print dude
    if (dude and dude.verify_password(data['password'])):
        print "IT got here \n\n"
        login_user(dude)
    else:
        flash('no')
        return jsonify({'data': "Email or password invalid."}), 400
    flash('You were logged in')
    return jsonify({'data': "you were logged in", 'home': '/dashboard'})

@app.route('/userLogout', methods=['POST'])
def user_Logout():
    logout_user()
    flash('You were logged out')
    return render_template('profile.html')


class UserNotFoundError(Exception):
    pass

class User(UserMixin): 
    users = []
    def __init__(self, id):
        
        
        self.users.append({'email': 'glorimar@etax.com', 'password': "1234", 'group': "admin"})
        self.users.append({'email': 'graciany@etax.com', 'password': "poop", 'group': "admin"})
        self.users.append({'email': 'gloribel@etax.com', 'password': "4567", 'group': "marketing"})
        self.users.append({'email': 'janiry@etax.com', 'password': "7896", 'group': "preparer"})
        
        if not any(user['email'] == id for user in self.users):
            print "not found"
            raise UserNotFoundError()
        self.id = id
        for x in self.users:
            if x['email'] == id:
                self.password = x['password']
                self.email = x['email']
                self.email = x['group']
                self.newImgUrl = ''
        #self.username = self.users['username']

    def verify_password(self, password):
        return self.password == password

    @classmethod
    def get(self_class, id):
        '''Return user instance of id, return None if not exist'''
        try:
            user = self_class(id)
            return user
        except UserNotFoundError:
            return None

@login_manager.user_loader
def user_loader(id):
    return User.get(id)   
        
if __name__ == '__main__':
    app.run()