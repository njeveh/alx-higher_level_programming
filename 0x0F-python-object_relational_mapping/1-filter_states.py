#!/usr/bin/python3

"""
This script lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""

if __name__ == '__main__':
    import sys
    import MySQLdb
    if len(sys.argv) > 3:
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8"
            )
        cur = conn.cursor()
        cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        conn.close()
