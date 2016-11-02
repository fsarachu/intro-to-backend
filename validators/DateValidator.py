import DayValidator
import MonthValidator
import YearValidator


class DateValidator:
    def __init__(self):
        pass

    month_validator = MonthValidator.MonthValidator.validate
    day_validator = DayValidator.DayValidator.validate
    year_validator = YearValidator.YearValidator.validate
