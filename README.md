# sqlite_python_moviesdb
SQLITE PYTHON INTEGRATION AND BASIC CRUD OPERATIONS
--------------------------------------------------

1.Download repo

2.Extract 

3.Execute python script>>python script.py

----------------------------------------------------
Movies.db
----------


create movies database using DB BROWSER 

or
mannually create

*con=sqlite3.connect('movies.db')*



*CREATE TABLE "movies" (
	"ID"	INTEGER,
	"NAME"	TEXT,
	"LEAD"	TEXT,
	"YEAR"	INTEGER,
	"DIRECTOR"	TEXT,
	PRIMARY KEY("ID" AUTOINCREMENT)
);*


----------------------------------------------------
script.py
----------

Used python to Communicate with the database


Below are operations performed on the database

1.INSERT   2.UPDATE 3.DELETE  4.SELECT(DISPLAY ALL)   5.DELETE ALL

You are asked to select a option 

1.INSERT >>Inserts a record into the table

2.UPDATE >>Makes changes to the existing record

3.DELETE >>Deletes a record by ID

4.SELECT >>Displays all Records

5.DELETE ALL>> TRUNCATE operation



