from scripts.exceptions import EmployeeExistException
from scripts.contratct import CONTRACT_FROM_DICT, Contract
from scripts.restrictions import RESTRICTIONS_FROM_DICT, Restrictions
from scripts.config import CONFIG, CONFIGS

_EMPLOYEES_KEYS = list()
_DEF_EMP = CONFIG(CONFIGS.DEF_EMP)


class Employee():
    tel = None
    mail = None
    contract = Contract()
    restrictions = Restrictions()
    __name = None

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def dict(self):
        dict = {}
        dict['name'] = self.name
        dict['tel'] = self.tel
        dict['mail'] = self.mail
        dict['contract'] = self.contract.dict()
        dict['restrictions'] = self.restrictions.dict()
        return dict

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        global _EMPLOYEES_KEYS
        if name in _EMPLOYEES_KEYS:
            raise EmployeeExistException(name)

        if self.name in _EMPLOYEES_KEYS:
            _EMPLOYEES_KEYS.remove(self.name)
        _EMPLOYEES_KEYS.append(name)

        self.__name = name

    def contract_viability(self, day):
        if self.contract.start > day or self.contract.end < day:
            return False
        for vacation in self.contract.vacations:
            vac = vacation.split('-')
            if len(vac) == 1:  # Single day
                if int(vac[0]) == day:
                    return False
            elif len(vac) == 2:  # Range
                if int(vac[0]) > day or int(vac[1]) < day:
                    return False
        return True

    def check_restrictions_works(self, day):
        pass

    def check_restrictions_not_works(self, day):
        pass

    def check_restrictions_wants(self, day):
        pass

    def restrictions_viability(self, day):
        from scripts.week import DAYS_OF_WEEK
        from datetime import datetime
        viability = True
        level = None  # Free to work

        for restriction in self.restrictions:
            if restriction in DAYS_OF_WEEK:
                datetime.strftime(str(day), "%Y%m%d")
    

def EMPLOYEES_FROM_DICT(data, set_def=True):
    employees = dict()
    for name in data:

        # Get data
        employee_data = data.get(name, {})
        tel = employee_data.get("tel", None)
        mail = employee_data.get("mail", None)
        contract = employee_data.get("contract", {})
        restrictions = employee_data.get("restrictions", {})

        # Set defaults
        if set_def:
            tel = tel or _DEF_EMP.get('tel', None)
            mail = mail or _DEF_EMP.get('mail', None)

        employee = Employee(name)
        employee.tel = tel
        employee.mail = mail
        employee.contract = CONTRACT_FROM_DICT(contract, set_def=set_def)
        employee.restrictions = RESTRICTIONS_FROM_DICT(restrictions, set_def=set_def)
        employees[name] = employee
    return employees
