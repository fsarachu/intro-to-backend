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

        self._month_abbreviations = [month[:3].lower() for month in self.months]

    @property
    def months(self):
        return self._months

    @property
    def month_abbreviations(self):
        return self._month_abbreviations

    def validate(self, month, abbreviation=True):
        short_month = month[:3].lower()

        if short_month in self.month_abbreviations:
            return self.months[self.month_abbreviations.index(short_month)]
        else:
            return None


def main():
    validator = MonthValidator()

    print '\n--- Months ---'
    print validator.months

    print '\n--- Abbreviations ---'
    print validator.month_abbreviations

    print '\n--- Test Validations ---'
    print 'validate(\'january\'): {}'.format(validator.validate('january'))
    print 'validate(\'some junk\'): {}'.format(validator.validate('some junk'))
    print 'validate(\'AUGUST\'): {}'.format(validator.validate('AUGUST'))


if __name__ == '__main__':
    main()
