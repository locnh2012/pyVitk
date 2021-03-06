import logging
from logging.config import dictConfig
import os
import json


def setup_logging(default_path=None, default_level=logging.INFO, env_key='LOG_CFG'):
    """Setup logging configuration
    logging practice from: https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/
    """
    if default_path is None:
        import os
        this_dir, this_filename = os.path.split(__file__)
        path = os.path.join(this_dir, 'logging.json')
    else:
        path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
