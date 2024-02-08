# Проект Tube API Django
Задачей данного проекта является разработка API для сервиса Tube. В этом сервисе пользователи могут
опубликововать посты, комментировать их, делать подписки. API для этого сервиса реализует получение, создание, обновление и удаление информации. 

## Стек технологий:
```
Python 3.9.10
Django 3.2.16
djoser 2.1.0
```

## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:Ice444-222/Tube-API-Django.git
```

```
cd Tube-API-Django
```

Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
```
```
source env/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```
Запустить проект:

```
python3 manage.py runserver
```

## Примеры запросов

### Запрос списка всех публикаций
Получение списка всех публикаций Post. Выдача может работать с offset и limit.

**GET http://127.0.0.1:8000/api/v1/posts/**

**Response**
```
{
    "count": 123,
    "next": "http://api.example.org/accounts/?offset=400&limit=100",
    "previous": "http://api.example.org/accounts/?offset=200&limit=100",
    "results": [
        {
            "id": 0,
            "author": "string",
            "text": "string",
            "pub_date": "2021-10-14T20:41:29.648Z",
            "image": "string",
            "group": 0
        }
    ]
}
```

### Удаление публикации
Удаление публиакции Post по id. Возможно только авторизированным пользователем - автором публикации.

**Delete http://127.0.0.1:8000/api/v1/posts/{id}/**

**Request**
```
instance.author != self.request.user
```


**Response**
```
'Изменение чужого контента запрещено!'
```
**Request**
```
UserIsNotAuthenticated
```

**Response**
```
{
    "detail": "Authentication credentials were not provided."
}
```

### Создание комментария
Создание комментария к публикации Post по post_id. Может быть совершенна только авторизированным пользователем.

**Post http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/**

**Request**
```
{
"text": "string"
}
```

**Response**
```
{
"id": 0,
"author": "string",
"text": "string",
"created": "2023-01-08T11:48:20Z",
"post": 0
}
```

### Запрос подписок пользователя
Возвращает все подписки пользователя, сделавшего запрос. Анонимные запросы запрещены

**Get http://127.0.0.1:8000/api/v1/follow/**

**Response**
```
[
    {
    "user": "string",
    "following": "string"
    }
]
```

