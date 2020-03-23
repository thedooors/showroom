import os
from config import db
from models import Content

# Тестовый контент
CONTENT = [
    {"year": "Ведьмак", "title": "The Witcher", "restrict": "18", \
    "selectservice": "NETFLIX", "season": "2", "duration": "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerEscapes.mp4", \
    "rating": "5", "kp_rating": "NOW", "imdb_rating": "89", \
    "description": "Описание Ведьмака", "background": "https://www.film.ru/sites/default/files/styles/thumb_1024x450/public/movies/frames/20948850-1145721.jpg", "poster": "https://www.film.ru/sites/default/files/movies/posters/20948850-1144190.jpg", \
    "whenontv": "К сожалению, на этой неделе нет в эфире"},
    {"year": "Очень странные дела", "title": "Stranger Things", "restrict": "12", \
    "selectservice": "AMAZON", "season": "4", "duration": "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerFun.mp4", \
    "rating": "5", "kp_rating": "NOW", "imdb_rating": "80", \
    "description": "Описание ОСД", "background": "https://www.film.ru/sites/default/files/styles/thumb_1024x450/public/movies/frames/13948241-1003333.jpg", "poster": "https://www.film.ru/sites/default/files/movies/posters/13948241-1112209.jpg", \
    "whenontv": "К сожалению, на этой неделе нет в эфире"},
    {"year": "Во все тяжкие", "title": "Breaking Bad", "restrict": "16", \
    "selectservice": "HBO-GO", "season": "-", "duration": "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerJoyrides.mp4", \
    "rating": "5", "kp_rating": "NOW", "imdb_rating": "80", \
    "description": "Описание Во все Тяжкие", "background": "https://www.film.ru/sites/default/files/styles/thumb_1024x450/public/movies/frames/Breaking-Bad-42.jpg", "poster": "https://www.film.ru/sites/default/files/movies/posters/1628896-904328.jpg", \
    "whenontv": "FX Live - 16 Марта - Пн - 23:30"},
]

# Удалить текущую
if os.path.exists("content.db"):
    os.remove("content.db")

# Создать по модели
db.create_all()

# Заполнить тестовыми данными
for element in CONTENT:
    p = Content(title=element.get("title"), year=element.get("year"), \
    restrict=element.get("restrict"), selectservice=element.get("selectservice"), \
    season=element.get("season"), duration=element.get("duration"), rating=element.get("rating"), \
    kp_rating=element.get("kp_rating"), imdb_rating=element.get("imdb_rating"), description=element.get("description"), \
    background=element.get("background"), poster=element.get("poster"), whenontv=element.get("whenontv"))
    db.session.add(p)

db.session.commit()
