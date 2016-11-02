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


def main():
    print DayValidator.days
    print DayValidator.day_abbvs


if __name__ == '__main__':
    main()
