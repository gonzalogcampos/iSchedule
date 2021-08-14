from scripts.config import CONFIG, CONFIGS

_LANGUAGE = CONFIG(CONFIGS.GLOBAL).get('language', 'default')
_MESSAGES = CONFIG(CONFIGS.LANGUAGE)

# Messages list
NOT_MONDAY = 'NOT_MONADY'
NOT_VALID_H = 'NOT_VALID_H'
EMP_IN_TURN = 'EMP_IN_TURN'
EMP_OU_TURN = 'EMP_OU_TURN'
NOT_EMPLOYEE = 'NOT_EMPLOYEE'


def MESSAGE(name):
    message = _MESSAGES.get('name', None)
    if not message:
        return "UNKOWN MESSAGE"

    language = _LANGUAGE

    return message.get(language, "UNKONWN MESSAGE")
