from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.fields.html5 import EmailField, DateTimeField
from wtforms.validators import InputRequired, DataRequired, Email, EqualTo
import datetime

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
    subject = StringField("Тема", validators=[InputRequired(), DataRequired()])
    description = StringField("Описание", validators=[DataRequired()])
    date_start = DateTimeField("Дата начала", default=datetime.datetime.now(), format='%Y-%m-%d %H:%M:%S',
                               validators=[DataRequired(message="Не правильный формат даты")], )
    date_end = DateTimeField("Крайник срок", default=datetime.date.today(), format='%Y-%m-%d %H:%M:%S',
                             validators=[DataRequired(message="Не правильный формат даты")], )

    submit = SubmitField('Создать событие')
