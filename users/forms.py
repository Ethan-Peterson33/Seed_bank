from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from seed_bank.models import User


class RegistrationForm(FlaskForm):
    username = StringField("Username",
                            validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField("Email", validators=[DataRequired(), Email()])

    password = PasswordField('Passsord', validators=[DataRequired()])

    confirm_password = PasswordField('Confirm Passsord', validators=[DataRequired(),
                                                                    EqualTo('password')])
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user =  User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError("That username is taken. Please use a different one. ")

    def validate_email(self, email):
        email =  User.query.filter_by(email=email.data).first()

        if email:
            raise ValidationError("That email is taken. Please use a different one. ")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])

    password = PasswordField('Passsord', validators=[DataRequired()])

    remember = BooleanField("Remember Me")
    submit = SubmitField("Sign Up")

class UpdateAccountForm(FlaskForm):
    username = StringField("Username",
                            validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField("Email", validators=[DataRequired(), Email()])

    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png'])])

    submit = SubmitField("Update")

    def validate_username(self, username):
        if username.data != current_user.username:
            user =  User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError("That username is taken. Please use a different one. ")

    def validate_email(self, email):
        if email.data != current_user.email:
            email =  User.query.filter_by(email=email.data).first()
            if email:
                raise ValidationError("That email is taken. Please use a different one. ")

class RequestResetForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user =  User.query.filter_by(email=email.data).first()

        if user is None:
            raise ValidationError("There is no account with that email.  You must register first! ")

class ResetPasswordForm(FlaskForm):
        password = PasswordField('Passsord', validators=[DataRequired()])

        confirm_password = PasswordField('Confirm Passsord', validators=[DataRequired(),
                                                                        EqualTo('password')])
        submit = SubmitField('Reset Password')

class LibraryForm(FlaskForm):
    species = StringField("Species", validators=[DataRequired()])
    amount = StringField("Amount", validators=[DataRequired()])
    age = StringField("Age")
    picture = FileField('Picture of Seeds', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField("Add")
