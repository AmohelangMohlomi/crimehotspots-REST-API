from datetime import datetime
from flask import abort,make_response

def get_timestamp():
    return datetime.now().isoformat()

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

def create(hotspot):
    """Create a new hotspot entry"""
    area = hotspot.get("area") 

    if not area:
        abort(400, "New hotspot must include an 'area' field")

    if area in CRIME_HOTSPOTS:
        abort(406, f"Hotspot '{area}' already exists")

    CRIME_HOTSPOTS[area] = {
        "province": hotspot.get("province"),
        "city": hotspot.get("city"),
        "crime_types": hotspot.get("crime_types", []),
        "danger_scale": hotspot.get("danger_scale"),
        "last_reported": hotspot.get("last_reported"),
        "report_count": hotspot.get("report_count", 0),
        "data_source": hotspot.get("data_source", "Unknown"),
        "timestamp": get_timestamp(),
    }

    return CRIME_HOTSPOTS[area], 201


def read_one(area):
    """Read a single hotspot"""
    if area in CRIME_HOTSPOTS:
        return CRIME_HOTSPOTS[area]
    else:
        abort(404, f"Hotspot '{area}' not found")


def update(area, hotspot):
    """Update an existing hotspot entry"""
    if area not in CRIME_HOTSPOTS:
        abort(404, f"Hotspot '{area}' not found")

    record = CRIME_HOTSPOTS[area]

    record["province"] = hotspot.get("province", record["province"])
    record["city"] = hotspot.get("city", record["city"])
    record["crime_types"] = hotspot.get("crime_types", record["crime_types"])
    record["danger_scale"] = hotspot.get("danger_scale", record["danger_scale"])
    record["last_reported"] = hotspot.get("last_reported", record["last_reported"])
    record["report_count"] = hotspot.get("report_count", record["report_count"])
    record["data_source"] = hotspot.get("data_source", record["data_source"])
    record["timestamp"] = get_timestamp()

    return record


def delete(area):
    """Delete an existing hotspot"""
    if area in CRIME_HOTSPOTS:
        del CRIME_HOTSPOTS[area]
        return make_response(f"Hotspot '{area}' successfully deleted", 200)
    else:
        abort(404, f"Hotspot '{area}' not found")