from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import  FileField, FileAllowed 


from flask_login import current_user
from wowblog.models import User


class LoginForm(FlaskForm):
    email    = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit   = SubmitField("Log in")



class RegistrationForm(FlaskForm):
    email        = StringField('Email', validators = [DataRequired(), Email()])
    username     = StringField('Username', validators=[DataRequired()])
    password     = PasswordField('Password', validators = [DataRequired(), EqualTo('pass_confirm', 'Password must match!')])
    pass_confirm = PasswordField('Confirm Password', validators = [DataRequired()])
    submit       = SubmitField('Register!')


    def check_email(self, field):

        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Your email already registered!")
        
    
    def check_username(self, field):
        
        if User.query.filter_by(username = field.data).first():
            raise ValidationError("Username already taken by someone else!")
    



class UpdateUserForm(FlaskForm):
    email        = StringField('Email', validators = [DataRequired(), Email()])
    username     = StringField('Username', validators=[DataRequired()])
    picture      = FileField("Update Profile Picture ", validators=[FileAllowed(['jpg','png','jpeg'])])
    submit       = SubmitField('Update!')

    def check_email(self, field):

        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Your email already registered!")
        
    
    def check_username(self, field):
        
        if User.query.filter_by(username = field.data).first():
            raise ValidationError("Username already taken by someone else!")