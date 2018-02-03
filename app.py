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

current_projects = {}



'''
-----------------------------------------------------
            DASHBOAR                        DASHBOARD
-----------------------------------------------------
'''


'''
-----------------------------------------------------
            PROJECT                           PROJECT 
-----------------------------------------------------
'''
@app.route('/projects')
@app.route('/')
@login_required
def projects_view():
    return render_template("index.html")

class Emails:
    emails = []
    emails.append({'location': ['pr'], 'gender': ['other'], 'client_type': ['accountants'], 'email_attachments': 'false', 'email_text': 'true', 'id': '1' })
    
    def __init__(self, project_name):
        pass
    
    @classmethod
    def getById(self, id):
        for x in self.emails:
            if x['id'] == id:
                return x
    
    @classmethod
    def addSettings(self, data):
        temp = {}
        x = data
        temp2 = []
        print x
        for j in x['location']:
            temp2.append(j.encode("utf-8"))
        temp['location'] = temp2
            
        temp2 =[]
        for j in x['gender']:
            temp2.append(j.encode("utf-8"))
        temp['gender'] = temp2
            
        temp2 =[]
        for j in x['client_type']:
            temp2.append(j.encode("utf-8"))
        temp['client_type'] = temp2
            
        temp['email_attachments'] = x[ 'email_attachments'].encode("utf-8")
        temp['email_text'] = x[ 'email_text'].encode("utf-8")
        print x[ 'id']
        temp['id'] = x[ 'id'].encode("utf-8")
            
            
        
        self.emails.append(temp)
        

@app.route('/getemaildata/<id>', methods=['GET'])
def get_email_data(id):
    print "getting email"
    print id
    data = Emails.getById( id)
    print data
    return jsonify(data), 200

@app.route('/addSettings', methods=['POST'])
def add_settings():
    data = request.get_json(force=True)
    Emails.addSettings(data)
    print Emails.emails
    return ('se anadio')
           
    
