import csv

with open("PT_QC_Doc_data.csv", "r", newline='') as csvFile:
    with open("PT_QC_Doc-Inserts.sql",'w', newline='') as outputFile:
        reader = csv.reader(csvFile, delimiter=',')
        next(reader)

        outputFile.write('INSERT INTO PT_QC_Doc (Doc_Num, Doc_Name, Doc_type, Revision, Doc_status, Effective_Date, File_Path) VALUES \n')
        for row in reader:

            if (reader.line_num != 2):
                outputFile.write(',\n')
            outputFile.write('(\'' + '\',\''.join(row) + '\')')
        
        outputFile.write(';')