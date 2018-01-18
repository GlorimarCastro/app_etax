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
    return render_template("index.html")



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
            PROJECT                           PROJECT 
-----------------------------------------------------
'''
class Projects: 
    projects = []
    
    
    projects.append({'owner': 'glorimar@etax.com', 'members': ['glorimar@etax.com', 'janire@etax.com'], 'deadline': "5-20-18", 
                              'importance': 'high', 'tasks': [], 'type': "marketing", 'name': 'project1', 'description': 'prueba 1', 'completed': 'False'})
    projects.append({'owner': 'graciany@etax.com', 'members': ['graciany@etax.com', 'glorimar@etax.com', 'janire@etax.com'], 'deadline': "8-20-18", 
                              'importance': 'low', 'tasks': [], 'type': "marketing", 'name': 'project 2', 'description': 'prueba 2', 'completed': 'False'})
    projects.append({'owner': 'graciany@etax.com', 'members': ['graciany@etax.com', 'glorimar@etax.com', 'janire@etax.com'], 'deadline': "6-20-18", 
                              'importance': 'high', 'tasks': [], 'type': "marketing", 'name': 'project3', 'description': 'prueba 3', 'completed': 'False'})
    projects.append({'owner': 'graciany@etax.com', 'members': ['graciany@etax.com', 'glorimar@etax.com', 'janire@etax.com', 'gloribel@etax.com'], 'deadline': "3-20-18", 
                              'importance': 'medium', 'tasks': [], 'type': "marketing", 'name': 'project4', 'description': 'prueba 4', 'completed': 'False'})
        
        
    def __init__(self, project_name):
        pass

    @classmethod
    def get(self, project_name):
        user_projects = {}
        '''Return project instance of project_name, return None if not exist'''
        try:
            user_projects['name'] = project_name
            for x in self.projects:
                if x['name'] == project_name:
                    user_projects['owner']       = x['owner']
                    user_projects['members']     = x['members']
                    user_projects['deadline']    = x['deadline']
                    user_projects['importance']  = x['importance']
                    user_projects['tasks']       = x['tasks']
                    user_projects['type']        = x[ 'type']
                    user_projects['description'] = x['description']
                    user_projects['completed']   = x['completed']
        #self.username = self.users['username']
            return user_projects
        except UserNotFoundError:
            return None
    
    @classmethod
    def getAllForUser(self, user_email):
        user_projects = []
        '''Return project instance of project_name, return None if not exist'''
        try:
            for x in self.projects:
                if x['owner'] == user_email:
                    user_projects.append(x)
        #self.username = self.users['username']
            return user_projects
        except UserNotFoundError:
            return None
        


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
        
        
        self.users.append({'email': 'glorimar@etax.com', 'password': "1234", 'group': "admin", 'name': "glorimar"})
        self.users.append({'email': 'graciany@etax.com', 'password': "poop", 'group': "admin", 'name': "graciany"})
        self.users.append({'email': 'gloribel@etax.com', 'password': "4567", 'group': "marketing", 'name': "gloribel"})
        self.users.append({'email': 'janire@etax.com', 'password': "7896", 'group': "preparer", 'name': "janire"})
        
        if not any(user['email'] == id for user in self.users):
            print "not found"
            raise UserNotFoundError()
        self.id = id
        for x in self.users:
            if x['email'] == id:
                self.password = x['password']
                self.email = x['email']
                self.group = x['group']
                self.name  = x['name']
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