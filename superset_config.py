# from typing import Optional
import os
from datetime import timedelta

DATABASE_DIALECT = os.getenv("DATABASE_DIALECT")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_DB = os.getenv("DATABASE_DB")

# EXAMPLES_USER = os.getenv("EXAMPLES_USER")
# EXAMPLES_PASSWORD = os.getenv("EXAMPLES_PASSWORD")
# EXAMPLES_HOST = os.getenv("EXAMPLES_HOST")
# EXAMPLES_PORT = os.getenv("EXAMPLES_PORT")
# EXAMPLES_DB = os.getenv("EXAMPLES_DB")

# The SQLAlchemy connection string.
SQLALCHEMY_DATABASE_URI = (
    f"{DATABASE_DIALECT}://"
    f"{DATABASE_USER}:{DATABASE_PASSWORD}@"
    f"{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_DB}"
)

# SQLALCHEMY_EXAMPLES_URI = (
#     f"{DATABASE_DIALECT}://"
#     f"{EXAMPLES_USER}:{EXAMPLES_PASSWORD}@"
#     f"{EXAMPLES_HOST}:{EXAMPLES_PORT}/{EXAMPLES_DB}"
# )

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = os.getenv("REDIS_PORT", "6379")
REDIS_CELERY_DB = os.getenv("REDIS_CELERY_DB", "0")
REDIS_RESULTS_DB = os.getenv("REDIS_RESULTS_DB", "1")


LANGUAGES = {
    'en': {'flag': 'us', 'name': 'English'},
    "ru": {"flag": "ru", "name": "Russian"},
}

CURRENCIES = ["USD", "EUR", "RUR", "CNY"]


CACHE_DEFAULT_TIMEOUT = int(timedelta(days=1).total_seconds())


cache_redis_url = 'redis://redis:6379/0'

CACHE_CONFIG = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': 60 * 60 * 24,  # 1 day default (in secs)
    'CACHE_KEY_PREFIX': 'superset_results',
    'CACHE_REDIS_URL': cache_redis_url
}

FILTER_STATE_CACHE_CONFIG = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': 86400,
    'CACHE_KEY_PREFIX': 'filter_state_cache',
    'CACHE_REDIS_URL': cache_redis_url
}

EXPLORE_FORM_DATA_CACHE_CONFIG = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': 86400,
    'CACHE_KEY_PREFIX': 'explore_form_data_cache',
    'CACHE_REDIS_URL': cache_redis_url
}

DATA_CACHE_CONFIG = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': 60 * 60 * 24,  # 1 day default (in secs)
    'CACHE_KEY_PREFIX': 'data_cache',
    'CACHE_REDIS_URL': cache_redis_url
}
