import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))

# Создаем connexion инстанс для REST
connex_app = connexion.App(__name__, specification_dir=basedir)

# Из него просимся к инстансу Flaskа
app = connex_app.app

# Путь к базе данных sqlite для SqlAlchemy
sqlite_url = "sqlite:////" + os.path.join(basedir, "content.db")

# Конфиги SqlAlchemy
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = sqlite_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Подключаем SqlAlchemy
db = SQLAlchemy(app)

# Подключаем Marshmallow
ma = Marshmallow(app)