class Projects: 
    projects = []
    
    project_id_flag = 4
    
    
    projects.append({'owner': 'glorimar@etax.com', 'members': ['glorimar@etax.com', 'janire@etax.com'], 'deadline': "May-20-18", 'id': '1',
                              'members_profile_pic': ['static/img/glorimar.jpg', 'static/img/Janire.jpg'], 'month_num': '05',
                              'media_channel': ['facebook', 'email'], 'person_to_approve': 'Gloribel',
                              'importance': 'high', 'tasks': [], 'type': "marketing", 'name': 'Consejo Tributario 2018', 'description': 'prueba 1', 'completed': 'False'})
    projects.append({'owner': 'graciany@etax.com', 'members': ['graciany@etax.com', 'glorimar@etax.com', 'janire@etax.com'], 'deadline': "Aug-20-18",  'id': "2",
                              'members_profile_pic': ['static/img/glorimar.jpg', 'static/img/graciany2', 'static/img/Janire.jpg'], 'month_num': '08',
                              'media_channel': ['facebook', 'email'],'person_to_approve': 'Gloribel',
                              'importance': 'low', 'tasks': [], 'type': "marketing", 'name': 'Comienzo de Temporada', 'description': 'prueba 2', 'completed': 'False'})
    projects.append({'owner': 'graciany@etax.com', 'members': ['graciany@etax.com', 'glorimar@etax.com', 'janire@etax.com'], 'deadline': "Jun-20-18",  'id': "3",
                              'members_profile_pic': ['static/img/glorimar.jpg', 'static/img/graciany2', 'static/img/Janire.jpg'], 'month_num': '06',
                              'media_channel': ['facebook', 'email'], 'person_to_approve': 'Gloribel',
                              'importance': 'high', 'tasks': [], 'type': "marketing", 'name': 'Seminario Etica', 'description': 'prueba 3', 'completed': 'False'})
    projects.append({'owner': 'graciany@etax.com', 'members': ['graciany@etax.com', 'glorimar@etax.com', 'janire@etax.com', 'gloribel@etax.com'], 'deadline': "Mar-20-18", 'id': "4",
                              'members_profile_pic': ['static/img/glorimar.jpg', 'static/img/graciany2', 'static/img/Janire.jpg', 'static/img/Gloribel.jpg'],
                              'media_channel': ['facebook', 'email'], 'month_num': '03', 'person_to_approve': 'Gloribel',
                              'importance': 'medium', 'tasks': [], 'type': "marketing", 'name': 'Seminario Cambios Contributivos', 'description': 'prueba 4', 'completed': 'False'})
        
        
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
                    user_projects['id']          = x['id']
                    user_projects['month_num']          = x['month_num']
                    user_projects['media_channel'] = x['media_channel']
                    user_projects['person_to_approve'] = x['person_to_approve']
                    
        #self.username = self.users['username']
            return user_projects
        except UserNotFoundError:
            return None
    @classmethod
    def getByID(self, id):
        user_projects = {}
        '''Return project instance of project_name, return None if not exist'''
        try:
            user_projects['id'] = id
            print "esto es lo que buscas"
            print self.projects
            for x in self.projects:
                if x['id'] == id:
                    user_projects['name']       = x['name']
                    user_projects['owner']       = x['owner']
                    user_projects['members']     = x['members']
                    if  x['deadline'] != "":
                        user_projects['deadline']    = '20' + x['deadline'][7:9] + '-' + x['month_num'] + '-' + x['deadline'][4:6]
                    else:
                        user_projects['deadline'] = ""
                    user_projects['importance']  = x['importance']
                    user_projects['tasks']       = x['tasks']
                    user_projects['type']        = x[ 'type']
                    user_projects['description'] = x['description']
                    user_projects['completed']   = x['completed']
                    user_projects['id']   = x['id']
                    user_projects['media_channel'] = x['media_channel']
                    user_projects['person_to_approve'] = x['person_to_approve']
                    temp_name = []
                    for u in x['members']:
                        temp_name.append(User.getNameFromEmail( u))
                    user_projects['members_name'] = temp_name
        #self.username = self.users['username']
            return user_projects
        except UserNotFoundError:
            return None
    @classmethod
    def addProject(self, project_data):
        temp_json = {'owner': current_user.email, 'person_to_approve': project_data['person_to_approve'].encode("utf-8"),
                    'importance':  project_data['importance'].encode("utf-8"), 'tasks': [], 'type': "marketing", 'name':  project_data['name'].encode("utf-8"), 'description':  project_data['description'].encode("utf-8"), 'completed': 'False'
        }
        
        temp_media = []
        for c in  project_data['media_channel']:
            temp_media.append(c.encode("utf-8"))
        temp_json['media_channel'] = temp_media
        temp_pic = [];
        for m in project_data['members']:
            temp_pic.append('static/img/' + m.encode("utf-8") + '.jpg')
        temp_json['members_profile_pic'] = temp_pic
        
        temp_members = []
        for m in project_data['members']:
            temp_members.append(User.getEmailFromName(m.encode("utf-8")))
            
        already_in = False
        for m in temp_members:
            if m == current_user.email:
                already_in = True
        if not already_in:
            temp_members.append(current_user.email)
            temp_pic.append('static/img/' + current_user.name + '.jpg')
            
        temp_json['members'] = temp_members
        temp_json['id'] = str(Projects.project_id_flag + 1);
        Projects.project_id_flag += 1
        temp_json['members_profile_pic'] = temp_pic
        
        if project_data['deadline'] == "":
            temp_json['deadline']  = ""
        else:
            months = ["", "Jan", "Feb",'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            print 
            temp_json['deadline'] = months[int(project_data['deadline'][5:7].encode("utf-8"))] + '-' + project_data['deadline'][8:10].encode("utf-8") + "-" + project_data['deadline'][2:4].encode("utf-8")
            temp_json['month_num'] = project_data['deadline'][5:7].encode("utf-8")
        
        self.projects.append(temp_json)
        print self.projects
    
    @classmethod
    def editProject(self, project_data):
        temp_json = {'owner': current_user.email, 'person_to_approve': project_data['person_to_approve'].encode("utf-8"),
                    'importance':  project_data['importance'].encode("utf-8"), 'tasks': [], 'type': "marketing", 'name':  project_data['name'].encode("utf-8"), 'description':  project_data['description'].encode("utf-8"), 'completed': 'False'
        }
        
        temp_media = []
        for c in  project_data['media_channel']:
            temp_media.append(c.encode("utf-8"))
        temp_json['media_channel'] = temp_media
        temp_pic = [];
        for m in project_data['members']:
            temp_pic.append('static/img/' + m.encode("utf-8") + '.jpg')
        temp_json['members_profile_pic'] = temp_pic
        
        temp_members = []
        for m in project_data['members']:
            temp_members.append(User.getEmailFromName(m.encode("utf-8")))
            
        already_in = False
        for m in temp_members:
            if m == current_user.email:
                already_in = True
        if not already_in:
            temp_members.append(current_user.email)
            temp_pic.append('static/img/' + current_user.name + '.jpg')
            
        temp_json['members'] = temp_members
        temp_json['id'] = project_data['id'].encode("utf-8");
        Projects.project_id_flag += 1
        temp_json['members_profile_pic'] = temp_pic
        
        if project_data['deadline'] == "":
            temp_json['deadline']  = ""
        else:
            months = ["", "Jan", "Feb",'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            print 
            temp_json['deadline'] = months[int(project_data['deadline'][5:7].encode("utf-8"))] + '-' + project_data['deadline'][8:10].encode("utf-8") + "-" + project_data['deadline'][2:4].encode("utf-8")
            temp_json['month_num'] = project_data['deadline'][5:7].encode("utf-8")
        
        self.deleteProject(temp_json['id'])
        self.projects.append(temp_json)
        print self.projects   
       
    @classmethod
    def deleteProject(self, id):
        for p in self.projects:
            if p['id'] == id:
                self.projects.remove(p)
                
    @classmethod
    def getAllOwnerByUser(self, user_email):
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
        
    @classmethod
    def getAllForUser(self, user_email):
        user_projects = []
        '''Return project instance of project_name, return None if not exist'''
        try:
            for x in self.projects:
                for h in x['members']:
                    if h == user_email:
                        x['current_user'] = current_user.email
                        x['current_user_name'] = current_user.name
                        user_projects.append(x)
        #self.username = self.users['username']
            return user_projects
        except UserNotFoundError:
            return None

@app.route('/addNewProject', methods=['POST'])
def add_new_project():
    data = request.get_json(force=True)
    Projects.addProject( data)
    return ('se anadio')   

@app.route('/editProject', methods=['POST'])
def edit_project():
    data = request.get_json(force=True)
    Projects.editProject( data)
    return ('se anadio')      





@app.route('/deleteProject', methods=['POST'])
def delete_project():
    data = request.get_json(force=True)
    print "deleting project " + data['id']
    Projects.deleteProject( data['id'])
    return ('se borro') 




@app.route('/getProjectData/<id>', methods=['GET'])
def getProjectData(id):
    print "getting project"
    data = Projects.getByID( id.replace("u'", ""))
    print id.replace("u'", "")
    print data
    return jsonify(data), 200


@app.route('/project')
def getProjectView():
    project_name = request.args.get('name')
    project_id   = request.args.get('id')
    current_projects[current_user.email] = project_id
    return render_template('project.html')

@app.route('/getProjectInView')
def getProjectInView():
    temp = Projects.getByID(current_projects[current_user.email].encode("utf-8"))
    temp['current_user'] = current_user.email
    print temp
    return jsonify(temp), 200
 
 
 
@app.route('/help')
def help_view():
    return render_template('help2.html')
'''
-----------------------------------------------------
            QUERIES                           QUERIES
-----------------------------------------------------
'''
@app.route('/getProjectsForUser',  methods=['GET'])
def getProjectsForUser():
    user_in_session = current_user.email
    return jsonify(Projects.getAllForUser(user_in_session)), 200

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
    data = request.get_json(force=True)
    dude = User.get(data['email'])
    #print dude
    if (dude and dude.verify_password(data['password'])):
        login_user(dude)
    else:
        flash('no')
        return jsonify({'data': "Email or password invalid."}), 400
    flash('You were logged in')
    return jsonify({'data': "you were logged in", 'home': '/projects'})

@app.route('/userLogout', methods=['GET'])
def user_Logout():
    logout_user()
    flash('You were logged out')
    return render_template('example.html')


class UserNotFoundError(Exception):
    pass

class User(UserMixin): 
    users = []
    def __init__(self, id):
        
        
        self.users.append({'email': 'glorimar@etax.com', 'password': "1234", 'group': "admin", 'name': "Glorimar", 'current_project': "null"})
        self.users.append({'email': 'graciany@etax.com', 'password': "poop", 'group': "admin", 'name': "Graciany", 'current_project': "null"})
        self.users.append({'email': 'gloribel@etax.com', 'password': "4567", 'group': "marketing", 'name': "Gloribel", 'current_project': "null"})
        self.users.append({'email': 'janire@etax.com', 'password': "7896", 'group': "preparer", 'name': "Janire", 'current_project': "null"})
        self.users.append({'email': 'fabiola@etax.com', 'password': "7896", 'group': "marketing", 'name': "Fabiola", 'current_project': "null"})
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
                self.current_project = x['current_project']
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
    
    @classmethod
    def getEmailFromName(self, name):
        for x in self.users:
            if x['name'] == name:
                return x['email']
    @classmethod
    def getNameFromEmail(self, email):
        for x in self.users:
            if x['email'] == email:
                return x['name']

@login_manager.user_loader
def user_loader(id):
    return User.get(id)   
        
if __name__ == '__main__':
    app.run()