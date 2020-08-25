"""
shows.py содержит функции REST запросов, которые описаны в swagger.yml
"""

from flask import make_response, abort
from config import db
from models import Content, ContentSchema
from models import AppUsers, AppUsersSchema


def read_all():
    """
    Запрос /api/shows - возвращает все строки из бд в json формате
    """
    # Создаем список сериалов из наших данных
    content = Content.query.order_by(Content.content_id.desc()).all()

    # Сериализуем данные для ответа
    content_schema = ContentSchema(many=True)
    data = content_schema.dump(content).data
    return data


def read_one(content_id):
    """
    Запрос /api/shows/{content_id} - возвращает строку по id (param)
    """
    # Запрос по id
    content = Content.query.filter(Content.content_id == content_id).one_or_none()

    # Проверка на наличие id
    if content is not None:

        # Сериализация
        content_schema = ContentSchema()
        data = content_schema.dump(content).data
        return data

    # Ошибка, если нет
    else:
        abort(
            404,
            "Show with this id not found: {content_id}".format(content_id=content_id),
        )

def read_from_string_array(string_array_waitlist):
    """
    Запрос /api/shows/string_array/{string_array_waitlist} - возвращает контент по массиву id
    """
    # Запрос по id
    try:
        array_waitlist = [int(s) for s in string_array_waitlist.split(',')]
    except ValueError:
        abort(
            404,
            "Waitlist empty or wrong format. Format of waitlist string should be - 1,2,3,4,5 etc",
        )
    except AttributeError:
        abort(
            404,
            "Waitlist empty or wrong format. Format of waitlist string should be - 1,2,3,4,5 etc",
        )

    content = Content.query.filter(Content.content_id.in_(array_waitlist)).all()

    # Проверка на наличие id
    if content is not None:

        # Сериализация
        content_schema = ContentSchema(many=True)
        data = content_schema.dump(content).data
        return data

    # Ошибка, если нет
    else:
        abort(
            404,
            "Empty show list with this IDs",
        )

def create(content):
    """
     Создает новую строку на основе отправленных данных (201 - ок, 409 - уже есть)
    """
    title = content.get("title")
    title_season = content.get("title_season")

    existing_content = (
        Content.query.filter(Content.title == title)
        .filter(Content.title_season == title_season)
        .one_or_none()
    )

    # Проверка на существование
    if existing_content is None:

        # Добавляем
        schema = ContentSchema()
        new_content = schema.load(content, session=db.session).data
        db.session.add(new_content)
        db.session.commit()

        # Сериализация
        data = schema.dump(new_content).data

        return data, 201

    # Ошибка, если существует
    else:
        abort(
            409,
            "Сериал {title} {title_season} уже добавлен, попробуйте изменить информацию".format(
                title=title, title_season=title_season
            ),
        )


def update(content_id, content):
    """
    Обновляет инфо о сериале. Проверяется существование id и отсутсвие дупликатов при обновлении

    :param content_id:   Id сериала для изменения
    :param content:      content для добавления
    :return:            обновленный контент
    """
    update_content = Content.query.filter(
        Content.content_id == content_id
    ).one_or_none()
    title = content.get("title")
    title_season = content.get("title_season")

    existing_content = (
        Content.query.filter(Content.title == title)
        .filter(Content.title_season == title_season)
        .one_or_none()
    )

    if update_content is None:
        abort(
            404,
            "Сериал по данному Id не найден: {content_id}".format(content_id=content_id),
        )
    elif (
        existing_content is not None and existing_content.content_id != content_id
    ):
        abort(
            409,
            "Такой же сериал - {title} {title_season} уже существует. Попробуйте другое описание".format(
                title=title, title_season=title_season
            ),
        )
    else:
        schema = ContentSchema()
        update = schema.load(content, session=db.session).data

        # Устанавливаем id как у обновляемого
        update.content_id = update_content.content_id

        # Мерджим старое с новым и коммитим в db
        db.session.merge(update)
        db.session.commit()

        # возвращаем обновленный контент
        data = schema.dump(update_content).data

        return data, 200


def delete(content_id):
    """
    Удаление строки по id (200 - ок, 404 - не найден id)
    """
    # Запрос по id
    content = Content.query.filter(Content.content_id == content_id).one_or_none()

    # Удаление
    if content is not None:
        db.session.delete(content)
        db.session.commit()
        return make_response(
            "Сериал {content_id} удален".format(content_id=content_id), 200
        )

    # Не найден
    else:
        abort(
            404,
            "Нет сериала с таким Id: {content_id}".format(content_id=content_id),
        )

