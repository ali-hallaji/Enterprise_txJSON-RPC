from config.settings import EXIST_DB
from mongo_drivers import MongoConnectionGlobal
from mongo_drivers import MongoConnectionLocal
from mongo_drivers import MongoConnectionSelf


def MongoCursorDefsLocal(db):
    return MongoConnectionLocal().getCursor(db)


def MongoCursorDefsSelf(db):
    return MongoConnectionSelf().getCursor(db)


def MongoCursorDefsGlobal(db):
    return MongoConnectionGlobal().getCursor(db)


if EXIST_DB:
    cursor_local = MongoCursorDefsLocal('FIDS')
    cursor_global = MongoCursorDefsGlobal('FIDS')
    cursor_self = MongoCursorDefsSelf('FIDS')
