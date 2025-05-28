import sqlite3

CONN=sqlite3.connect('lib/db/estate_management.db')
CURSOR=CONN.cursor()