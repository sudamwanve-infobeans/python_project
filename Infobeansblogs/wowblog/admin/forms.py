from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, PasswordField,TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wowblog.models import AdminUser


class AdminLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField("Log in")


class AdminRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', 'Password must match!')])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register!')

    def check_username(self, field):

        if AdminUser.query.filter_by(username=field.data).first():
            raise ValidationError("Username already taken by someone else!")

class CarouselForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    desc =  TextAreaField('Description', validators=[DataRequired()])
    cimg = StringField('Image URL', validators=[DataRequired()])
    submit = SubmitField('Submit')

