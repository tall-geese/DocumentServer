from sqlalchemy.engine import Engine, create_engine, Connection, ResultProxy, url, RowProxy
from flask import Flask


def testConnection_Lin(app) -> list:
    if not (isinstance(app, Flask)):
        pass
    # eng = create_engine(app.config.get('CONNECTION_STRING_LINUX'))
    eng = create_engine(app.config.get('CONNECTION_STRING_WINDOWS'))
    conn = eng.connect()
    proxyAllDocs = conn.execute('SELECT Doc_ID, Doc_Num, Doc_Name, Doc_Type, Revision, Doc_Status, File_Path FROM dbo.PT_QC_Doc').fetchall()
    # TODO: add another select statement here for the linux server

    documents = []
    for row in proxyAllDocs: documents.append(row.values())
    conn.close()

    return documents

def TestOutput(line):
    print (line)

