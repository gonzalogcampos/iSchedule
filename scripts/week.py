from datetime import datetime
from scripts.exceptions import KeyNotValidException
import scripts.messages as msg

DAYS_OF_WEEK = {"MON": 0,
                "TUE": 1,
                "WED": 2,
                "THU": 3,
                "FRI": 4,
                "SAT": 5,
                "SUN": 6}


def CHECK_MON(key):
    date = datetime.strptime(str(key), '%Y%m%d')
    if not date.weekday() == 0:
        raise KeyNotValidException(msg.MESSAGE(msg.NOT_MONDAY).format(key))
    return key


def CHECK_KEY(key):
    datetime.strptime(str(key), '%Y%m%d')
    return key


class Day():
    def __init__(self, date):
        CHECK_KEY(date)
        self.__date = date
        self.turns = list()

    def __eq__(self, other):
        return self.date == other.date

    @property
    def date(self):
        return self.__date

    def add_turn(self, turn):
        if turn.day or turn in self.turns:
            return

        turn.day = self
        self.turns.append(turn)

    def remove_turn(self, turn):
        if turn not in self.turns:
            turn.day = None
            self.turns.remove(turn)

    def dict(self):
        d_turns = dict()
        for turn in self.turns:
            d_turn = {
                "h": turn.h,
                "n_employees": turn.n_employees
            }
            d_turns[turn.name] = d_turn
        return d_turns


class Week():
    def __init__(self, key):
        CHECK_MON(key)
        self.__key = key
        self.__days = [
            Day(key + 0),
            Day(key + 1),
            Day(key + 2),
            Day(key + 3),
            Day(key + 4),
            Day(key + 5),
            Day(key + 6)]

    def __eq__(self, other):
        return self.key == other.key

    @property
    def key(self):
        return self.__key

    @property
    def days(self):
        return self.__days

    def dict(self):
        d_week = {"key": self.key}
        d_days = dict()
        for day in range(len(self.days)):

            # Get day name
            name = None
            for d_name in DAYS_OF_WEEK:
                if day == DAYS_OF_WEEK[d_name]:
                    name = d_name
            if not name:
                continue

            d_days[name] = self.days[day].dict()

        d_week["days"] = d_days
        return d_week


def WEEKS_FROM_DICT(data):
    from scripts.turn import GET_TURN
    weeks = dict()
    for week in data:
        week_data = data[week]
        week_key = week_data.get("key")
        week_object = Week(week_key)
        week_days = week_data.get('days', {})
        for day in week_days:
            if day not in DAYS_OF_WEEK:
                continue
            day_data = week_days[day]
            day_object = week_object.days[DAYS_OF_WEEK[day]]
            turns_data = day_data.get("turns", {})
            for turn in turns_data:
                turn_data = turns_data[turn]
                turn = GET_TURN(turn, turn_data)
                day_object.add_turn(turn)
        weeks[week_key] = week_object
    return weeks
