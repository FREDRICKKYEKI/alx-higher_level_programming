#!/usr/bin/python3
"""
 - Write a script that lists all states with a name starting with N (upper N)
   from the database hbtn_0e_0_usa:
 - Your script should take 3 arguments: mysql username, mysql password and
   database name (no argument validation needed)
 - You must use the module MySQLdb (import MySQLdb)
 - Your script should connect to a MySQL server running on localhost at port
   3306
 - Results must be sorted in ascending order by states.id
 - Results must be displayed as they are in the example below
 - Your code should not be executed when imported
"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT * FROM states
                WHERE CONVERT(`name` USING Latin1)
                COLLATE Latin1_General_CS
                LIKE 'N%'
                ORDER BY id;""")

    states = cur.fetchall()

    for filt_state in states:
        print(filt_state)
