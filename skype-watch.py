#!/usr/bin/python

import sys
import signal
from time import sleep
import sqlite3

if len(sys.argv) != 3:
    sys.stderr.write("Usage: %s <path to skype `main.db` file> <watch interval in seconds>\n" % sys.argv[0])
    sys.exit(1)

def int_handler(signum, frame):
    sys.exit(0)
signal.signal(signal.SIGINT, int_handler)

dbfilename = sys.argv[1]
interval = float(sys.argv[2])

conn = sqlite3.connect(dbfilename)
c = conn.cursor()
c.execute("select id from Messages where id = (select max(id) from Messages);")
(last_msg_id,) = c.fetchone()
while True:
    sleep(interval)
    for id, body in c.execute("select id, body_xml from Messages where id > ?;", (last_msg_id,)):
        last_msg_id = id
        print body
