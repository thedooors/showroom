import time
import json
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
import os
import urllib.request
from PIL import Image
import random

options = webdriver.ChromeOptions()
# Run with ad_block in Visual_mode
options.add_extension('extension_1_4_3_0.crx')
# options.add_argument("--headless")
# Запуск без окна - driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome(options=options)
# Внесите сюда путь до папки с изображениями на сервере
PATH_TO_POSTERS_FOLDER_ON_SERVER = "http://35.228.3.191:9090/static/posters/"
SAVE_PATH = "posters/"
serial_info = []
title_season = ""
poster = "apps/favshow/resources/catalog_default_172x264.png"
advertise = "advertise"
restricty = "18"
description = "Нет описания"
release_date = "2020"
country = "USA"
genre = "Не определен"
num_of_series = "-"
serial_duration = "-"
actors = "-"
kp_rating = "3"
imdb_rating = "-"
series_list = "Нет списка серий"
flag_status = "GO"
TRAILERS_STANDART = ["https://dump.video/i/fitlEm.mp4", "https://dump.video/i/r1fkpz.mp4", "https://dump.video/i/K3jLY8.mp4"]
whenontv = "Пока нет на ТВ"
tv_channel = ""
temp_col1 = ""
temp_col2 = ""
ADVERTISE_BANNERS = ["advertise", "advertise1", "advertise2"]
with open("showlist.json", encoding='utf8') as showlist_file:    
    showlist = json.load(showlist_file)
for showinfo in showlist:
    link = showinfo["link"]
    title = showinfo["title"]
    selectservice = showinfo["selectservice"]
    driver.get(link)
    try:
        title_season = driver.find_element_by_class_name('serial-header_title').text
    except NoSuchElementException:
        print("ERROR - Title with season not found - use standart")
    try:
        poster = driver.find_element_by_class_name('serial-summary_poster-image').get_attribute('src')
        head, tail = os.path.split(poster)
        poster_path = os.path.join(SAVE_PATH, "full" + tail)
        urllib.request.urlretrieve(poster, poster_path)
        img = Image.open(poster_path).convert('RGB')
        new_img = img.resize((172,264))
        new_img.save(os.path.join(SAVE_PATH, tail), "JPEG", optimize=True)
        poster = os.path.join(PATH_TO_POSTERS_FOLDER_ON_SERVER, tail)
    except NoSuchElementException:
        print("ERROR - poster not found - use standart")
    try:
        restricty = str(driver.find_element_by_class_name('serial-summary_poster-age-rating').text[:-1])
    except NoSuchElementException:
        print("ERROR - Age restricty not found - use standart")
    try:
        description = driver.find_element_by_class_name('serial-content_container').text
    except NoSuchElementException:
        print("ERROR - description  not found - use standart")
    try:
        show_info = driver.find_element_by_class_name('serial-summary_table').text
        show_info_list = show_info.splitlines()
        for elem in show_info_list:
            if "Дата выхода " in elem:
                release_date = elem.partition("Дата выхода ")[2]
            if "Страна " in elem:
                country = elem.partition("Страна ")[2]
            if "Жанр " in elem:
                genre = elem.partition("Жанр ")[2]
            if "Количество серий " in elem:
                num_of_series = elem.partition("Количество серий ")[2]
            if "Продолжительность " in elem:
                serial_duration = elem.partition("Продолжительность ")[2]
            if "Актёры " in elem:
                actors = elem.partition("Актёры ")[2]
            if "Рейтинг КП " in elem:
                kp_rating = str(int(float(elem.partition("Рейтинг КП ")[2])/2) + 1)
                if kp_rating == "6":
                    kp_rating = "4"
            if "Рейтинг IMDB " in elem:
                imdb_rating = elem.partition("Рейтинг IMDB ")[2]
    except NoSuchElementException:
        print("ERROR - table not found - use standart")
    try:
        series_list = driver.find_element_by_class_name('serial-issue').text
    except NoSuchElementException:
        print("ERROR - list of series not found - use standart")
    serial_info.append({'title': title, 'selectservice': selectservice, 'title_season': title_season, \
        'poster': poster, 'advertise': random.choice(ADVERTISE_BANNERS), 'restricty': restricty, 'description': description, 'release_date': release_date, \
            'country': country, 'genre': genre, 'num_of_series': num_of_series, 'serial_duration': serial_duration, \
                'actors': actors, 'kp_rating': kp_rating, 'imdb_rating': imdb_rating, 'series_list': series_list, 'flag_status': flag_status, \
                    'trailer': random.choice(TRAILERS_STANDART), 'whenontv': whenontv, 'tv_channel': tv_channel, 'temp_col1': temp_col1, 'temp_col2': temp_col2})
print("Сохраняем в database.json")
print("Кол-во записей - " + str(len(serial_info)))
with open('database.json', 'w', encoding='utf8') as f:
    json.dump(serial_info, f, ensure_ascii=False)
print("Done")
