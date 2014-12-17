#!/usr/bin/env python

import MySQLdb as mdb


""" 
Purpose: Reads CSV file and inserts data into People DB
"""

table_command = """CREATE TABLE IF NOT EXISTS internationStudents (
                   student_id int(5) NOT NULL AUTO_INCREMENT,
                   first_name varchar(50) DEFAULT NULL,
                   last_name varchar(50) DEFAULT NULL,
                   email_addr varchar(50) DEFAULT NULL,
                   country varchar (50) DEFAULT NULL,
                   city varchar(50) DEFAULT NULL,
                   PRIMARY KEY(student_id)
                   );
                   """


# Open database connection, (host, user, pw, DB_Name)
db = mdb.connect("localhost", "root", "password", "people")

# prepare a cursor object using cursor() method
cur = db.cursor()

try:
    cur.execute(table_command) #create table in DB    
    
    #firstname, lastname, email, country, city
    file_obj = open("MOCK_DATA.csv", "r")

    for line in file_obj:
        arry =  tuple(line.split(','))
        #print arry
        
        ins_cmd = """INSERT INTO internationStudents (first_name, last_name, email_addr, country, city) VALUES ('{0}','{1}','{2}','{3}','{4}');""".format(arry[1],arry[2],arry[3],arry[4],arry[5].rstrip("\n"))
        cur.execute(ins_cmd)

    db.commit()
except mdb.Error, e:
    # Rollback in case there is any error
    db.rollback()
    cur.execute("DROP TABLE IF EXISTS internationStudents;")
    print e


# disconnect from server
db.close()
        

