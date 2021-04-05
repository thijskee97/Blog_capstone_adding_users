from flask_wtf import FlaskForm
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")



class RegisterForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(message='Fill this shit')])
    password = PasswordField('password', validators=[DataRequired(message='Fill this shit')])
    name = StringField('name', validators=[DataRequired(message='Fill this shit')])
    submit = SubmitField('Sign me the Fuck up!')

class LoginForm(FlaskForm):
     email = StringField('email', validators=[DataRequired(message='Fill this shit')])
     password = PasswordField('password', validators=[DataRequired(message='Fill this shit')])
     submit = SubmitField('Sign me the Fuck in!')


class CommentForm(FlaskForm):
    comment = CKEditorField('lemme know what ya think', validators=[DataRequired()])
    submit = SubmitField('comment')
