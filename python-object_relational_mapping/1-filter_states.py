#!/usr/bin/python3
"""List all states with name starting with N from a database"""
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3], port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name \
                   LIKE BINARY 'N%' \
                   ORDER BY id")

    states = cursor.fetchall()

    for state in states:
        print(state)
