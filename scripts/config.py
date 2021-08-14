from enum import Enum
import yaml
import os
from scripts.exceptions import ConfigNotFoundException


class CONFIGS():
    GLOBAL = 'global'
    LANGUAGE = 'language'
    EMPLOYEES = 'employees'
    WEEKS = 'weeks'
    DEF_EMP = 'def_emp'
    TURNS = 'turns'


BASE_PATH = '{}/../configs'.format(os.path.dirname(__file__))


def CONFIG(config_name):
    path = __GET_PATH(config_name)
    with open(path, 'r') as f:
        config = yaml.safe_load(f)
        f.close()
    return config


def __GET_PATH(config_name):
    path = "{0}/{1}.yml".format(BASE_PATH, config_name)
    if not os.path.isfile(path):
        raise ConfigNotFoundException(config_name)
    return path
