#!/usr/bin/python3.10
##c used by ipy script to get ipy history
sqldb="/home/steff007/.ipython/profile_default/history.sqlite"
fileName = "/home/steff007/script/sql_hist"
import sqlite3
conn = sqlite3.connect(sqldb)
c = conn.cursor()
q='''
SELECT source from history where source not like '%get%';
'''
ip = c.execute(q)
ipl=list(ip)
f = open(fileName, "a", encoding="utf-8")
for row in ipl:
    # print(len(str(row)))
    # myRow = row[0].translate(mapping)
    if len(row) != 0:
        print(row[0])
        print(row[0], file=f)
f.close()
