import DayValidator
import MonthValidator
import YearValidator


class DateValidator:
    def __init__(self):
        pass

    month_validator = MonthValidator.MonthValidator.validate
    day_validator = DayValidator.DayValidator.validate
    year_validator = YearValidator.YearValidator.validate

    @staticmethod
    def validate(month, day, year):
        valid_month = DateValidator.month_validator(month)
        valid_day = DateValidator.day_validator(day)
        valid_year = DateValidator.year_validator(year)

        if valid_month and valid_day and valid_year:
            valid_date = dict(month=valid_month, day=valid_day, year=valid_year)
            return valid_date
        else:
            return None
