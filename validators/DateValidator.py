import DayValidator
import MonthValidator
import YearValidator


class DateValidator:
    def __init__(self):
        pass

    month_validator = MonthValidator.MonthValidator
    day_validator = DayValidator.DayValidator
    year_validator = YearValidator.YearValidator

    @staticmethod
    def validate(month, day, year):
        valid_month = DateValidator.month_validator.validate(month)
        valid_day = DateValidator.day_validator.validate(day)
        valid_year = DateValidator.year_validator.validate(year)

        if valid_month and valid_day and valid_year:
            valid_date = dict(month=valid_month, day=valid_day, year=valid_year)
            return valid_date
        else:
            return None


def main():
    print 'validate(\'Jan\', \'mon\', \'1996\'): {}'.format(DateValidator.validate('Jan', 'mon', '1996'))
    print 'validate(\'Jan\', \'mon\', \'2017\'): {}'.format(DateValidator.validate('Jan', 'mon', '2017'))
    print 'validate(\'jasndj\', \'mon\', \'1996\'): {}'.format(DateValidator.validate('jasndj', 'mon', '1996'))
    print 'validate(\'Jan\', \'ladkjs\', \'1996\'): {}'.format(DateValidator.validate('Jan', 'ladkjs', '1996'))


if __name__ == '__main__':
    main()
