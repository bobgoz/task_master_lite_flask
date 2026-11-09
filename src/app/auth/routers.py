"""Роутеры приложения auth (авторизация)."""

from flask import Blueprint, render_template

from .forms import LoginForm

router = Blueprint('auth', __name__)


@router.route('/login')
def login():
    """Эндпоинт входа."""
    form = LoginForm()
    # if form.validate_on_submit():
    return render_template('auth/login.html', form=form)
