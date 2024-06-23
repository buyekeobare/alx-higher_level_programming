#!/usr/bin/python3
"""
This module connects a python script to a database
"""

    import MySQLdb
    from sys import argv


    if __name__ == "__main__":

    # Connect database using command-line args
    db = MySQLdb.connect(host='localhost', user=argv[1], password=argv[2],
                            db=argv[3], port=3306)
    # Create cursor object to interact with db
    cur = db.cursor()

    # Execute a SELECT query to fetch data
    cur.execute("SELECT * FROM states ORDER BY states.id ASC;")

    # fetch all the data returned by the query
    data = cur.fetchall()

    # Iterate through the fetched data and print each row
    for row in data:
        print(row)

    # Close all cursors
    cur.close()

    # Close all databases
    db.close()
