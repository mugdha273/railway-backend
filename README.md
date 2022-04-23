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

1. https://railway-backend.herokuapp.com/api/token/: to obtain token of an account.

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
2. SignUp/Registration: https://railway-backend.herokuapp.com/api/users/register/

```
curl --location --request POST 'http://127.0.0.1:8000/api/users/register/' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=62KjlMixjCOIaieXB4eUNjQidMxmzhsxHmcrjhXZpaPlzMvZb4EhCqdOQNg5t8wx' \
--data-raw '{
    "first_name": "Mugdha",
    "last_name": "Sharma" ,
    "email": "mugdhasharma0327@gmail.com",
    "phone_number": "9174400406",
    "date_of_birth": "2002-03-27",
    "password": "demopass",
    "password2": "demopass",
    "occupation": "student",
    "gender": "female",
    "city": "Indore" ,
    "state": "MP" ,
    "pincode": "452018"
}'
```
![image](https://user-images.githubusercontent.com/85048574/164679501-f959b33b-8096-47f5-a481-aad00b1a5f30.png)

 3. Login: https://railway-backend.herokuapp.com/api/users/login/

 ```
 curl --location --request POST 'https://railway-backend.herokuapp.com/api/users/login/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "mugdhasharma0327@gmail.com",
    "password": "demopass"
}'

 ```
 ![image](https://user-images.githubusercontent.com/85048574/164872876-bd7c11c5-0015-4b60-b77d-15c2eb90fe73.png)