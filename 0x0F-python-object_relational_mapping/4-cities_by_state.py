#!/usr/bin/python3
"""
    a script that lists all cities from the database hbtn_0e_4_usa
     Your script should take 3 arguments: mysql username, mysql password and database name
     You must use the module MySQLdb (import MySQLdb)
     Your script should connect to a MySQL server running on localhost at port 3306
     Results must be sorted in ascending order by cities.id
     You can use only execute() once
     Results must be displayed as they are in the example below
     Your code should not be executed when imported
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=argv[1], passwd=argv[2], db=argv[3])
    query = "SELECT cities.id, cities.name, states.name\
             FROM cities JOIN states\
             WHERE cities.state_id = states.id"
    cursor = db.cursor()
    cursor.execute(query)
    for state in cursor.fetchall():
        print(state)
    cursor.close()
    db.close()
