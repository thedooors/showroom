from flask import render_template

import config


# Цепляем connex инстанс из config
connex_app = config.connex_app

# Считываем swagger.yml для конфигурации эндпоинтов
connex_app.add_api("swagger.yml")


# !!! Вместо index.html на вход home.html, чтобы не было конфликтов со swagger
@connex_app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    connex_app.run(debug=True)
