"""Формы приложения task."""

from flask_wtf import FlaskForm
from wtforms import (
    BooleanField,
    IntegerField,
    StringField,
    SubmitField,
)


class TaskForm(FlaskForm):
    """Форма для управления задачами."""

    name = StringField('Имя')
    task = StringField('Задача')
    submit = SubmitField('Отправить')
