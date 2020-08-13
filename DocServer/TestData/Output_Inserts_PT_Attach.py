import csv

with open("PT_Attach_data.csv", "r", newline='') as csvFile:
    with open("PT_Attach-Inserts.sql",'w', newline='') as outputFile:
        reader = csv.reader(csvFile, delimiter=',')
        next(reader)

        outputFile.write('INSERT INTO PT_Attach (Attach_Reference, Attach_Path, Attach_Type) VALUES \n')
        for row in reader:

            if (reader.line_num != 2):
                outputFile.write(',\n')
            outputFile.write('(\'' + '\',\''.join(row) + '\')')
        
        outputFile.write(';')