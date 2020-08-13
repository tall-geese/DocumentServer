# Windows   
    # set FLASK_APP=doc_server.py
    # set FLASK_ENV=development
    # set DEVELOPMENT=1
    # set FLASK_RUN_PORT=8080

from flask import Flask, url_for, render_template, render_template_string
from sqlalchemy.engine import Engine, create_engine, Connection, ResultProxy

app = Flask(__name__)

@app.route('/')
def index():
    # render_template('index.html')
    return render_template_string('Hello David')