#!/usr/bin/env python3

# based on
# https://pythonprogramming.net/sql-database-python-part-1-inserting-database/

import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')

con = sqlite3.connect('my_db')
c = con.cursor()


def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS myTable(
	unix REAL, datestamp TEXT, keyword TEXT, value REAL
	)
    """)


def data_entry():
    c.execute(
        "INSERT INTO myTable VALUES(1452541231251,'2019-11-03 13:53:39','Python',2)")
    con.commit()


def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(
        unix).strftime('%Y-%m-%d %H:%M:%S'))
    keywords = ['python', 'data_science', 'tutorial', 'sqlite', 'fun']
    value = random.randrange(0, 5)
    key = keywords[value]

    c.execute("INSERT INTO myTable (datestamp, keyword, unix, value)\
        VALUES (?, ?, ?, ?)",
              (date, key, unix, value)
              )
    con.commit()


def read_from_db():
    c.execute(
        "SELECT datestamp, value FROM myTable WHERE value>=2 AND value<4 AND keyword='tutorial'")
    for row in c.fetchall():
        print(f"date: {row[0]}, value: {row[1]}")

    c.execute(
        "SELECT COUNT(value), SUM(value), AVG(value) FROM myTable WHERE value >= 3")
    data = c.fetchone()
    print('**********************\
        \nCOUNT:\t', data[0],
          '\nSUM:\t', data[1],
          '\nAVG:\t', data[2])


def graph_data():
    c.execute("SELECT unix, value FROM myTable")
    dates = []
    values = []
    for row in c.fetchall():
        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])

    plt.plot_date(dates, values, '-')
    plt.show()


def update_data():
    c.execute("UPDATE myTable SET value=999 WHERE value=3")
    con.commit()

    c.execute("SELECT * FROM myTable WHERE value=999")
    [print(row) for row in c.fetchall()]


def update_one():
    c.execute("SELECT COUNT(*) FROM myTable WHERE value=555")
    print(f"BEFORE:\t{c.fetchone()[0]}")

    c.execute("UPDATE myTable SET value=555 WHERE rowid IN \
        (SELECT rowid FROM myTable WHERE value=999 LIMIT 1)")

    c.execute("SELECT COUNT(*) FROM myTable WHERE value=555")
    print(f"AFTER:\t{c.fetchone()[0]}")

    con.commit()


def delete_data():
    c.execute("SELECT COUNT(*) FROM myTable WHERE value=555")
    print(f"BEFORE:\t{c.fetchone()[0]}")

    c.execute("SELECT rowid FROM myTable WHERE value=555 LIMIT 1")
    to_delete = c.fetchone()
    if to_delete:
        c.execute(f"DELETE FROM myTable WHERE rowid={to_delete[0]}")

    c.execute("SELECT COUNT(*) FROM myTable WHERE value=555")
    print(f"AFTER:\t{c.fetchone()[0]}")

    con.commit()


# uncomment single lines to use

# create_table()
# data_entry()

# for i in range(0, 50):
#     dynamic_data_entry()
    # time.sleep(1)
# read_from_db()
# graph_data()
# update_data()
# update_one()
# delete_data()

c.close()
con.close()
