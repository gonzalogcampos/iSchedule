from scripts.config import CONFIG, CONFIGS
_DEF_CONTRACT = CONFIG(CONFIGS.DEF_EMP).get('contract', {})


class Contract():
    start = None
    end = None
    type = None
    hours = None
    free_days = None
    vacations = list()

    def __init__(self):
        pass

    def dict(self):
        dict = {
            "start": self.start,
            "end": self.end,
            "type": self.type,
            "hours": self.hours,
            "free_days": self.free_days,
            "vacations": self.vacations
        }
        return dict


def CONTRACT_FROM_DICT(data, set_def=True):
    contract = Contract()
    contract.start = data.get('start', None)
    contract.end = data.get("end", None)
    contract.type = data.get("type", None)
    contract.hours = data.get('hours', None)
    contract.free_days = data.get('free_days', None)
    contract.vacations = data.get('vacations', [])

    if set_def:
        contract.start = contract.start or _DEF_CONTRACT.get('start')
        contract.end = contract.end or _DEF_CONTRACT.get('end')
        contract.type = contract.type or _DEF_CONTRACT.get('type')
        contract.hours = contract.hours or _DEF_CONTRACT.get('hours')
        contract.free_days = contract.free_days or _DEF_CONTRACT.get('free_days')
        contract.vacations = contract.vacations or _DEF_CONTRACT.get('vacations', [])

    # Formatting vacations
    contract.vacations = [str(x) for x in contract.vacations]

    return contract
