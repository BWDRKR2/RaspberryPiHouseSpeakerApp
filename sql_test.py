#!/usr/bin/python

import sqlite3
from werkzeug.security import check_password_hash

conn = sqlite3.connect('Speakers.db')
print "Opened database successfully";


conn.execute('DROP TABLE USERS;')

conn.execute('''CREATE TABLE USERS
         (
         User            TEXT    NOT NULL,
         Password        TEXT    NOT NULL);''')
print "Table created successfully";


conn.execute("INSERT INTO USERS ( User,Password) \
     VALUES ( 'BWDRKR2','pbkdf2:sha1:1000$HegX5Ikp$7a51190456ff7f2c5b039804932813475b289e8b')");

conn.execute("INSERT INTO USERS ( User,Password) \
     VALUES ( 'DanK','pbkdf2:sha1:1000$HegX5Ikp$7a51190456ff7f2c5b03980493281347gngfgf5b289e8b')");

conn.execute("INSERT INTO USERS ( User,Password) \
     VALUES ( 'Kelly','pbkdf2:sha1:1000$HegX5Ikp$7a51190456ff7f2c5b03980493281347gngfgf5b289e8b')");

conn.execute("INSERT INTO USERS ( User,Password) \
     VALUES ( 'Pete','pbkdf2:sha1:1000$HegX5Ikp$7a51190456ff7f2c5b03980493281347gngfgf5b289e8b')");


conn.commit()
print "Records created successfully";



cursor = conn.execute("SELECT rowid, User, Password from USERS ")
for row in cursor:
   #print rowid
   print "ID = ", row[0]
   print "USERS = ", row[1]
   print "PASSWORD = ", row[2]

#hashpassword = row[2]

  

#check_hash =  check_password_hash(hashpassword, 'Editors100')

#print "Hash Passed = ", check_hash







conn.close()

