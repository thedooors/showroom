# Showroom (by the Doors team)

![Showroom Logo](https://i.ibb.co/Z6PV4D3/2d538a9d-c383-48a7-8a5b-4cbb45cd518f-200x200.png)
> Наше приложение Showroom обладает клиент-серверной архитектурой.

### Клиентское приложение (JavaScript, QML) - папка favshow
Агрегирует информацию о сериалах с зарубежных стриминговых сервисов (Netflix, Amazon Prime Videos, Hulu, Disney+ etc.), позволяет добавлять передачи в ожидание, а также отображает какие из этих шоу будут на этой неделе на российском спутниковом телевидении.

Главный экран отображает сериалы, которые на этой неделе будут по ТВ и во сколько. Остальные вкладки содержат информацию о новых и популярных шоу на различных стриминговых сервисах. Нажав на постер, можно посмотреть расписание выхода серий, состояние на данный момент (продолжается, завершено, заморожено, премьера), трейлер, описание, рейтинг и другое, поставить проект в ожидание с последующим обновлением.

`GIF`

![Appvid.gif](https://github.com/thedooors/showroom/blob/master/Appvid.gif)

`SCREENSHOT`

![Screenshot](https://i.ibb.co/fp7FWYQ/Deepin-Screenshot-select-area-20200825113059.png)

### Контент-менеджмент и модерация (Flask, jQuery) - папка backend_and_API http://35.228.3.191:9090/

Для этих целей разработан backend и API (Flask, Connexion (Python)) – при изменении данных на нем, контент будет также меняться и на клиенте. Сервер задеплоен на Google Cloud Platform, автообновление контента производится выполнением скрэппинг-скриптов (filmru_parse.py) через cron каждую неделю (когда обновляется телепередача). Back-end написан с соблюдением паттерна разделения данных Model View Controller (клиентская логика MVC в файле `home.js`). Модератор может изменять автоматически внесенный контент и добавлять свой. Можно добавлять описание, ссылку на трейлер, рейтинг, график выхода, рекламный постер, который отобразится внизу страницы с контентом (например, изображение подталкивающее пользователя купить расширенный пакет каналов или сменить тариф на приставке (вариант монетизации приложения)).

![Servergif](https://github.com/thedooors/showroom/blob/master/servervid.gif)

### API приложения (Connexion, Marshmellow, Swagger)
API обладает всем спектром запросов GET, POST, PUT, DELETE для отображения и изменения контента – данные сериализуются и возвращаются в формате JSON. В последствии API можно использовать для внедрения на другие типы устройств. Функции API написаны на языке программирования Python (файл `shows.py`), их описание содержится в файле `swagger.yml`. API автоматически задокументирован.

![APIImage](https://i.ibb.co/ZJmVLsS/2020-03-23-22-08-18.png) 


### Мобильное приложение компаньон (ShowroomApp.apk)
Просто использует функционал API.
`Скриншоты`

![Screen1](https://i.ibb.co/N2PfYL1/Deepin-Screenshot-select-area-20200825113122.png)
![mobile.gif](https://github.com/thedooors/showroom/blob/master/mobile.gif)

### Парсинг данных при помощи Selenium
Рекомендую запускать не на сервере, а на десктопе с включенным расширением AdBlock
`PS`
Ссылка на панель управления контентом - http://35.228.3.191:9090/
