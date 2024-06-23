#!/usr/bin/python3

"""
This module connects python script to a database.
"""

import MySQLdb as db
from sys import argv

if __name__ == "__main__":

    my_db = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])

    with my_db.cursor() as my_cursor:
        my_cursor.execute("""
            SELECT
                cities.id, cities.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name LIKE BINARY %(state_name)s
            ORDER BY
                cities.id ASC
        """, {
            'state_name': argv[4]
        })
        rows_selected = my_cursor.fetchall()

    if rows_selected is not None:
        print(", ".join([row[1] for row in rows_selected]))
