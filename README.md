# README

# Dependencies

- [django-phonenumber-field](https://github.com/stefanfoulis/django-phonenumber-field)

# Run local development environment

Clone this repository:

```jsx
git pull https://github.com/anatolio-deb/sellspoint
```

Create a virtual environment:

```jsx
python3 -m venv venv
```

Activate a virtual environment:

```jsx
source ./venv/bin/activate
```

Install dependencies:

```jsx
pip install -r requirements.txt
```

Apply the migrations:

```jsx
python manage.py makemigrations && python manage.py migrate
```

Run the local development server:

```jsx
python manage.py runserver
```

# Querying an API

The API comes with two REST endpoints available.

## The Sells Point endpoint

- **URL**: `/api/sell-points/`
- **Methods available**: `GET`
- **Accepts**: a `phone_number` data field for an authorisation purposes
- **Returns**: a list of Sell Points by an existing Worker(User)

### Statuses

- **400** — The request is missing a `phone_number` field
- **404** — There’s no a Worker instance with a `phone_number` field coming in the request

## The Visits endpoint

- **URL**: `/api/visits/`
- **Methods available**: `POST`
- **Accepts**: a `phone_number` data field for an authorisation purposes, `pk` of the Sells Point instance, `longitude` and `latitude` data fields
- **Returns**: `pk` of created Visit instance and the `time` field

### Statuses

- **400** — The request is missing a `phone_number` field
- **404** — There’s no a Worker instance with a `phone_number` field coming in the request
- **201** — The Visit instance is created