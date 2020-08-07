Create table dbo.PT_Attach(
	Attachment INT IDENTITY(1,1),
		Constraint pt_attach_pk
		PRIMARY KEY (Attachment),
	Attach_Type VARCHAR(30),
	Attach_Path VARCHAR(255),
	Attach_Reference VARCHAR(255),
		Constraint pt_attach_fk
		FOREIGN KEY (Attach_Reference)
		REFERENCES dbo.PT_QC_Doc(Doc_Num)
);