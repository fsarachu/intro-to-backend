class MonthValidator:
    def __init__(self):

        self._months = (
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

        self._month_abbreviations = {month[:3].lower(): (index + 1, month) for index, month in enumerate(self._months)}

    @property
    def months(self):
        return self._months

    @property
    def month_abbreviations(self):
        return self._month_abbreviations

    def validate(self, month, abbreviation=True):
        month = month.capitalize()
        if month in self._months:
            return month
        else:
            return None


def main():
    validator = MonthValidator()

    print '\n--- Months ---'
    print validator.months

    print '\n--- Abbreviations ---'
    print sorted(validator.month_abbreviations, key=validator.month_abbreviations.__getitem__)

    print '\n--- Test Validations ---'
    print 'validate(\'january\'): {}'.format(validator.validate('january'))
    print 'validate(\'some junk\'): {}'.format(validator.validate('some junk'))
    print 'validate(\'AUGUST\'): {}'.format(validator.validate('AUGUST'))


if __name__ == '__main__':
    main()
