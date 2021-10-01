#PYTHON INTEGRATION WITH SQLITE AND PERFORMING CRUD OPERATIONS  -->BY:JANARDHAN

import sqlite3 
con=sqlite3.connect('movies.db')    #this creates movies.db database if it doesnt exist
#after creating database create table with columns NAME,LEAD,YEAR,DIRECTOR (i used DB browser for creating table ) 
#or create table manually
# con.execute("""CREATE TABLE movies(
#ID INTEGER,
#NAME TEXT,
#LEAD TEXT,
#YEAR INTEGER,
#DIRECTOR TEXT,
#PRIMARY KEY(ID AUTOINCREMENT)
# );""")


#function for inserting records
def insertData(name,lead,year,director):
    qry="insert into movies (NAME,LEAD,YEAR,DIRECTOR) values (?,?,?,?);"
    con.execute(qry,(name,lead,year,director))
    con.commit()
    print("INSERT SUCCESS!")

#function for updating records
def updateData(name,lead,year,director,id):
    qry="update movies set NAME=?,LEAD=?,YEAR=?,DIRECTOR=? where ID=?;"
    con.execute(qry,(name,lead,year,director,id))
    con.commit()
    print("EDIT SUCCESS!")

#function for deleting records
def deleteData(id):
    qry="delete from movies where ID=?;"
    con.execute(qry,(id))
    con.commit()
    print("DELETED ROW "+id+" SUCCESSFULLY")

#function for displaying all records
def selectData():
    qry="select * from movies"
    result=con.execute(qry)
    for row in result:
        print(row)
#function to delete all records
def deleteAll():
    prom=input("ENTER YES TO CONTINUE OR ANY KEY TO SKIP :  ")
    if(prom=='YES' or  prom=='yes'):
        qry="delete from movies;"
        con.execute(qry)
        con.commit()
        print("DELETED ALL RECORDS")
    else:
        print("skipped....")
   
    

#choice based function selection (choose the specified number for INSERT , UPDATE , DELETE, SELECT operations)
ch=1
while ch==1:
    print("""
1.INSERT   2.UPDATE   3.DELETE   4.SELECT(DISPLAY ALL)  5.DELETE ALL
""")
    c=int(input("Select Your Choice : "))
    if(c==1):
        print("----Add New Record----")
        name=input("Enter Movie Name : ")
        lead=input("Enter Lead Actor : ")
        year=input("Enter Year : ")
        director=input("Enter director Name :")
        insertData(name,lead,year,director)
       
    elif (c==2):
        print("----Edit A Record----")
        id=input("Enter Row ID : ")
        name=input("Enter Movie Name : ")
        lead=input("Enter Lead Actor : ")
        year=input("Enter Year of Release : ")
        director=input("Enter director Name :")
        updateData(name,lead,year,director,id)
       
    elif (c==3):
        id=input("Enter Row ID : ")
        deleteData(id)
        
    elif (c==4):
        print("----PRINTING ALL RECORDS----")
        selectData()
    elif (c==5):
        deleteAll()
    else:
        print("Invalid Selection!!")
    ch=int(input("Enter 1 To Continue : "))
print("OK DONE")