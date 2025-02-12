import logging
from logging.config import dictConfig

dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": False,
        "filters": {  # correlation ID filter must be added here to make the %(correlation_id)s formatter work
            "correlation_id": {
                "()": "asgi_correlation_id.CorrelationIdFilter",
                "uuid_length": 36,
                "default_value": "-",
            },
        },
        "formatters": {
            "console": {
                "class": "logging.Formatter",
                # formatter decides how our console logs look, and what info is included.
                # adding %(correlation_id)s to this format is what make correlation IDs appear in our logs
                "format": "[%(levelname)s] [%(asctime)s] [%(module)s:%(lineno)d] [%(correlation_id)s] %(message)s",
            },
            "access": {
                "()": "uvicorn.logging.AccessFormatter",
                "fmt": '[%(levelprefix)s] [%(asctime)s] [%(correlation_id)s] [%(client_addr)s] - "%(request_line)s" %(status_code)s',
                "use_colors": None,
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                # Filter must be declared in the handler, otherwise it won't be included
                "filters": ["correlation_id"],
                "formatter": "console",
            },
            "access": {
                "class": "logging.StreamHandler",
                # Filter must be declared in the handler, otherwise it won't be included
                "filters": ["correlation_id"],
                "formatter": "access",
            },
        },
        # Loggers can be specified to set the log-level to log, and which handlers to use
        "loggers": {
            # project logger
            "gc-pdf-util": {"handlers": ["console"], "level": "DEBUG", "propagate": True},
            # third-party package loggers
            "asgi_correlation_id": {"handlers": ["console"], "level": "WARNING"},
            "uvicorn.access": {"handlers": ["access"], "level": "INFO"}
        },
    }
)
# logging.basicConfig(
#     # level=logging.DEBUG,
#     format="%(asctime)s - %(levelname)s [%(correlation_id)s] - %(message)s",
# )

logger = logging.getLogger("gc-pdf-util")
logger.setLevel(logging.DEBUG)

