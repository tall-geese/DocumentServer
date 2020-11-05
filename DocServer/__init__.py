# Windows/Linux 
    # set/export FLASK_APP=DocServer
    # set/export FLASK_ENV=development
    # set/export DEVELOPMENT=1
    # set/export FLASK_RUN_PORT=8080   <--- port 8080 forbidden on J76

from flask import Flask, url_for, render_template, render_template_string, Response, send_file, abort, redirect
import DocServer.db as db
import os
# import db

def create_app():
    app = Flask('DocServer')
    app.config.from_pyfile('configurations/testing_config.py')
    # app.config.from_pyfile('configurations/production_config.py')
    

    documents = db.testConnection_Lin(app)

    @app.route('/')
    def index():
        fileList = os.listdir(app.config.get('UNIPOINT_FILE_DIR'))
        fileList.extend([app.config.get('UNIPOINT_FILE_DIR')+'\\SAMPLE 1_A.docx'])
        return render_template('index.html', documents=documents, something=fileList)

    @app.route('/sample.git')
    def generate_file():
        try:
            return send_file(app.config.get('UNIPOINT_FILE_DIR')+'\\Git.pdf', as_attachment=True)
        except FileNotFoundError:
            abort(404)
        return redirect('/')
        

    
    # def generate_large_csv():
    #     def generate():
    #         yield 'This is a sample file'
    #     return Response(generate(), mimetype='text/csv')

    return app

# if __name__ == ('__main__'):
#     print('hit main')
#     create_app()



