#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    curs = db.cursor()
    mat = argv[4]
    curs.execute("""SELECT * FROM states WHERE name LIKE BINARY %s
                    ORDER BY states.id""", (mat))
    data = curs.fetchall()
    for row in data:
        print(row)s
    curs.close()
    db.close()
