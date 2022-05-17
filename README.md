# *Let's Dance! Dikir Barat* server
A python server application for the game *Let's Dance! Dikir Barat*. It manages
a database with different dance files, available for the community to access and
share their own. Access to those dances can be done through a REST API.

## Dependencies

Python modules for runtime:
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](uvicorn.org)
- [Python-multipart](https://andrew-d.github.io/python-multipart/)
- [Python-dotenv](https://pypi.org/project/python-dotenv/)
- [Psycopg2](https://pypi.org/project/psycopg2/)

Python modules for development:
- [Alembic](https://alembic.sqlalchemy.org/en/latest/)

## Setup

First, make sure to use python 3.10+.

```console
$ python --version
Python 3.10.4
```


Then, create a virtual enviroment.

```console
$ python -m venv .venv
```
Activate the newly created virtual enviroment. Then, install the dependencies.

```console
$ pip install -r requirements.txt
```

Finally, setup a `.env` file with the following or similar structure.
```
MEDIA_PATH="${HOME}/lddb"
DB_URL="postgresql+psycopg2://lddb@localhost/lddb_db"
DANCES_PATH="${MEDIA_PATH}/dances"
SONGS_PATH="${MEDIA_PATH}/songs"
```
## Run

```
uvicorn lddb.main:app --reload
```

## API Documentation

*pending*

## Client

The client code is available in [PKGaspi/LDDB-client](https://github.com/PKGaspi/LDDB-client).