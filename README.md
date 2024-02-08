# Project Tube API Django
The purpose of this project is to develop an API for the Tube service. 
In this service, users can publish posts, comment on them, and make subscriptions. 
The API for this service implements the retrieval, creation, updating, and deletion of information.

## Technology Stack:
```
Python 3.9.10
Django 3.2.16
djoser 2.1.0
```

## How to run the project:
Clone the repository and navigate to it in the command line:
```
git clone git@github.com:Ice444-222/Tube-API-Django.git
```

```
cd Tube-API-Django
```

Create and activate a virtual environment:
```
python3 -m venv env
```
```
source env/bin/activate
```
Install dependencies from the requirements.txt file:
```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Apply migrations:

```
python3 manage.py migrate
```
Run the project:

```
python3 manage.py runserver
```

## Example Requests

### Request for the list of all publications
Get a list of all Post publications. Pagination can work with offset and limit.

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

### Deletion of a publication
Delete the Post publication by id. Only an authorized user who is the author of the publication can perform this action.

**Delete http://127.0.0.1:8000/api/v1/posts/{id}/**

**Request**
```
instance.author != self.request.user
```


**Response**
```
'Changing someone else's content is forbidden!'
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

### Creating a comment
Create a comment for the Post publication by post_id. Only an authorized user can perform this action.

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

### User subscription request
Returns all subscriptions of the user making the request. Anonymous requests are not allowed.

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

