'''
Created on Sep 18, 2017

@author: mohommad_belal
'''
import mysql.connector

cnxn = mysql.connector.connect(user='mohommad_belal', password='India@123',
                              host='db4free.net',
                              database='hibernate_2017')
crsr = cnxn.cursor()
crsr.execute("DROP TABLE IF EXISTS pytest")
crsr.execute("""
CREATE TABLE pytest (
    id INT(11) NOT NULL AUTO_INCREMENT,
    firstname VARCHAR(20),
    PRIMARY KEY (id)
    )
""")
crsr.execute("INSERT INTO pytest (firstname) VALUES ('Gord')")
crsr.execute("INSERT INTO pytest (firstname) VALUES ('Anne')")
cnxn.commit()
crsr.execute("SELECT firstname FROM pytest")
fname = crsr.fetchone()[0]
print(fname)
crsr.execute("SELECT firstname FROM pytest")