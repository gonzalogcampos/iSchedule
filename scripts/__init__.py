from scripts.config import CONFIGS, CONFIG
from scripts.employee import Employee, EMPLOYEES_FROM_DICT
from scripts.week import Week, WEEKS_FROM_DICT
from scripts.turn import Turn

if __name__ == '__main__':
    print(CONFIG(CONFIGS.GLOBAL))

    employees_data = CONFIG(CONFIGS.EMPLOYEES)
    employees = EMPLOYEES_FROM_DICT(employees_data)
    for employee in employees:
        print(employees[employee].dict())

    weeks_data = CONFIG(CONFIGS.WEEKS)
    weeks = WEEKS_FROM_DICT(weeks_data)
    for week in weeks:
        print(weeks[week].dict())

    pass
