--Pulling attachments data from IQS in the format that it will be used in Unipoint for
--testing with the doc Server. In addition this will get a field to refer to the unique 
--id of the document of the most current revision

SELECT do.DOCUMENT_ID , le.LINK_EMBED_SYSID, le.FILE_LOCATION, dle.DEF_LINK_EMBED 
FROM IQSWeb.dbo.LINK_EMBED le 
LEFT OUTER JOIN IQSWeb.dbo.DOCUMENT_LINK_EMBED dle on le.LINK_EMBED_SYSID = dle.LINK_EMBED_SYSID 
LEFT OUTER JOIN IQSWeb.dbo.DOCUMENT do on dle.DOCUMENT_ID = do.DOCUMENT_ID 
WHERE do.DOCUMENT_ID IN ('WI-75-005','WI-71-001','WI-75-057','FO-83-001','FO-83-005','PR-42-002','PR-72-001','PR-75-003')
