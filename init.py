import sqlite3
conn = sqlite3.connect("crimehotspots.db")
columns = [
    "id INTEGER PRIMARY KEY",
    "area VARCHAR",
    "province VARCHAR",
    "city VARCHAR",
    "crime_types VARCHAR",
    "danger_scale FLOAT",
    "last_reported DATETIME",
    "report_count INTEGER",
    "data_source VARCHAR",
    "timestamp DATETIME",
]
create_table_cmd = f"CREATE TABLE hotspots ({','.join(columns)})"
conn.execute(create_table_cmd)