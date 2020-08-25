from datetime import datetime
from config import db, ma


class Content(db.Model):
    __tablename__ = "content"
    content_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    title_season = db.Column(db.String(256))
    restricty = db.Column(db.String(256))
    selectservice = db.Column(db.String(256))
    num_of_series = db.Column(db.String(256))
    trailer = db.Column(db.String(512))
    kp_rating = db.Column(db.String(256))
    flag_status = db.Column(db.String(256))
    actors = db.Column(db.Text)
    description = db.Column(db.Text)
    advertise = db.Column(db.String(512))
    poster = db.Column(db.String(512))
    whenontv = db.Column(db.Text)
    release_date = db.Column(db.String(256))
    country = db.Column(db.String(256))
    genre = db.Column(db.String(256))
    serial_duration = db.Column(db.String(256))
    series_list = db.Column(db.Text)
    tv_channel = db.Column(db.String(256))
    temp_col1 = db.Column(db.String(256))
    temp_col2 = db.Column(db.String(512))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class ContentSchema(ma.ModelSchema):
    class Meta:
        model = Content
        sqla_session = db.session


class AppUsers(db.Model):
    __tablename__ = "appusers"
    user_id = db.Column(db.Integer, primary_key=True)
    usercode = db.Column(db.String(256), unique=True)
    waitlist = db.Column(db.String(1024))
    tg_col1 = db.Column(db.String(256))
    tg_col2 = db.Column(db.String(256))
    regdate = db.Column(db.DateTime, default=datetime.utcnow)
    user_col1 = db.Column(db.String(256))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class AppUsersSchema(ma.ModelSchema):
    class Meta:
        model = AppUsers
        sqla_session = db.session