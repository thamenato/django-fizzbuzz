# django-fizzbuzz

This projects uses [Django REST Framework](https://www.django-rest-framework.org) 
to implement an API for _fizzbuzzes_

The following endpoints are implemented:

* GET /fizzbuzz to list all fizzbuzz objects
* GET /fizzbuzz/123 to retrieve a single fizz buzz object
* POST /fizzbuzz to create a new fizzbuzz object

More information on fizzbuzz [here](https://fizzbuzz.docs.apiary.io)

## Running the project

After cloning (or downloading) the repository -

1. Create the python virtual env

```shell
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
cd myproject
```
OR
```shell
poetry install
poetry shell
cd myproject
```

2. Start the database and create superuser

```shell
python manage.py migrate
python manage.py createsuperuser
```

3. Run the server with `python manage.py runserver`

4. To run the test suite `python manage.py test`