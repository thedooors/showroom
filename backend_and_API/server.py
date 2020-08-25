from flask import render_template

import config
from models import Content
from models import AppUsers
import requests
import time
# import atexit

# from apscheduler.schedulers.background import BackgroundScheduler

# Цепляем connex инстанс из config
connex_app = config.connex_app

# Считываем swagger.yml для конфигурации эндпоинтов
connex_app.add_api("swagger.yml")

BOT_TOKEN = "PUTYOURBOTTOKEN"

# !!! Вместо index.html на вход home.html, чтобы не было конфликтов со swagger
@connex_app.route("/")
def home():
    return render_template("home.html")

@connex_app.route("/logout")
def logout():
    return render_template("login.html")

@connex_app.route('/streamservice/<service_name>')
def streamservice(service_name):
    required_services = ["FX", "NETFLIX", "AMC", "HBO", "AMAZON", "SHOWTIME", \
        "DISNEY", "APPLE-TV", "THE-CW", "ABC", "SYFY", "BBC", "CBS", "FOX", "HULU"]
    if service_name in required_services:
        data = Content.query.filter(Content.selectservice == service_name).all()
        return render_template("streamservice.html", service_name=service_name, data=data)
    else:
        return render_template("404.html")

@connex_app.route('/users_info')
def users_info():
    app_users = AppUsers.query.order_by(AppUsers.user_id.desc()).all()
    return render_template("users_info.html", app_users=app_users)

@connex_app.route('/user_information/<usercode>')
def user_information(usercode):
    user_information = AppUsers.query.filter(AppUsers.usercode == usercode).one_or_none()
    waitlist = user_information.waitlist 
    try:
        if waitlist == "":
            shows_waitlist = {}
            return render_template("waitlist.html", usercode=usercode, shows_waitlist=shows_waitlist, most_frequent_service="-", \
            number_of_shows="0", most_frequent_genre="-", most_frequent_country="-")
        array_waitlist = [int(s) for s in waitlist.split(',')]
    except ValueError:
        shows_waitlist = {}
        return render_template("waitlist.html", usercode=usercode, shows_waitlist=shows_waitlist, most_frequent_service="-", \
            number_of_shows="0", most_frequent_genre="-", most_frequent_country="-")
    except AttributeError:
        shows_waitlist = {}
        return render_template("waitlist.html", usercode=usercode, shows_waitlist=shows_waitlist, most_frequent_service="-", \
            number_of_shows="0", most_frequent_genre="-", most_frequent_country="-")
    shows_waitlist = Content.query.filter(Content.content_id.in_(array_waitlist)).all()
    number_of_shows = str(len(shows_waitlist))
    services_list = [shows.selectservice for shows in shows_waitlist]
    most_frequent_service = max(set(services_list), key = services_list.count)
    genres_list = [shows.genre for shows in shows_waitlist]
    most_frequent_genre = max(set(genres_list), key = genres_list.count)
    country_list = [shows.country for shows in shows_waitlist]
    most_frequent_country = max(set(country_list), key = country_list.count)
    return render_template("waitlist.html", usercode=usercode, shows_waitlist=shows_waitlist, most_frequent_service=most_frequent_service, \
        number_of_shows=number_of_shows, most_frequent_genre=most_frequent_genre, most_frequent_country=most_frequent_country)

@connex_app.route('/analytics')
def analytics():
    users = AppUsers.query.order_by(AppUsers.user_id.desc()).all()
    number_of_users = str(len(users))
    tg_col1 = [shows.tg_col1 for shows in users]
    subscribed_on_bot = len(list(filter(None, tg_col1)))
    allwaitlists = [shows.waitlist for shows in users]
    print(allwaitlists)
    allwaitliststring = ','
    allwaitliststring = allwaitliststring.join(allwaitlists)
    array_waitlist = [str(s) for s in allwaitliststring.split(',')]
    array_waitlist = list(filter(lambda a: a != "", array_waitlist))
    most_anticipated = max(set(array_waitlist), key = array_waitlist.count)
    try:
        most_anticipated_content = Content.query.filter(Content.content_id == int(most_anticipated)).one_or_none()
    except ValueError:
        most_anticipated_content = Content.query.filter(Content.content_id == 1).one_or_none()
    if most_anticipated_content is None:
        most_anticipated_content = Content.query.filter(Content.content_id == 1).one_or_none()
    return render_template("analytics.html", number_of_users=number_of_users, subscribed_on_bot=subscribed_on_bot, \
        most_anticipated_content=most_anticipated_content)

# Обновляем телеграм id chat'ов пользователей в боте
# def telegram_update_users():
#     MethodGetUpdates = 'https://api.telegram.org/bot{token}/getUpdates?limit=10'.format(token=BOT_TOKEN)
#     response = requests.post(MethodGetUpdates)
#     result = response.json()
#     if result["ok"]:
#         for messages in result["result"]:
#             if messages["message"]["text"] == "/start":
#                 start_message = "Добрай день! Введите ваш Usercode после /"
#                 MethodSendHello = 'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={start_message}'.format(\
#                     token=BOT_TOKEN, chat_id=messages["message"]["chat"]["id"], start_message=start_message)
#                 continue
#             if messages[i]["message"]["entities"][0]["type"] == "bot_command" and messages["message"]["text"] != "/start":
#                 try:
#                     user_information = AppUsers.query.filter(AppUsers.usercode == usercode).one_or_none()
#                     if user_information.usercode == messages["message"]["text"]:
#                         ок_message = "Вы успешно подписались на обновления!"
#                         MethodSendHello = 'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={start_message}'.format(\
#                             token=BOT_TOKEN, chat_id=messages["message"]["chat"]["id"], start_message=ок_message)
#                         user_information.tg_col1 = messages["message"]["chat"]["id"]
#                         db.session.add(new_content)
#                         db.session.commit()
#                     else:
#                         ок_message = "Данного пользователя не существует! Введите ваш Usercode после /"
#                         continue
#                 except:
#                     return "Server Error: Please restart the Showroom Bot"

# def telegram_notify():
#     MethodGetUpdates = 'https://api.telegram.org/bot{token}/getUpdates?limit=10'.format(token=BOT_TOKEN)
#     response = requests.post(MethodGetUpdates)
#     result = response.json()
#     user_telegram = AppUsers.query.filter(AppUsers.usercode != None).one_or_none()
#     content = Content.query.filter(Content.flag_status == "NOW").all()
#     for i in user_telegram:
#         try:
#             notify = content.title + " " + content.whenontv
#             MethodSendNotify = 'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={start_message}'.format(\
#                     token=BOT_TOKEN, chat_id=user_telegram.tg_col1, notify=notify)
#         except:
#             return "Server Error: Please restart the Showroom Bot"
                
# scheduler = BackgroundScheduler()
# scheduler.add_job(func=telegram_update_users, trigger="interval", seconds=5)
# sched.add_job(func=telegram_notyfy, 'cron', day_of_week='mon-fri', hour=23, minute=30)
# scheduler.start()
# Отключить scheduller после выхода
# atexit.register(lambda: scheduler.shutdown())

if __name__ == "__main__":
    connex_app.run(debug=True)
