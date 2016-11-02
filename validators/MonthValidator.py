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

        self._month_abbreviations = {month[:3].lower(): (index + 1, month) for index, month in enumerate(self.months)}
        self._month_numbers = {month[:3].lower(): index + 1 for index, month in enumerate(self.months)}

    @property
    def months(self):
        return self._months

    @property
    def month_abbreviations(self):
        return self._month_abbreviations

    @property
    def month_numbers(self):
        return self._month_numbers

    def validate(self, month, abbreviation=True):
        if month:
            month = month[:3].lower()
            return self.month_abbreviations.get(month)


def main():
    validator = MonthValidator()

    print '\n--- Months ---'
    print validator.months

    print '\n--- Abbreviations ---'
    print sorted(validator.month_abbreviations, key=validator.month_numbers.__getitem__)

    print '\n--- Test Validations ---'
    print 'validate(\'january\'): {}'.format(validator.validate('january'))
    print 'validate(\'some junk\'): {}'.format(validator.validate('some junk'))
    print 'validate(\'AUGUST\'): {}'.format(validator.validate('AUGUST'))


if __name__ == '__main__':
    main()
