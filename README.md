# CSVtoSQlite

version 0.08

CSVtoSQLite.py is a program that reads through a CSV file and either creates a new SQLite table or updates and existing one.

The script needs an csv file input and a database name to check if it needs to update/insert information to an existing database or create an entirely new database.

The initial database creation and data entry is functional. However, the data comparation and insertion needs to be tweaked as it just inserts new rows of data regardless of the fact that ourID matches with data already present in the database.
