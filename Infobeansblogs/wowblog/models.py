from wowblog import app,db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_login import current_user
import datetime

@login_manager.user_loader
def load_user(user_id):
    # if isinstance(current_user, AdminUser):
       # user = AdminUser.query.get(int(user_id))
    # else:
        user = User.query.get(int(user_id))
        return user



class User(db.Model, UserMixin):
    
    __tablename__ = 'users'

    id              = db.Column(db.Integer, primary_key=True)
    profile_image   = db.Column(db.String(64), nullable=False, default='default_profile.jpg')
    email           = db.Column(db.String(64), unique=True,index=True)
    username        = db.Column(db.String(64), unique=True, index=True)
    password_hash   = db.Column(db.String(128))

    post            = db.relationship('BlogPost',  backref='author', lazy=True)


    def __init__(self, email, username, password):
        self.email          = email
        self.username       = username
        self.password_hash  = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"Username {self.username}"



class BlogPost(db.Model):
    
    user        = db.relationship(User)

    id          = db.Column(db.Integer, primary_key=True)
    user_id     = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date        = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow())
    title       = db.Column(db.String(140), nullable=False)
    text        = db.Column(db.Text, nullable=False)
    bimg        = db.Column(db.String(200), nullable=True)



    def __init__(self, title, text, user_id,bimg):
        self.title      = title
        self.text       = text
        self.user_id    = user_id
        self.bimg = bimg
    
    def __repr__(self):
        return f"Post Id :  {self.id} Date: {self.date}"


class AdminUser(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(128), default='admin')

    def __init__(self, username, password):
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"Username {self.username}"

class Carousel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(128), nullable=False)
    cimg = db.Column(db.String(200), nullable=False)

    def __init__(self, title, desc,cimg):
        self.title = title
        self.desc = desc
        self.cimg = cimg

    def __repr__(self):
        return f"Carousel Title {self.title}"

    def image_url(self):
        return f'{app.config["UPLOAD_FOLDER"]}/{self.cimg}'

