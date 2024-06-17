import re
from os import environ,getenv

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', ''))
SESSION = environ.get('SESSION', 'Media_search')
LOG_STR = "Current Cusomized Configurations are:-\n"
PORT = environ.get("PORT", "8080")
