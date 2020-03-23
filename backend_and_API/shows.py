"""
shows.py содержит функции REST запросов, которые описаны в swagger.yml
"""

from flask import make_response, abort
from config import db
from models import Content, ContentSchema


def read_all():
    """
    Запрос /api/shows - возвращает все строки из бд в json формате
    """
    # Создаем список сериалов из наших данных
    content = Content.query.order_by(Content.content_id).all()

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
            "Сериала с данным id не найдено: {content_id}".format(content_id=content_id),
        )


def create(content):
    """
     Создает новую строку на основе отправленных данных (201 - ок, 406 - уже есть)
    """
    year = content.get("year")
    title = content.get("title")

    existing_content = (
        Content.query.filter(Content.year == year)
        .filter(Content.title == title)
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
            "Сериал {year} {title} уже добавлен, попробуйте изменить информацию".format(
                year=year, title=title
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
    year = content.get("year")
    title = content.get("title")

    existing_content = (
        Content.query.filter(Content.year == year)
        .filter(Content.title == title)
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
            "Такой же сериал - {year} {title} уже существует. Попробуйте другое описание".format(
                year=year, title=title
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

def read_fx():
    """
    Запрос /api/fx - возвращает все сериалы fx
    """
    # Запрос по id
    content = Content.query.filter(Content.selectservice == "FX").all()

    content_schema = ContentSchema(many=True)
    data = content_schema.dump(content).data
    return data

def read_netflix():
    """
    Запрос /api/netflix - возвращает все сериалы netflix
    """
    # Запрос по id
    content = Content.query.filter(Content.selectservice == "NETFLIX").all()

    content_schema = ContentSchema(many=True)
    data = content_schema.dump(content).data
    return data

def read_hbogo():
    """
    Запрос /api/hbogo - возвращает все сериалы HBO GO
    """
    # Запрос по id
    content = Content.query.filter(Content.selectservice == "HBO-GO").all()

    content_schema = ContentSchema(many=True)
    data = content_schema.dump(content).data
    return data

def read_amazon():
    """
    Запрос /api/amazon - возвращает все сереалы amazon
    """
    # Запрос по id
    content = Content.query.filter(Content.selectservice == "AMAZON").all()

    content_schema = ContentSchema(many=True)
    data = content_schema.dump(content).data
    return data

def read_amc():
    """
    Запрос /api/amc - возвращает все сереалы amc
    """
    # Запрос по id
    content = Content.query.filter(Content.selectservice == "AMC").all()

    content_schema = ContentSchema(many=True)
    data = content_schema.dump(content).data
    return data

def read_hulu():
    """
    Запрос /api/hulu - возвращает все сереалы hulu
    """
    # Запрос по id
    content = Content.query.filter(Content.selectservice == "HULU").all()

    content_schema = ContentSchema(many=True)
    data = content_schema.dump(content).data
    return data

def read_showtime():
    """
    Запрос /api/showtime - возвращает все сереалы showtime
    """
    # Запрос по id
    content = Content.query.filter(Content.selectservice == "SHOWTIME").all()

    content_schema = ContentSchema(many=True)
    data = content_schema.dump(content).data
    return data

def read_disney():
    """
    Запрос /api/disney - возвращает все сереалы disney plus
    """
    # Запрос по id
    content = Content.query.filter(Content.selectservice == "DISNEY").all()

    content_schema = ContentSchema(many=True)
    data = content_schema.dump(content).data
    return data

def read_apple():
    """
    Запрос /api/apple - возвращает все сереалы apple
    """
    # Запрос по id
    content = Content.query.filter(Content.selectservice == "APPLE").all()

    content_schema = ContentSchema(many=True)
    data = content_schema.dump(content).data
    return data

def read_cw():
    """
    Запрос /api/cw - возвращает все сереалы CW
    """
    # Запрос по id
    content = Content.query.filter(Content.selectservice == "CW").all()

    content_schema = ContentSchema(many=True)
    data = content_schema.dump(content).data
    return data

def read_others():
    """
    Запрос /api/others - возвращает все остальные сериалы
    """
    # Запрос по id
    content = Content.query.filter(Content.selectservice == "OTHERS").all()

    content_schema = ContentSchema(many=True)
    data = content_schema.dump(content).data
    return data

def read_abc():
    """
    Запрос /api/abc - возвращает все сереалы abc
    """
    # Запрос по id
    content = Content.query.filter(Content.selectservice == "ABC").all()

    content_schema = ContentSchema(many=True)
    data = content_schema.dump(content).data
    return data

def read_cbs():
    """
    Запрос /api/cbs - возвращает все сереалы cbs
    """
    # Запрос по id
    content = Content.query.filter(Content.selectservice == "CBS").all()

    content_schema = ContentSchema(many=True)
    data = content_schema.dump(content).data
    return data

def read_bbc():
    """
    Запрос /api/bbc - возвращает все сереалы bbc
    """
    # Запрос по id
    content = Content.query.filter(Content.selectservice == "BBC").all()

    content_schema = ContentSchema(many=True)
    data = content_schema.dump(content).data
    return data

def read_scyfi():
    """
    Запрос /api/scyfi - возвращает все сереалы sy-fy
    """
    # Запрос по id
    content = Content.query.filter(Content.selectservice == "SCY-FI").all()

    content_schema = ContentSchema(many=True)
    data = content_schema.dump(content).data
    return data

def read_now():
    """
    Запрос /api/now - возвращает все сериалы которые сейчас есть и на Stingray TV
    """
    # Запрос по id
    content = Content.query.filter(Content.selectservice == "СЕЙЧАС").all()

    content_schema = ContentSchema(many=True)
    data = content_schema.dump(content).data
    return data