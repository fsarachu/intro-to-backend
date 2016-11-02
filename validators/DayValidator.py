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
        if len(day) == 3:
            short_day = day.lower()
            if short_day in DayValidator.day_abbreviations:
                return DayValidator.days[DayValidator.day_abbreviations.index(short_day)]
            else:
                return None
        else:
            cap_day = day.capitalize()
            if cap_day in DayValidator.days:
                return cap_day
            else:
                return None


def main():
    print DayValidator.days
    print DayValidator.day_abbvs


if __name__ == '__main__':
    main()
