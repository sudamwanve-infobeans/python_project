import os
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)


############### DB Setup ###################

app.config['SECRET_KEY'] = 'mysecretkey'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'


from wowblog.core.views import core
from wowblog.users.views import users
from wowblog.blogpost.views import blogpost
from wowblog.error_pages.handlers import error_pages
from wowblog.admin.views import admin

app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(blogpost)
app.register_blueprint(error_pages)
app.register_blueprint(admin)