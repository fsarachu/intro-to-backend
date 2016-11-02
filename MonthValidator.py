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

        self._month_abbreviations = {m[:3].lower(): m for m in self._months}

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
    print validator.validate('january')
    print validator.validate('some junk')
    print validator.validate('AUGUST')


if __name__ == '__main__':
    main()
