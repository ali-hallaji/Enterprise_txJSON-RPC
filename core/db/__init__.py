from config.settings import EXIST_DB
from config.settings import DB_NAME
from mongo_drivers import MongoConnection


def MongoCursor(db):
    return MongoConnection().getCursor(db)


if EXIST_DB:
    cursor = MongoCursor(DB_NAME)
