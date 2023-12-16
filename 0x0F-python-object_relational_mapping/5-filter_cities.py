#!/usr/bin/python3
"""script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
Results must be sorted in ascending order by cities.id
Your script should take 4 arguments: mysql
username, mysql password, database name and
a state name (SQL injection free!)
You must use the module MySQLdb (import MySQLdb)
You can use only execute() once
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name FROM cities " +
                "INNER JOIN states ON cities.state_id = states.id " +
                "WHERE states.name = %s " +
                "ORDER BY cities.id", (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
