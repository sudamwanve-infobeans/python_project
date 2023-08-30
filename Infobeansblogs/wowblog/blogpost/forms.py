from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, TextAreaField,FileField

from wtforms.validators import DataRequired


class BlogPostForm(FlaskForm):
    
    title   =  StringField('Title', validators=[DataRequired()])
    text    =  TextAreaField('Text', validators=[DataRequired()])
    bimg = FileField('Image')
    submit  = SubmitField("Post")