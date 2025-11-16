import sqlite3
conn = sqlite3.connect("crimehotspots.db")
cur = conn.cursor()
cur.execute("SELECT * FROM hotspots")


hotspots = cur.fetchall()
for hotspot in hotspots:
    print(hotspot)