#!/usr/bin/python3

"""
This script lists all cities from the database hbtn_0e_4_usa
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
    query = """SELECT cities.id, cities.name, states.name FROM cities
    INNER JOIN states ON cities.state_id = states.id ORDER BY id ASC;"""
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
