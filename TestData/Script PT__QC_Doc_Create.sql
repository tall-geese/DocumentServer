Create Table dbo.PT_QC_Doc(
	Doc_ID INT IDENTITY (1,1),
		Constraint pt_qc_doc_pk
		Primary Key (Doc_ID),
	Doc_Num VARCHAR(255),
		Constraint pt_doc_unique
		UNIQUE (Doc_Num),
	Doc_Name VARCHAR(255),
	Doc_Type VARCHAR(50),
	Revision VARCHAR(2),
	Doc_Status VARCHAR(15),
	Effective_Date DATETIME,
	File_Path VARCHAR(255)
);

