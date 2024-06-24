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
    query = """SELECT cities.name FROM states
            INNER JOIN cities ON states.id = cities.state_id
            WHERE states.name = %s
            ORDER BY cities.id ASC"""

    cur.execute(query, (argv[4],))
    data = cur.fetchall()

    # Create list with items and join them with ", "
    print(", ".join([city[0] for city in data]))
    cur.close()
    conn.close()
