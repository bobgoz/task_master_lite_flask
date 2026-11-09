"""Роутеры приложения task."""

from flask import Blueprint, render_template, redirect, url_for

from .forms import TaskForm

router = Blueprint('task', __name__)


@router.route('/add', methods=['GET', 'POST'])
def add_task():
    """Добавить задачу."""
    form = TaskForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('add_task.html', form=form)
