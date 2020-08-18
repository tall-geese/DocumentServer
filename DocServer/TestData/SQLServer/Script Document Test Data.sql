--Select our sample data from IQS, formatted roughly in the way that Unipoint will be storing it.
--Not selecting everything though, only what we expect to use in the doc server
--included or docID = pr-42-002 at the end there since its revision is currently pending

SELECT do.DOCUMENT_ID [Doc_num], do.NAME [Doc_name], 'XXX' [Doc_type], do.REVISION_LEVEL [Revision],
'Active'[Doc_status], do.EFFECTIVE_DATE, le.FILE_LOCATION [File_Path], ROW_NUMBER() OVER(ORDER BY do.DOCUMENT_ID ASC) [Doc_ID]
FROM IQSWeb.dbo.DOCUMENT do
LEFT OUTER JOIN DOCUMENT_LINK_EMBED dle on dle.DOCUMENT_ID = do.DOCUMENT_ID 
LEFT OUTER JOIN LINK_EMBED le on dle.LINK_EMBED_SYSID  = le.LINK_EMBED_SYSID 
WHERE (do.DOCUMENT_ID IN ('wi-75-005','wi-71-001','wi-75-057','fo-83-001','fo-83-005','pr-42-002','pr-72-001','pr-75-003')) 
AND dle.DEF_LINK_EMBED = 'Y' and (do.STATUS = 'C' or do.DOCUMENT_ID = 'pr-42-002')
