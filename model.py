from datetime import datetime
from config import db, ma

class Hotspot(db.Model):
    __tablename__ = "hotspots"
    area = db.Column(db.String(255))
    province = db.Column(db.String(255))
    city = db.Column(db.String(255))
    crime_types = db.Column(db.String(255))
    danger_scale = db.Column(db.Float)
    last_reported = db.Column(db.DateTime, default=datetime.utcnow)
    report_count = db.Column(db.Integer, default=0)
    data_source = db.Column(db.String(255))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

class HotspotSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Hotspot
        load_instance = True
        sqla_session = db.session

hotspot_schema = HotspotSchema()
hotspots_schema = HotspotSchema(many=True)