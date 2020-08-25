import os
import json
from config import db
from models import Content
from models import AppUsers

# Тестовый контент
with open("database.json", encoding='utf8') as database_file:    
    CONTENT = json.load(database_file)

# Удалить текущую
if os.path.exists("content.db"):
    os.remove("content.db")

# Создать по модели
db.create_all()

# Заполнить тестовыми данными
for element in CONTENT:
    p = Content(title=element.get("title"), title_season=element.get("title_season"), \
    restricty=element.get("restricty"), selectservice=element.get("selectservice"), \
    num_of_series=element.get("num_of_series"), trailer=element.get("trailer"), kp_rating=element.get("kp_rating"), \
    flag_status=element.get("flag_status"), actors=element.get("actors"), description=element.get("description"), \
    advertise=element.get("advertise"), poster=element.get("poster"), whenontv=element.get("whenontv"), \
    release_date=element.get("release_date"), country=element.get("country"), genre=element.get("genre"), \
    serial_duration=element.get("serial_duration"), series_list=element.get("series_list"), tv_channel=element.get("tv_channel"), \
    temp_col1=element.get("temp_col1"), temp_col2=element.get("temp_col2"))
    db.session.add(p)

db.session.commit()

APPUSERS = [{"usercode": "QWERTY", "waitlist": "0,1,2,3,4,5,14", "tg_col1": "658639130"},
    {"usercode": "ASDFGH", "waitlist": "12,14,15,34,35,213", "tg_col1": "658639427"},
    {"usercode": "ZXCVBN", "waitlist": "12,14,34,65,124,200", "tg_col1": "693432413"}]

for element in APPUSERS:
    appusers = AppUsers(usercode=element.get("usercode"), waitlist=element.get("waitlist"), tg_col1=element.get("tg_col1"))
    db.session.add(appusers)

db.session.commit()
