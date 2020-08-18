# Windows   
    # set FLASK_APP=DocServer
    # set FLASK_ENV=development
    # set DEVELOPMENT=1
    # set FLASK_RUN_PORT=8080

from flask import Flask, url_for, render_template, render_template_string



def create_app():
    app = Flask('DocServer')
    app.config.from_pyfile('configurations/testing_config.py')
    app.config.from_pyfile('configurations/production_config.py')

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.context_processor
    def inject_function():
        def try_something():
            print([1,23,4,5])
        return dict(func=try_something)

    return app

