# Windows/Linux 
    # set/export FLASK_APP=DocServer
    # set/export FLASK_ENV=development
    # set/export DEVELOPMENT=1
    # set/export FLASK_RUN_PORT=8080   <--- port 8080 forbidden on J76, occupied by former doc viewer

from flask import Flask, url_for, render_template, render_template_string, Response, send_file, abort, redirect
import DocServer.db as db

def create_app():
    app = Flask('DocServer')
    # app.config.from_pyfile('configurations/testing_config.py')  #IQS server / Unipoint Test Server
    app.config.from_pyfile('configurations/production_config.py')   #Unipoint Server
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


    @app.route('/')
    def index():
        documents = db.testConnection_Lin(app)
        return render_template('index.html', documents=documents)

    @app.route('/documents/<path:subpath>')
    def generate_file(subpath):
        try:
            print(subpath)
            return send_file(app.config.get('UNIPOINT_FILE_DIR') + subpath, as_attachment=False)
        except FileNotFoundError:
            abort(404)
        return redirect('/')


    return app
