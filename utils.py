import secrets
from postgres import Postgres
import json


def generate_id():
    return str(secrets.token_hex(4)).upper()


def db_connect(DSN: str):
    return Postgres(url=DSN)


def load_config(file: str):
    with open(file, "r") as f:
        return json.load(f)
