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
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `cities` as `ci` \
                INNER JOIN `states` as `st` \
                   ON `ci`.`state_id` = `st`.`st_id` \
                ORDER BY `ci`.`id`")
    print(", ".join([ct[2] for ct in c.fetchall() if ct[4] == sys.argv[4]]))
