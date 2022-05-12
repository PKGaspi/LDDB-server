# *Let's Dance! Dikir Barat* server
A python server application for the game *Let's Dance! Dikir Barat*. It manages
a database with different dance files, available for the community to access and
share their own. Access to those dances can be done through a REST API.

## Dependencies

- [SQLAlchemy](https://www.sqlalchemy.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](uvicorn.org)

## Setup

First, create a virtual enviroment.

```
python -m venv .venv
```
Activate the newly created virtual enviroment. Then, install the dependencies.

```
pip install -r requirements.txt
```

## Run

```
uvicorn main:app --reload
```

## API Documentation

*pending*

## Client

The client code is available in [PKGaspi/LDDB-client](https://github.com/PKGaspi/LDDB-client).