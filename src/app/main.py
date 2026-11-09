"""Главное управление приложением."""

from flask import Flask, render_template

from app.auth.routers import router as auth_router
from app.config import config
from app.task.routers import router as task_router

app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(auth_router)
app.register_blueprint(task_router)
print(app.config)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
