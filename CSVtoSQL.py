import sqlite3
import csv


print("--------------------------------------------------------")
# waits for CSV file input
execfile = input("--csv ")
print("--------------------------------------------------------")
# waits for database name input
makeDB = input("--db ")
print("--------------------------------------------------------")

if os.path.exists(makeDB):
    print("Updating Database!\n")
    print("Finished.")

else:
    conn = sqlite3.connect(makeDB)
    c = conn.cursor()

    # creates the table in SQLite
    print("Creating Database.\n")
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

    # opening the file and inserting the data into the table
    with open(execfile, "r", encoding='UTF-8') as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            ourId = row[0]
            party = row[1]
            counterParty = row[2]
            description = row[3]
            officeLocation = row[4]
            caseNumbers = row[5]
            vps = row[6]
            status = row[7]
            c.execute('''INSERT INTO cases(ourId,party,counterParty,description,officeLocation,caseNumbers,vps,status) 
            VALUES (?,?,?,?,?,?,?,?)''',
                    (ourId,
                    party,
                    counterParty,
                    description,
                    officeLocation,
                    caseNumbers,
                    vps,
                    status)),
            conn.commit()
        print("Finished.")
        conn.close()
