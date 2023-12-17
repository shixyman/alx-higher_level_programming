#!/usr/bin/python3
"""
python script that lists all states from the database hbtn_0e_0_usa with
a given name
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM states WHERE name LIKE '{argv[4]}' ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        if row in rows:
            print(row)
    cursor.close()
    db.close()
