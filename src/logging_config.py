LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters':
        {
            'default_formatter': {
                'format': '%(asctime)s:[%(levelname)s] %(message)s',
            },
            'json':
                {
                    '()':
                        "pythonjsonlogger.jsonlogger.JsonFormatter",
                    'format':
                        "%(asctime)s %(levelname)s %(name)s %(pathname)s %(lineno)s %(funcName)s %(message)s %(extra)s %(exc_info)s",    # noqa
                },
        },
    'handlers':
        {
            'stream_handler': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'default_formatter',
            },
            'json_stream_handler': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'json',
            },
            'json_rotatating_file_handler':
                {
                    'level': 'WARNING',
                    'class': 'logging.handlers.RotatingFileHandler',
                    'filename': 'logs/logs.jsonl',
                    'maxBytes': 1000,
                    'backupCount': 0,
                    'formatter': 'json',
                },
        },
    'loggers': {
        '': {
            'handlers': ['json_stream_handler'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
