from sqlalchemy.engine import Engine, create_engine, Connection, ResultProxy, url, RowProxy
from flask import Flask


def testConnection_Lin(app) -> list:
    if not (isinstance(app, Flask)):
        pass
    # eng = create_engine(app.config.get('CONNECTION_STRING_LINUX'))
    # eng = create_engine(app.config.get('CONNECTION_STRING_WINDOWS'))
    # eng = create_engine(app.config.get('CONNECTION_STRING_76'))
    eng = create_engine(app.config.get('CONNECTION_STRING_UNIPOINT_TEST'))
    
    conn = eng.connect()

    # Unipoint test database connection string
    # proxyAllDocs = conn.execute(
    #     """
    #     SELECT pqd.Doc_ID, pqd.Doc_Num, pqd.Doc_Name, pqd.Doc_Type, pqd.Revision, pqd.Doc_Status, pqd.File_Path
    #     FROM dbo.PT_QC_Doc pqd 
    #     FULL OUTER JOIN (Select pqd.Doc_ID
    #     FROM dbo.PT_QC_Doc pqd 
    #     Inner Join dbo.PT_Attach pta ON pqd.Doc_ID = pta.AttachReference 
    #     Where pta.AttachPath like '%Sample%' and pta.AttachType = 'Document PDF') src on pqd.Doc_ID = src.Doc_ID
    #     WHERE pqd.Doc_Num like '%Sample%' AND pqd.Doc_Status = 'Active' AND (pqd.Doc_ID IS NULL OR src.Doc_ID IS NULL)
    #     UNION ALL
    #     Select pqd.Doc_ID, pqd.Doc_Num, pqd.Doc_Name, pqd.Doc_Type, pqd.Revision, pqd.Doc_Status, pta.AttachPath
    #     FROM dbo.PT_QC_Doc pqd 
    #     Inner Join dbo.PT_Attach pta ON pqd.Doc_ID = pta.AttachReference 
    #     Where pta.AttachPath like '%Sample%' and pta.AttachType = 'Document PDF' AND pqd.Doc_Status ='Active'
    #     ORDER BY pqd.Doc_Num 

    #     """
    # ).fetchall()
    proxyAllDocs = conn.execute(
        """
        SELECT pqd.Doc_ID, pqd.Doc_Num, pqd.Doc_Name, pqd.Doc_Type, pqd.Revision, pqd.Doc_Status, pqd.File_Path
        FROM dbo.PT_QC_Doc pqd 
        FULL OUTER JOIN (Select pqd.Doc_ID
        FROM dbo.PT_QC_Doc pqd 
        Inner Join dbo.PT_Attach pta ON pqd.Doc_ID = pta.AttachReference 
        Where pta.AttachPath like '%Sample%' and pta.AttachType = 'Document PDF') src on pqd.Doc_ID = src.Doc_ID
        WHERE pqd.Doc_Num like '%Sample%' AND (pqd.Doc_ID IS NULL OR src.Doc_ID IS NULL)
        UNION ALL
        Select pqd.Doc_ID, pqd.Doc_Num, pqd.Doc_Name, pqd.Doc_Type, pqd.Revision, pqd.Doc_Status, pta.AttachPath
        FROM dbo.PT_QC_Doc pqd 
        Inner Join dbo.PT_Attach pta ON pqd.Doc_ID = pta.AttachReference 
        Where pta.AttachPath like '%Sample%' and pta.AttachType = 'Document PDF'
        ORDER BY pqd.Doc_Num 

        """
    ).fetchall()



    # Home Test Database SQL string
    # proxyAllDocs = conn.execute('SELECT Doc_ID, Doc_Num, Doc_Name, Doc_Type, Revision, Doc_Status, File_Path FROM dbo.PT_QC_Doc').fetchall()
    


    # Jade76 IQS Sql Call
#     proxyAllDocs = conn.execute(
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
#     ).fetchall()

    documents = []
    for row in proxyAllDocs:
        proxyList = row.values()

        # some document names contain ','s in them and cause errors when we end up splitting by 
        # these later on. Temp replacing them with ^ here and switching back later after we split in arrays
        # Removing the '-' here to differentiate between searching for a doc name and searching for a doc_id
        # in main.js we will auto search by the doc_id if the user ever enters a '-'
        proxyList[2] = proxyList[2].replace(',','^')
        proxyList[2] = proxyList[2].replace('-',' ')
        documents.append(proxyList)
    conn.close()

    # TODO: We should try and clean the fields for any ',' in the values, is there any way to do this through the SQL select??

    return documents

def TestOutput(line):
    print (line)

