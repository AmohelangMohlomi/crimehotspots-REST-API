from datetime import datetime

def get_timestamp():
    return datetime.utcnow().isoformat()

CRIME_HOTSPOTS = {
    "Hillbrow": {
        "province": "Gauteng",
        "city": "Johannesburg",
        "crime_types": ["robbery", "assault", "sexual_offence"],
        "danger_scale": 9.5,
        "last_reported": "2025-11-01T10:00:00Z",
        "report_count": 134,
        "data_source": "SAPS 2025 Q3",
        "timestamp": get_timestamp(),
    },
    "Nyanga": {
        "province": "Western Cape",
        "city": "Cape Town",
        "crime_types": ["murder", "theft", "sexual_offence"],
        "danger_scale": 8.9,
        "last_reported": "2025-10-22T16:30:00Z",
        "report_count": 95,
        "data_source": "SAPS 2025 Q3",
        "timestamp": get_timestamp(),
    },
    "Durban CBD": {
        "province": "KwaZulu-Natal",
        "city": "Durban",
        "crime_types": ["robbery", "gender_based_violence", "assault"],
        "danger_scale": 7.8,
        "last_reported": "2025-10-28T09:45:00Z",
        "report_count": 76,
        "data_source": "Crowd Reports + SAPS",
        "timestamp": get_timestamp(),
    },
}

def read_all():
    return list(CRIME_HOTSPOTS.values())