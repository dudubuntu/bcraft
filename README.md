# bcraft

Приложение поднимается на localhost
docker-compose up --build


Для получения токена отправить запрос 
POST /api/v1/auth/jwt/create/
{"username": "admin", "password": "1234"}

Далее
POST /api/v1/auth/jwt/verify/
{"token": "{{access_token}}"}   -   подставить сюда access_token, полученный от предыдущего шага

Также следует проставить заголовки запросов:
Content-Type: application/json
Authorization: JWT {{access_token}}


Описание api

Получить статистику по дням
GET /api/v1/statistics
    Принимает json вида
        {"from": "YYYY-MM-DD", "to": "YYYY-MM-DD"}
    Если значения не переданы, возвращается вся статистика в формате
        [{"date": "YYYY-MM-DD", "views": int, "clicks": int, "cost": float, "cpc": float, "cpm": float}, ...]

Сохранить статистику
POST /api/v1/statistics/save/
    Принимает json вида
        {"date": "YYYY-MM-DD", "views": int, "clicks": int, "cost": float}
        Все поля, кроме "date" обязательно

Сбросить статистику
DELETE /api/v1/statistics/reset/