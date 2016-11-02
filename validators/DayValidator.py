class DayValidator:
    def __init__(self):
        pass

    days = (
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thurdsday',
        'Friday',
        'Saturday',
        'Sunday'
    )

    day_abbvs = tuple([day[:3].lower() for day in days])

    @staticmethod
    def validate(day):
        """Validates either a 3 letter day abbreviation or a full day. Returns full day if valid, else None"""
        day = day.strip()

        if len(day) == 3:
            short_day = day.lower()
            if short_day in DayValidator.day_abbvs:
                return DayValidator.days[DayValidator.day_abbvs.index(short_day)]
            else:
                return None
        else:
            cap_day = day.capitalize()
            if cap_day in DayValidator.days:
                return cap_day
            else:
                return None


def main():
    print '\n--- Days ---'
    print DayValidator.days

    print '\n--- Day Abbreviations ---'
    print DayValidator.day_abbvs

    print '\n--- Test Validations ---'
    print 'validate(\'monday\'): {}'.format(DayValidator.validate('monday'))
    print 'validate(\'MON\'): {}'.format(DayValidator.validate('MON'))
    print 'validate(\'tueasdlkas\'): {}'.format(DayValidator.validate('tueasdlkas'))
    print 'validate(\'tue\'): {}'.format(DayValidator.validate('tue'))
    print 'validate(\'SUNDAY\'): {}'.format(DayValidator.validate('SUNDAY'))
    print 'validate(\'Some junk\'): {}'.format(DayValidator.validate('Some junk'))


if __name__ == '__main__':
    main()
