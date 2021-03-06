# Default configuration for xtas.
# Can be overridden by an xtas_config module in the PYTHONPATH, with the same
# general structure as this module.

CELERY = dict(
    BROKER_URL='amqp://',
    CELERY_RESULT_BACKEND='amqp://',

    CELERY_TASK_SERIALIZER='json',
    CELERY_RESULT_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_TIMEZONE='Europe/Amsterdam',
    CELERY_ENABLE_UTC=True,

    CELERY_TASK_RESULT_EXPIRES=3600,

    # Uncomment the following to make Celery tasks run locally (for debugging).
    #CELERY_ALWAYS_EAGER=True,
)

ELASTICSEARCH = [
    {"host": "localhost", "port": 9200},
    # add more hosts here
]

# Additional modules to load in the worker and webserver.
EXTRA_MODULES = [
]
