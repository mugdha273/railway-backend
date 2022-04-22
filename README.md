# Railway-Backend

## Development 🔧

## Setup

```
git clone https://github.com/mugdha273/railway-backend.git
cd railway-backend
```

### For setting virtual environment

```sh
virtualenv venv
```

### For activating virtual environment in Windows

```sh
venv/Scripts/activate
```

### For activating virtual environment in Linux and macOS

```sh
source venv/bin/activate
```

### For deactivating virtual environment
```sh
deactivate
```
After creating virtual environment

### Start

```sh
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```


## APIs in Use:

1. http://127.0.0.1:8000/api/token/: to obtain token of an account.

Curl Request: (Type your registered username and password in the body)
```
curl --location --request POST 'http://127.0.0.1:8000/api/token/' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=62KjlMixjCOIaieXB4eUNjQidMxmzhsxHmcrjhXZpaPlzMvZb4EhCqdOQNg5t8wx' \
--data-raw '{
    "username": "<username>",
    "password": "<password>"
}'
```
2.