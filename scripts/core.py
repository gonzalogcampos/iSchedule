_WEEKS = {}
_EMPLOYEES = {}


def GET_WEEK(day_key):
    from datetime import datetime
    date = datetime.strftime(str(day_key), "%Y%m%d")
    monday = date + datetime.timedelta(days=date.weekday)
    day_key = int(date.strftime("%Y%m%d"))
    return _WEEKS.get(day_key)


def FILL_WEEK(week_key):
    week = _WEEKS.get(week_key, None)

    if not week:
        return

    extras = [e for e in _EMPLOYEES if e.contract.type == "extra"]
    full = [e for e in _EMPLOYEES if e.contract.type == "full"]

    # Fill all days with full-contract employees
    for day in week.days:
        for employee in full:
            for turn in day:
                if employee.can_work(turn, day):
                    turn.add_employee(employee)
                    break

    # Fill all days with extra-contract employees
    for day in week.days:
        for employee in extras:
            for turn in day:
                if employee.can_work(turn, day):
                    turn.add_employee(employee)
                    break


def MUST_WORK(employee, turn):
    # Check if employee must work in this day
    return employee.must_work(turn.day.date)

def CAN_WORK(employee, turn):
    # Check contract restrictions
    #   - Start/End
    #   - Vacations
    # Check viability
    #   - Filled turn
    #   - Filled week
    # Check restrictions restrictions
    #   - Worksss
    #   - Not works
    #   - Wants
    return False, 3
    if employee.contract_viability(turn.day.date)
    employee.restrictions_viability(turn.day.date)
