import sqlite3
import csv


conn = sqlite3.connect('C:\Coding\ProjectsFile\court.sqlite')
c = conn.cursor()
try:
    c.execute('''CREATE TABLE cases (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    ourId TEXT NOT NULL,
    party TEXT NOT NULL,
    counterParty TEXT,
    description TEXT,
    officeLocation TEXT,
    caseNumbers TEXT,
    vps TEXT,
    status TEXT, 
    tStamp TEXT DEFAULT CURRENT_TIMESTAMP)''')

except:
    print("Database already exists, updating existing one!")

# opening the file
with open("C:\Coding\ProjectsFile\Projects\CSVtoSQL\\tmp.csv", "r", encoding='UTF-8') as file:
    reader = csv.reader(file, delimiter=";")
    for row in reader:
        print(row)
        ourID = row[0]
        party = row[1]
        counterParty = row[2]
        description = row[3]
        officeLocation = row[4]
        caseNumbers = row[5]
        vps = row[6]
        status = row[7]
        c.execute('''INSERT INTO court (ourID,party,counterParty,description,officeLocation,caseNumbers,vps,status)
            VALUES (?,?,?,?,?,?,?,?)''',
            (ourID,
            party,
            counterParty,
            description,
            officeLocation,
            caseNumbers,
            vps,
            status))
            
        conn.commit()
        conn.close()
