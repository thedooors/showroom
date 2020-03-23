from datetime import datetime
from config import db, ma


class Content(db.Model):
    __tablename__ = "content"
    content_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    year = db.Column(db.String(256))
    restrict = db.Column(db.String(256))
    selectservice = db.Column(db.String(256))
    season = db.Column(db.String(256))
    duration = db.Column(db.String(512))
    rating = db.Column(db.String(256))
    kp_rating = db.Column(db.String(256))
    imdb_rating = db.Column(db.String(512))
    description = db.Column(db.String(1024))
    background = db.Column(db.String(512))
    poster = db.Column(db.String(512))
    whenontv = db.Column(db.String(512))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class ContentSchema(ma.ModelSchema):
    class Meta:
        model = Content
        sqla_session = db.session
