#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    curs = db.cursor()
    curs.execute("""SELECT cities.id, cities.name, states.name
                 FROM cities JOIN states
                 on cities.state_id = states.id
                 ORDER BY cities.id""")
    data = curs.fetchall()
    for row in data:
        print(row)
    curs.close()
    db.close()
