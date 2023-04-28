from configparser import ConfigParser
from datetime import datetime


class dotdict(dict):
    """dot.notation access to dictionary attributes"""

    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


def load_config(config_file: str) -> dotdict:
    # Load config from the specified file
    config = ConfigParser()
    config.read(config_file)

    # Convert configuration to dotdict
    dot_config = dotdict()
    for section in config.sections():
        dot_config[section] = dotdict()
        for key, value in config.items(section):
            dot_config[section][key] = value
            if section == "chatwoot":
                if key == "account_id":
                    dot_config[section][key] = int(value)
                if key == "inbox_id":
                    dot_config[section][key] = int(value)
            if section == "service":
                if key == "port":
                    dot_config[section][key] = int(value)

    return dot_config
