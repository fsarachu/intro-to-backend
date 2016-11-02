class MonthValidator:
    def __init__(self):
        pass

    months = (
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
    )

    month_abbreviations = [month[:3].lower() for month in months]

    @staticmethod
    def validate(month):
        """Validates either a 3 letter month abbreviation or a full month. Returns full month if valid, else None"""
        if len(month) == 3:
            short_month = month.lower()
            if short_month in MonthValidator.month_abbreviations:
                return MonthValidator.months[MonthValidator.month_abbreviations.index(short_month)]
            else:
                return None
        else:
            capitalized_month = month.capitalize()
            if capitalized_month in MonthValidator.months:
                return capitalized_month
            else:
                return None


def main():
    print '\n--- Months ---'
    print MonthValidator.months

    print '\n--- Abbreviations ---'
    print MonthValidator.month_abbreviations

    print '\n--- Test Validations ---'
    print 'validate(\'january\'): {}'.format(MonthValidator.validate('january'))
    print 'validate(\'some junk\'): {}'.format(MonthValidator.validate('some junk'))
    print 'validate(\'Febdksjadklas\'): {}'.format(MonthValidator.validate('Febdksjadklas'))
    print 'validate(\'FEB\'): {}'.format(MonthValidator.validate('FEB'))
    print 'validate(\'may\'): {}'.format(MonthValidator.validate('may'))
    print 'validate(\'AUGUST\'): {}'.format(MonthValidator.validate('AUGUST'))


if __name__ == '__main__':
    main()
