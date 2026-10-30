"""Главное управление приложением."""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add')
def add_task():
    """Добавить задачу."""
    return render_template('add_task.html')


if __name__ == '__main__':
    app.run(debug=True)