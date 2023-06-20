# (c) @EverythingSuckz | @AbirHasan2005

from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()


class Var(object):
    API_ID = int(getenv('API_ID', '7763257'))
    API_HASH = str(getenv('API_HASH', '52c9cbf4b4ee78eda09eb3d9ac0673d7'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', '5887558540:AAHnfHALLLW5cHVuLUDm1zT7bn7nsnUT5tQ'))
    SESSION_NAME = str(getenv('SESSION_NAME', 'VBStreamBot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1001861476160'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    OWNER_ID = int(getenv('OWNER_ID', '1441767180'))
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU else 'vbstreamer.in'
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://ThaniOruvan25:ThaniOruvan25@cluster0.cjv4s.mongodb.net/cluster0?retryWrites=true&w=majority'))
    PING_INTERVAL = int(getenv('PING_INTERVAL', '500'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', '-1001584500398'))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split()))
