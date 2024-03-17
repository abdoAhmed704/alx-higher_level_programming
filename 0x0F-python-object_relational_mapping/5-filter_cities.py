#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    curs = db.cursor()
    curs.execute("""SELECT cities.name
                 FROM cities JOIN states
                 on cities.state_id = states.id
                 WHERE states.name= %s
                 ORDER BY cities.id""", (argv[4],))
    data = curs.fetchall()
    new = (list(x[0] for x in data))
    print(*new, sep=", ")
    curs.close()
    db.close()
