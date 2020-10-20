from sqlalchemy.engine import Engine, create_engine, Connection, ResultProxy, url, RowProxy
from flask import Flask


def testConnection_Lin(app) -> list:
    if not (isinstance(app, Flask)):
        pass
    # eng = create_engine(app.config.get('CONNECTION_STRING_LINUX'))
    eng = create_engine(app.config.get('CONNECTION_STRING_WINDOWS'))
    # eng = create_engine(app.config.get('CONNECTION_STRING_76'))
    conn = eng.connect()

    # Home Test Database SQL string
    proxyAllDocs = conn.execute('SELECT Doc_ID, Doc_Num, Doc_Name, Doc_Type, Revision, Doc_Status, File_Path FROM dbo.PT_QC_Doc').fetchall()
    
    # Jade76 IQS Sql Call
    # proxyAllDocs = conn.execute(
#         """
#         SELECT src.DOCUMENT_ID [Doc_Num], max(src.NAME) [Doc_Name], max(dt.NAME) [Doc_Type], min(src.state) [Doc_Status],  
# (UPPER((SUBSTRING(max(em.FIRST_NAME) , 1, 1) +  max(em.LAST_NAME)))) [Doc_Manager] , 'Yes' [ForceRevControl], SRC.REVISION_LEVEL [Revision],
# NULL [Reference], NULL [Customer], NULL [Vendor], NULL [Part], 
# 		(SELECT rc.DESCRIPTION 
# 		 FROM IQSWeb.dbo.REFERENCE_CODE rc
# 		 WHERE rc.CODE_SYSID = max(src.deptCode)) [Department], NULL [Division], NULL [Doc_Category], NULL [Master_Location],
# 		(SELECT le.FILE_LOCATION 
# 		 FROM IQSWeb.dbo.DOCUMENT_LINK_EMBED dle 
# 		 LEFT OUTER JOIN IQSWeb.dbo.LINK_EMBED le on dle.LINK_EMBED_SYSID = le.LINK_EMBED_SYSID 
# 		 WHERE dle.DEF_LINK_EMBED = 'Y' and max(src.DOCUMENT_ID) = dle.DOCUMENT_ID) [File_Path], 'No' [IsWebPath]
# FROM (SELECT do.DOCUMENT_ID , do.NAME, do.REVISION_LEVEL, do.DOCUMENT_TYPE_ID, do.EMPLOYEE_ID, 
# 		CASE do.REVISION_LEVEL 
# 			when 'OBSOLETE' then 'OBSOLETE'
# 			when '0' then 'PENDING'
# 			else 'ACTIVE'
# 		END AS state, do.FUNCTION_CODE_SYSID deptCode
# 	from IQSWeb.dbo.DOCUMENT do
# 	union all
# 	SELECT  da.DOCUMENT_ID DOCUMENT_ID , da.NAME NAME, da.REVISION_LEVEL REVISION_LEVEL , da.DOCUMENT_TYPE_ID DOCUMENT_TYPE_ID , 
# 		 da.EMPLOYEE_ID EMPLOYEE_ID , 'OBSOLETE' state, da.FUNCTION_CODE_SYSID deptCode
# 	FROM IQSWeb.dbo.DOCUMENT_ARCH da) src
# left outer join IQSWeb.dbo.DOCUMENT_TYPE dt on src.DOCUMENT_TYPE_ID = dt.DOCUMENT_TYPE_ID 
# left outer join IQSWeb.dbo.EMPLOYEE em on src.EMPLOYEE_ID = em.EMPLOYEE_ID 
# where src.state = 'ACTIVE'
# group by src.REVISION_LEVEL, src.DOCUMENT_ID
# order by  src.DOCUMENT_ID, src.REVISION_LEVEL ASC

#         """

    # ).fetchall()

    documents = []
    for row in proxyAllDocs: documents.append(row.values())
    conn.close()

    return documents

def TestOutput(line):
    print (line)

