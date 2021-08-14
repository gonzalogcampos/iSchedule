from scripts.config import CONFIG, CONFIGS
_DEF_RESTRICTIONS = CONFIG(CONFIGS.DEF_EMP).get('restrictions', {})


class Restrictions():
    works = dict()
    not_works = dict()
    wants = dict()

    def __init__(self):
        pass

    def dict(self):
        dict = {
            "works": self.works,
            "not_works": self.not_works,
            "wants": self.wants
        }
        return dict


def RESTRICTIONS_FROM_DICT(data, set_def=True):
    restrictions = Restrictions()
    restrictions.works = data.get("works", dict())
    restrictions.not_works = data.get("not_works", dict())
    restrictions.wants = data.get("wants", dict())

    if set_def:
        restrictions.works = restrictions.works or _DEF_RESTRICTIONS.get('works', {})
        restrictions.not_works = restrictions.not_works or _DEF_RESTRICTIONS.get('not_works', {})
        restrictions.wants = restrictions.wants or _DEF_RESTRICTIONS.get('wants', {})

    return restrictions
