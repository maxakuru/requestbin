import os
from urllib.parse import urlparse

import logging
log = logging.getLogger('gunicorn.error')


DEBUG = True
REALM = os.environ.get('REALM', 'local')

PORT_NUMBER = os.environ.get("PORT", 5000)
ROOT_URL = os.environ.get("ROOT_URL", f"http://localhost:{PORT_NUMBER}")

FLASK_SESSION_SECRET_KEY = os.environ.get("SESSION_SECRET_KEY", "N1BKhJLnBqLpexOZdklsfDKFJDKFadsfs9a3r324YB7B73AglRmrHMDQ9RhXz35")

BIN_TTL = int(os.environ.get("BIN_TTL", f'{48*3600}')) # 48 hours
STORAGE_BACKEND = os.environ.get("STORAGE_BACKEND", "requestbin.storage.memory.MemoryStorage")
MAX_RAW_SIZE = int(os.environ.get("MAX_RAW_SIZE", f'{1024*10}'))
IGNORE_HEADERS = []
MAX_REQUESTS = int(os.environ.get("MAX_REQUESTS", f'{1000}'))
CLEANUP_INTERVAL = int(os.environ.get("CLEANUP_INTERVAL", f'{3600}'))

REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost:6379/0")
url_parts = urlparse(REDIS_URL)
REDIS_HOST = url_parts.hostname
REDIS_PORT = url_parts.port
REDIS_PASSWORD = url_parts.password
REDIS_DB = url_parts.fragment

# REDIS_URL = "redis://localhost:6379/0"
# REDIS_HOST = "localhost"
# REDIS_PORT = 6379
# REDIS_PASSWORD = None
# REDIS_DB = 9

REDIS_PREFIX = "requestbin"

if REALM == 'prod':
    DEBUG = False
    ROOT_URL = os.environ.get("ROOT_URL", ROOT_URL)

    FLASK_SESSION_SECRET_KEY = os.environ.get("SESSION_SECRET_KEY", FLASK_SESSION_SECRET_KEY)

    STORAGE_BACKEND = "requestbin.storage.redis.RedisStorage"

    REDIS_URL = os.environ.get("REDIS_URL")
    url_parts = urlparse(REDIS_URL)
    REDIS_HOST = url_parts.hostname
    REDIS_PORT = url_parts.port
    REDIS_PASSWORD = url_parts.password
    REDIS_DB = url_parts.fragment

    IGNORE_HEADERS = """
X-Varnish
X-Forwarded-For
X-Heroku-Dynos-In-Use
X-Request-Start
X-Heroku-Queue-Wait-Time
X-Heroku-Queue-Depth
X-Real-Ip
X-Forwarded-Proto
X-Via
X-Forwarded-Port
""".split("\n")[1:-1]

log.debug(f'[config] DEBUG: {DEBUG}')
log.debug(f'[config] REALM: {REALM}')
log.debug(f'[config] PORT_NUMBER: {PORT_NUMBER}')
log.debug(f'[config] ROOT_URL: {ROOT_URL}')
log.debug(f'[config] BIN_TTL: {BIN_TTL}')
log.debug(f'[config] STORAGE_BACKEND: {STORAGE_BACKEND}')
log.debug(f'[config] MAX_RAW_SIZE: {MAX_RAW_SIZE}')
log.debug(f'[config] IGNORE_HEADERS: {IGNORE_HEADERS}')
log.debug(f'[config] MAX_REQUESTS: {MAX_REQUESTS}')
log.debug(f'[config] CLEANUP_INTERVAL: {CLEANUP_INTERVAL}')
# log.debug(f'[config] REDIS_URL: {REDIS_URL}')
log.debug(f'[config] REDIS_HOST: {REDIS_HOST}')
log.debug(f'[config] REDIS_PORT: {REDIS_PORT}')
# log.debug(f'[config] REDIS_PASSWORD: {REDIS_PASSWORD}')
log.debug(f'[config] REDIS_DB: {REDIS_DB}')