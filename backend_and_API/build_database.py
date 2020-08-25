import os
import json
from config import db
from models import Content

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