def read_service(service_name):
    """
    Запрос /api/services/{service_name} - возвращает все сериалы fx
    """
    # Запрос по id
    content = Content.query.filter(Content.selectservice == service_name.upper()).all()

    content_schema = ContentSchema(many=True)
    data = content_schema.dump(content).data
    return data

def read_now():
    """
    Запрос /api/now - возвращает все сериалы которые сейчас есть по тв на каналах Stingray TV
    """
    # Запрос по id
    content = Content.query.filter(Content.flag_status == "NOW").all()

    content_schema = ContentSchema(many=True)
    data = content_schema.dump(content).data
    return data

def get_appuser(usercode):
    """
     Информация о пользователе - api/appusers/{usercode}
    """

    existing_usercode = (
        AppUsers.query.filter(AppUsers.usercode == usercode).one_or_none()
    )

    if existing_usercode is None:
        abort(
            409,
            "Usercode {usercode} does not exists".format(
                usercode=usercode
            ),
        )
    else:
        users_schema = AppUsersSchema()
        data = users_schema.dump(existing_usercode).data

        return data, 201


def create_new_appuser(usercode):
    """
     Создает нового пользователя сгенерированного при первом запуске приложения (201 - ок, 409 - уже есть)
    """

    existing_usercode = (
        AppUsers.query.filter(AppUsers.usercode == usercode).one_or_none()
    )

    # Проверка на существование
    if existing_usercode is None:

        # Добавляем
        appusers = AppUsers(usercode=usercode, waitlist="empty")
        db.session.add(appusers)
        db.session.commit()

        # Сериализация
        new_user = (
            AppUsers.query.filter(AppUsers.usercode == usercode).one_or_none()
        )
        users_schema = AppUsersSchema()
        data = users_schema.dump(new_user).data

        return data, 201

    # Ошибка, если существует
    else:
        abort(
            409,
            "Usercode {usercode} already exists".format(
                usercode=usercode
            ),
        )


def create_new_waitlist(usercode, waitlist):
    """
     Обновляет лист ожиданий пользователя - api/waitlists/{usercode}/{waitlist}
    """

    user_by_usercode = (
        AppUsers.query.filter(AppUsers.usercode == usercode).one_or_none()
    )

    if waitlist is None:
        abort(
            409,
            "Waitlist of {usercode} is None - Post query failed".format(
                usercode=usercode
            ),
        )

    # Ошибка - если пользователя не существует
    if user_by_usercode is None:
        abort(
            409,
            "Usercode {usercode} does not exists".format(
                usercode=usercode
            ),
        )

    # Обновляем лист ожиданий
    else:
        user_by_usercode.waitlist = waitlist
        db.session.commit()
        # Сериализация
        user_with_updated_waitlist = (
            AppUsers.query.filter(AppUsers.usercode == usercode).one_or_none()
        )
        users_schema = AppUsersSchema()
        data = users_schema.dump(user_with_updated_waitlist).data

        return data, 201

def get_waitlist(usercode):
    """
    Запрос /api/waitlists/{usercode} - возвращает waitlist контент по usercode
    """
    user_by_usercode = (
        AppUsers.query.filter(AppUsers.usercode == usercode).one_or_none()
    )

    if user_by_usercode is None:
        abort(
            409,
            "Usercode {usercode} does not exists".format(
                usercode=usercode
            ),
        )

    string_array_waitlist = user_by_usercode.waitlist
    # Запрос по id
    try:
        array_waitlist = [int(s) for s in string_array_waitlist.split(',')]
    except ValueError:
        abort(
            404,
            "Waitlist empty or wrong format. Format of waitlist string should be - 1,2,3,4,5 etc",
        )
    except AttributeError:
        abort(
            404,
            "Waitlist empty or wrong format. Format of waitlist string should be - 1,2,3,4,5 etc",
        )

    content = Content.query.filter(Content.content_id.in_(array_waitlist)).all()

    # Проверка на наличие id
    if content is not None:

        # Сериализация
        content_schema = ContentSchema(many=True)
        data = content_schema.dump(content).data
        return data

    # Ошибка, если нет
    else:
        abort(
            404,
            "Empty show list with this IDs",
        )