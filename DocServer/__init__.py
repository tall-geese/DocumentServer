# Windows/Linux 
    # set/export FLASK_APP=DocServer
    # set/export FLASK_ENV=development
    # set/export DEVELOPMENT=1
    # set/export FLASK_RUN_PORT=8080   <--- port 8080 forbidden on J76, occupied by former doc viewer

from flask import Flask, url_for, render_template, render_template_string, send_file, abort, redirect, request, make_response
import DocServer.db as db
from datetime import datetime, timedelta
import json

def create_app():
    app = Flask('DocServer')
    # app.config.from_pyfile('configurations/testing_config.py')  #IQS server / Unipoint Test Server
    app.config.from_pyfile('configurations/production_config.py')   #Unipoint Server
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


    @app.route('/', methods=['GET','POST'])
    def index():
        if request.method == 'POST':
            resp = make_response(redirect(url_for('index')))
            # set cookies to form values, checkboxes won't be in the dict if they arent check off, so we're just checking they exist
            # TODO: simplify this repeating block of code
            if 'enableSaved' in request.form:
                resp.set_cookie('enableSaved','checked')
            else:
                resp.set_cookie('enableSaved','unchecked')                
            if 'noPDF' in request.form:
                resp.set_cookie('noPDF','checked')
            else:
                resp.set_cookie('noPDF','unchecked')                
            if 'darkTheme' in request.form:
                resp.set_cookie('darkTheme','checked')
            else:
                resp.set_cookie('darkTheme','unchecked')
            resp.set_cookie('maxRows',request.form.get('maxRows'))                

            # now redirect to the GET block after setting the cookies
            return resp

        if request.method == 'GET':
            cookies = request.cookies

            # if cookies haven't been set yet or client has cookies disabled
            if not cookies:
                documents = db.testConnection_Lin(app, False)
                expires = datetime.now() + timedelta(days=365*10)

                enableSaved='checked'
                rows=[]
                noPDF='unchecked'
                maxRows='30'
                darkTheme='unchecked'

                resp = make_response(render_template('index.html', documents=documents, enableSaved=enableSaved,
                rows=rows, noPDF=noPDF, maxRows=maxRows, darkTheme=darkTheme, dev='disabled'))

                resp.set_cookie('enableSaved',enableSaved, expires=expires)
                resp.set_cookie('rows',json.dumps(rows), expires=expires)
                resp.set_cookie('noPDF',noPDF, expires=expires)
                resp.set_cookie('maxRows',maxRows, expires=expires)
                resp.set_cookie('darkTheme',darkTheme, expires=expires)

                return resp

            # standard response
            elif ('enableSaved' in cookies and 'noPDF' in cookies and 'rows' in cookies
                and 'maxRows' in cookies and 'darkTheme' in cookies):

                if cookies['enableSaved'] == 'checked':
                    rows = json.loads(cookies['rows'])
                else:
                    rows = []

                if cookies['noPDF'] == 'checked':
                    ogDocType = True
                else:
                    ogDocType = False

                if 'developer' in cookies and cookies['developer'] == 'QA':
                    dev = 'enabled'
                else:
                    dev = 'disabled'

                documents = db.testConnection_Lin(app, ogDocType)
                return render_template('index.html', documents=documents, enableSaved=cookies['enableSaved'],  noPDF=cookies['noPDF'],
                    rows=rows, maxRows=cookies['maxRows'], darkTheme=cookies['darkTheme'], dev=dev)
            else:
                print('issue here with user cookies, aborting')
                abort(404)


    @app.route('/documents/rev=<string:rev>/num=<string:num>/name=<path:name>/type=<string:ftype>/<path:subpath>')
    def generate_file(rev,num,name,ftype,subpath):
        cookies = request.cookies
        expires = datetime.now() + timedelta(days=365*10)

        if 'enableSaved' in cookies and cookies['enableSaved'] == 'checked':
            switch_file_type = {
                'pdf':'static/images/pdf-icon.png',
                'xl':'static/images/excel-xls-icon.png',
                'doc':'static/images/word-doc-icon.png',
                'ppt':'static/images/ppt-icon.png'
            }

            row_path = '/documents/' + 'rev=' + rev + '/num=' + num + '/name=' + name + '/type=' + ftype + '/' + subpath

            if 'rows' in cookies:
                savedRows = json.loads(cookies['rows'])
                searchedRow = [rev,num,name,switch_file_type[ftype],row_path]

                try:
                    duplicate_index = savedRows.index(searchedRow)
                    savedRows.remove(searchedRow)
                    savedRows.insert(0,searchedRow)
                except ValueError:
                    savedRows.insert(0,searchedRow)
                finally:
                    row_info = savedRows[:5]
            else:
                row_info = [searchedRow]
        else:
            row_info = []

        try:
            rows = json.dumps(row_info,sort_keys=False)

            resp = make_response(send_file(app.config.get('UNIPOINT_FILE_DIR') + subpath, as_attachment=False))
            resp.set_cookie('rows',rows,expires=expires)
            return resp
        except FileNotFoundError:
            abort(404)
        return redirect('/')

    return app
