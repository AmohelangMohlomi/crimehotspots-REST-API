import sqlite3
conn = sqlite3.connect("crimehotspots.db")
hotspots = [
    "1, 'Hillbrow', 'Gauteng', 'Johannesburg', '[robbery, assault, sexual_offence]','9.5','2025-11-01T10:00:00Z','134','SAPS 2025 Q3','2025-11-16T19:13:18.590656'",
    "2, 'Nyanga', 'Western Cape', 'Cape Town','[murder, theft, sexual_offence]',' 8.9','2025-10-22T16:30:00Z','95','SAPS 2025 Q3','2025-11-16T19:13:18.590656'",
    "3, 'Durban CBD', 'KwaZulu-Natal', 'Durban','[robbery, gender_based_violence, assault]','7.8','2025-10-28T09:45:00Z','76','Crowd Reports + SAPS','2025-11-16T19:13:18.590656'",
]
for hotspot in hotspots:
    insert_cmd = f"INSERT INTO hotspots VALUES ({hotspot})"
    conn.execute(insert_cmd)


conn.commit()
