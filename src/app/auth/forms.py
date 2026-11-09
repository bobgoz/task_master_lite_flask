"""Формы для аутентификации."""

from flask_wtf import FlaskForm
from wtforms import (
    BooleanField,
    PasswordField,
    StringField,
    SubmitField,
)
from wtforms.validators import data_required

ERROR_MESSAGE = 'Это поле обязательно.'


class LoginForm(FlaskForm):
    """Форма для входа."""

    username = StringField('Имя пользователя', validators=[data_required(ERROR_MESSAGE)])
    password = StringField('Пароль', validators=[data_required(ERROR_MESSAGE)])
    submit = SubmitField('Войти')
