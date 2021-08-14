from scripts.exceptions import EmployeeInTurnException
from scripts.exceptions import EmployeeNotInTurnException
from scripts.exceptions import KeyNotValidException
from datetime import datetime
import scripts.messages as msg


def VALID_H(h):
    try:
        datetime.strptime(str(h), '%H%M')
    except ValueError:
        raise KeyNotValidException(
            msg.MESSAGE(msg.NOT_VALID_H).format(h)
            )
    return True


class Turn():
    h = list()
    employees = list()
    n_employees = None
    name = None
    day = None

    def __init__(self, name, h, n_employees):
        self.h = h
        self.employees = list()
        self.n_employees = n_employees
        self.name = name

    def __eq__(self, other):
        return self.h == other.h and self.name == other.name

    def add_employee(self, employee):
        """Adds the employee to the turn

        Args:
            employee (Employee): Employee to add

        Raises:
            EmployeeInTurnException: If employee is not in turn
        """
        if employee in self.employees:
            raise EmployeeInTurnException(
                msg.MESSAGE(msg.EMP_IN_TURN).format(employee.name)
                )

        self.employees.append(employee)

    def remove_employee(self, employee):
        """Removes the employee from list

        Args:
            employee (Employee): Employee object

        Raises:
            EmployeeNotInTurnException: If employee is not in the turn
        """
        from scripts.employee import Employee
        if not isinstance(employee, Employee):
            raise ValueError(msg.MESSAGE(msg.NOT_EMPLOYEE))
        if employee not in self.employees:
            raise EmployeeNotInTurnException(employee.name)

        self.employees.remove(employee)

    def state(self):
        """Returns the difference between number of employees needad
        and number of emploees it hass

        Returns:
            int: n_employees - len(employees)
        """
        return self.n_employees - len(self.employees)


def GET_TURN(turn_name, data=dict()):
    from scripts.config import CONFIG, CONFIGS
    turn_d = CONFIG(CONFIGS.TURNS).get(turn_name)
    turn_d.update(data)
    h = turn_d.get('h')
    n_employees = turn_d.get('n_employees')
    turn = Turn(turn_name, h, n_employees)
    return turn
