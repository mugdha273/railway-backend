# Railway-Backend

## Development 🔧

## Setup


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
*OR*

Raw Data: (Type your registered username and password in the body)

```
{
    "username": "<username>",
    "password": "<password>"
}
```

2.