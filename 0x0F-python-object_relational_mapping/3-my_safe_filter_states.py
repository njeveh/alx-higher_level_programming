#!/usr/bin/python3

"""
This script takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
        )
    cur = conn.cursor()
    query = """
    SELECT * FROM states WHERE BINARY name=%(name)s ORDER BY id ASC
    """, {'name': argv[4]}
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
