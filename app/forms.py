from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, DataRequired, Email, EqualTo


class CreateUserForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[InputRequired(), DataRequired()])
    email = EmailField('Электронная почта', validators=[InputRequired(), DataRequired(), Email()])
    password = PasswordField("Введите пароль", validators=[InputRequired(), DataRequired(),
                                                           EqualTo('password_confirm', message='Пароли не совпадают')])
    password_confirm = PasswordField("Подтвердите пароль", validators=[InputRequired(), DataRequired(),
                                                                       EqualTo('password',
                                                                               message='Пароли не совпадают')])
    submit = SubmitField('Зарегистрироваться')


class LoginForm(FlaskForm):
    email = EmailField('Электронная почта', validators=[InputRequired(), DataRequired(), Email()])
    password = PasswordField("Пароль", validators=[InputRequired(), DataRequired()])

    submit = SubmitField('Авторизоваться')


class EventForm(FlaskForm):
    pass
