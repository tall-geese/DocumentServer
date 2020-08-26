# Windows/Linux 
    # set/export FLASK_APP=DocServer
    # set/export FLASK_ENV=development
    # set/export DEVELOPMENT=1
    # set/export FLASK_RUN_PORT=8080

from flask import Flask, url_for, render_template, render_template_string
import DocServer.db as db
# import db

def create_app():
    app = Flask('DocServer')
    app.config.from_pyfile('configurations/testing_config.py')
    # app.config.from_pyfile('configurations/production_config.py')
    
    def testOutput():
        return "hello"

    documents = db.testConnection_Lin(app)

    @app.route('/')
    def index():
        return render_template('index.html', documents=documents)
    

    # @app.context_processor
    # def inject_function():
    #     def testOutput():
    #         print('this worked')
    #     return dict(func=testOutput)

    return app

if __name__ == ('__main__'):
    print('hit main')
    create_app()



