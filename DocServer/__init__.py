# Windows   
    # set FLASK_APP=DocServer
    # set FLASK_ENV=development
    # set DEVELOPMENT=1
    # set FLASK_RUN_PORT=8080

from flask import Flask, url_for, render_template, render_template_string
from sqlalchemy.engine import Engine, create_engine, Connection, ResultProxy



def create_app():
    app = Flask('DocServer')

    @app.route('/')
    def index():
        return render_template('index.html')

    return app

